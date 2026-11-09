#!/usr/bin/env python3
"""Classies Chronicles v0.08.00: truthful geometric collage assembly/slicing.

Dependencies: Python 3.9+, Pillow. Examples:

    python cc_comic_collage_v008.py --self-test
    python cc_comic_collage_v008.py inspect --input sheet.png --cols 4 --rows 4
    python cc_comic_collage_v008.py slice --input sheet.png --cols 4 --rows 4 --output-dir cropped
    python cc_comic_collage_v008.py assemble --inputs page01.png page02.png page03.png page04.png --cols 2 --rows 2 --output sheet.png

Default minimum native individual-page width = 1080px. For a preview-only
geometry check of smaller tiles, supply --allow-preview; the report will
explicitly mark preview-only. This tool verifies raster geometry and real
file inventory; it CANNOT certify story fidelity, rights, character continuity,
legibility, final challenge placement or answer secrecy.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
import unittest
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List, Tuple

try:
    from PIL import Image
except ImportError as exc:
    raise SystemExit("Pillow is required: pip install Pillow") from exc


class GeometryError(ValueError):
    pass


@dataclass(frozen=True)
class Grid:
    cols: int
    rows: int
    margin_x: int = 0
    margin_y: int = 0
    gutter_x: int = 0
    gutter_y: int = 0

    def validate(self) -> None:
        if self.cols < 1 or self.rows < 1:
            raise GeometryError("cols and rows must be positive")
        if min(self.margin_x, self.margin_y, self.gutter_x, self.gutter_y) < 0:
            raise GeometryError("margins and gutters must not be negative")
        if self.cols * self.rows > 256:
            raise GeometryError("Maximum supported batch is 256 cells")

    def outer_size(self, w: int, h: int) -> Tuple[int, int]:
        self.validate()
        return (2 * self.margin_x + self.cols * w + (self.cols - 1) * self.gutter_x,
                2 * self.margin_y + self.rows * h + (self.rows - 1) * self.gutter_y)

    def cell_size(self, outer_w: int, outer_h: int) -> Tuple[int, int]:
        self.validate()
        available_w = outer_w - 2 * self.margin_x - (self.cols - 1) * self.gutter_x
        available_h = outer_h - 2 * self.margin_y - (self.rows - 1) * self.gutter_y
        if available_w <= 0 or available_h <= 0:
            raise GeometryError("Margins and gutters leave no cell area")
        if available_w % self.cols or available_h % self.rows:
            raise GeometryError("Sheet bounds do not divide into equal integer cells")
        w, h = available_w // self.cols, available_h // self.rows
        if 16 * w != 9 * h:
            raise GeometryError(f"Each cell must be exactly 9:16; got {w}x{h}")
        return w, h

    def box(self, row: int, col: int, w: int, h: int) -> Tuple[int, int, int, int]:
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise GeometryError("Cell index out of bounds")
        x = self.margin_x + col * (w + self.gutter_x)
        y = self.margin_y + row * (h + self.gutter_y)
        return x, y, x + w, y + h


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def image_dimensions(path: Path) -> Tuple[int, int]:
    if not path.is_file():
        raise GeometryError(f"Missing input image: {path}")
    with Image.open(path) as im:
        im.verify()
    with Image.open(path) as im:
        return im.size


def width_policy(width: int, minimum: int, allow_preview: bool) -> str:
    if minimum < 1:
        raise GeometryError("Minimum cell width must be positive")
    if width < minimum:
        if not allow_preview:
            raise GeometryError(f"Native cell width {width} < {minimum}; rerender larger or pass --allow-preview")
        return "PREVIEW_ONLY_BELOW_MINIMUM_NATIVE_WIDTH"
    return "GEOMETRY_ONLY_REQUIRES_HUMAN_PIXEL_QA"


def inspect(sheet: Path, grid: Grid, min_width: int, allow_preview: bool) -> dict:
    width, height = image_dimensions(sheet)
    w, h = grid.cell_size(width, height)
    quality_status = width_policy(w, min_width, allow_preview)
    return {
        "operation": "inspect", "sheet": str(sheet), "sheet_sha256": sha256(sheet),
        "sheet_dimensions": [width, height], "grid": asdict(grid),
        "page_count": grid.cols * grid.rows, "native_cell_dimensions": [w, h],
        "geometry_status": quality_status,
        "semantic_qa": "NOT_CHECKED; visual/human review required",
        "cells": [{"index": row * grid.cols + col + 1, "row": row + 1, "column": col + 1,
                   "crop_box_xyxy": list(grid.box(row, col, w, h))}
                  for row in range(grid.rows) for col in range(grid.cols)]
    }


def do_slice(sheet: Path, outdir: Path, grid: Grid, min_width: int, allow_preview: bool) -> dict:
    report = inspect(sheet, grid, min_width, allow_preview)
    outdir.mkdir(parents=True, exist_ok=True)
    output_paths = [outdir / f"comic_page_{i:02d}.png" for i in range(1, grid.cols * grid.rows + 1)]
    for p in output_paths:
        if p.exists():
            raise GeometryError(f"Refusing to overwrite existing file: {p}")
    with Image.open(sheet) as original:
        for cell, outpath in zip(report["cells"], output_paths):
            cropped = original.crop(tuple(cell["crop_box_xyxy"]))
            if 16 * cropped.width != 9 * cropped.height:
                raise GeometryError("Internal error: crop was not 9:16")
            cropped.save(outpath, format="PNG")
            cell["file"] = str(outpath)
            cell["actual_dimensions"] = [cropped.width, cropped.height]
            cell["sha256"] = sha256(outpath)
    report["operation"] = "slice"
    report["sliced_file_count"] = len(output_paths)
    report["actual_files_exist"] = all(path.is_file() for path in output_paths)
    return report


def do_assemble(paths: List[Path], outpath: Path, grid: Grid,
                min_width: int, allow_preview: bool) -> dict:
    grid.validate()
    if len(paths) != grid.cols * grid.rows:
        raise GeometryError(f"Expected {grid.cols * grid.rows} distinct page files, received {len(paths)}")
    resolved = [p.resolve() for p in paths]
    if len(set(resolved)) != len(resolved):
        raise GeometryError("Repeated input files are not allowed")
    if outpath.exists():
        raise GeometryError(f"Refusing to overwrite existing output: {outpath}")
    if outpath.resolve() in resolved:
        raise GeometryError("Output must not be an input")
    dims = [image_dimensions(p) for p in paths]
    if len(set(dims)) != 1:
        raise GeometryError("All source pages must have the same native dimensions")
    w, h = dims[0]
    if 16 * w != 9 * h:
        raise GeometryError("Source pages must each be exactly 9:16")
    quality = width_policy(w, min_width, allow_preview)
    W, H = grid.outer_size(w, h)
    if W * H > 150_000_000:
        raise GeometryError("Composite exceeds 150 million pixels; use smaller batches")
    outpath.parent.mkdir(parents=True, exist_ok=True)
    collage = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    inventory = []
    for index, path in enumerate(paths):
        row, col = divmod(index, grid.cols)
        box = grid.box(row, col, w, h)
        with Image.open(path) as im:
            collage.paste(im.convert("RGBA"), (box[0], box[1]))
        inventory.append({"index": index + 1, "source": str(path),
                          "source_sha256": sha256(path), "crop_box_xyxy": list(box)})
    collage.save(outpath, format="PNG")
    return {"operation": "assemble", "sheet": str(outpath), "sheet_sha256": sha256(outpath),
            "sheet_dimensions": [W, H], "grid": asdict(grid),
            "native_cell_dimensions": [w, h], "page_count": len(paths),
            "geometry_status": quality, "semantic_qa": "NOT_CHECKED; human review required",
            "pages": inventory}


class GeometryTests(unittest.TestCase):
    def test_4x4_target(self):
        self.assertEqual(Grid(4, 4).outer_size(1080, 1920), (4320, 7680))
        self.assertEqual(Grid(4, 4).cell_size(4320, 7680), (1080, 1920))

    def test_4x4_preview(self):
        self.assertEqual(Grid(4, 4).cell_size(1080, 1920), (270, 480))
        with self.assertRaises(GeometryError):
            width_policy(270, 1080, False)
        self.assertIn("PREVIEW", width_policy(270, 1080, True))

    def test_alternative_grids(self):
        self.assertEqual(Grid(2, 2).outer_size(1080, 1920), (2160, 3840))
        self.assertEqual(Grid(2, 4).outer_size(1080, 1920), (2160, 7680))
        self.assertEqual(Grid(2, 8).outer_size(1080, 1920), (2160, 15360))
        self.assertEqual(Grid(1, 16).outer_size(1080, 1920), (1080, 30720))

    def test_gutter_margin_exact(self):
        grid = Grid(2, 2, margin_x=3, margin_y=5, gutter_x=7, gutter_y=11)
        self.assertEqual(grid.outer_size(108, 192), (229, 405))
        self.assertEqual(grid.cell_size(229, 405), (108, 192))
        self.assertEqual(grid.box(1, 1, 108, 192), (118, 208, 226, 400))

    def test_reject_unequal_cells(self):
        with self.assertRaises(GeometryError):
            Grid(4, 4).cell_size(1081, 1920)

    def test_reject_wrong_page_ratio(self):
        with self.assertRaises(GeometryError):
            Grid(1, 1).cell_size(1080, 1800)

    def test_actual_roundtrip_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            paths = []
            palette = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 200, 0)]
            for index, color in enumerate(palette, 1):
                path = base / f"source_{index}.png"
                Image.new("RGB", (108, 192), color).save(path)
                paths.append(path)
            sheet = base / "sheet.png"
            report = do_assemble(paths, sheet, Grid(2, 2), 108, False)
            self.assertEqual(report["page_count"], 4)
            cuts = do_slice(sheet, base / "cuts", Grid(2, 2), 108, False)
            self.assertEqual(cuts["sliced_file_count"], 4)
            for i, color in enumerate(palette, 1):
                with Image.open(base / "cuts" / f"comic_page_{i:02d}.png") as im:
                    self.assertEqual(im.convert("RGB").getpixel((50, 50)), color)

    def test_overwrite_prevention(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            p = base / "in.png"
            Image.new("RGB", (108, 192), "white").save(p)
            with self.assertRaises(GeometryError):
                do_assemble([p], p, Grid(1, 1), 108, False)

    def test_reject_repeated_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "a.png"
            Image.new("RGB", (108, 192), "white").save(p)
            with self.assertRaises(GeometryError):
                do_assemble([p, p], p.parent / "out.png", Grid(2, 1), 108, False)

    def test_reject_wrong_page_count(self):
        with self.assertRaises(GeometryError):
            do_assemble([], Path("unused.png"), Grid(2, 2), 1080, False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--self-test", action="store_true", help="run offline unit tests and exit")
    sub = parser.add_subparsers(dest="operation")
    for action in ("inspect", "slice", "assemble"):
        sp = sub.add_parser(action)
        sp.add_argument("--cols", type=int, required=True)
        sp.add_argument("--rows", type=int, required=True)
        sp.add_argument("--margin-x", type=int, default=0)
        sp.add_argument("--margin-y", type=int, default=0)
        sp.add_argument("--gutter-x", type=int, default=0)
        sp.add_argument("--gutter-y", type=int, default=0)
        sp.add_argument("--min-cell-width", type=int, default=1080)
        sp.add_argument("--allow-preview", action="store_true")
        if action == "assemble":
            sp.add_argument("--inputs", nargs="+", type=Path, required=True)
            sp.add_argument("--output", type=Path, required=True)
        else:
            sp.add_argument("--input", type=Path, required=True)
            if action == "slice":
                sp.add_argument("--output-dir", type=Path, required=True)
        sp.add_argument("--manifest", type=Path, help="optional actual JSON report filename")
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(GeometryTests))
        return 0 if result.wasSuccessful() else 1
    if not args.operation:
        parser.print_help()
        return 2
    grid = Grid(args.cols, args.rows, args.margin_x, args.margin_y, args.gutter_x, args.gutter_y)
    try:
        if args.manifest and args.manifest.exists():
            raise GeometryError("Refusing to overwrite existing manifest")
        if args.operation == "inspect":
            result = inspect(args.input, grid, args.min_cell_width, args.allow_preview)
        elif args.operation == "slice":
            result = do_slice(args.input, args.output_dir, grid, args.min_cell_width, args.allow_preview)
        else:
            result = do_assemble(args.inputs, args.output, grid, args.min_cell_width, args.allow_preview)
    except (GeometryError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    serial = json.dumps(result, indent=2, ensure_ascii=False)
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(serial + "\n", encoding="utf-8")
    print(serial)
    return 0


if __name__ == "__main__":
    sys.exit(main())
