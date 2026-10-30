#!/usr/bin/env python3
"""Minimal CI smoke checks for the stdlib PDS assembler."""

from __future__ import annotations

import importlib.util
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_assembler():
    path = ROOT / "pds6502.py"
    spec = importlib.util.spec_from_file_location("pds6502", path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_help_exits_zero() -> None:
    for script in ("pds6502.py", "pds_extract.py"):
        r = subprocess.run(
            [sys.executable, str(ROOT / script), "--help"],
            check=False,
            capture_output=True,
            text=True,
        )
        assert r.returncode == 0, f"{script} --help failed: {r.stderr}"


def test_assemble_smoke() -> None:
    m = load_assembler()
    with tempfile.TemporaryDirectory() as tmp:
        src = pathlib.Path(tmp) / "smoke.pds"
        # Directives and instructions must be indented (column-0 names are labels).
        src.write_text("\torg $8000\nstart\n\tlda #$12\n\tldx #$34\n\trts\n")
        prg = bytearray(128 * 1024)
        asm = m.Assembler(prg, src.parent, [src.parent])
        asm.run_file(src, slot=0)
        assert asm.sym.get("start") == 0x8000
        assert prg[0:5] == bytes([0xA9, 0x12, 0xA2, 0x34, 0x60])


def test_setup_option_loader() -> None:
    m = load_assembler()
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        (root / "SETUP.PDS").write_text(
            "; test\noption 0,0\n", encoding="utf-8"
        )
        src = root / "main.pds"
        src.write_text("\torg $8000\n\tnop\n")
        prg = bytearray(128 * 1024)
        asm = m.Assembler(prg, root, [root])
        asm.run_file(src, slot=0)
        assert asm.selector_swap == 0


def main() -> int:
    test_help_exits_zero()
    test_assemble_smoke()
    test_setup_option_loader()
    print("smoke_test: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
