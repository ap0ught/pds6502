---
name: pds6502-scope
description: >-
  Identifies the PDS 1.26 6502 assembler and which sources it can assemble.
  Use when working in pds6502, Super Robin Hood, Magician, Dizzy, D3,
  SourceDIZZY3, Wireframe19, beebasm, NESASM, or any .PDS/.ROU/.PRJ tree.
---

# What pds6502 assembles

This repo is the PDS 1.26 6502 assembler shared by Super Robin Hood and Magician. It is not a Z80 assembler. It is not beebasm. It is not NESASM.

Assemble only those two games' PDS 6502 sources.

Do not treat Dizzy 3, SourceDIZZY3, or Wireframe19 as a 6502 target. That source is Z80 (`ld`, `out (c),a`, `skip`, Spectrum and Amstrad). The container header matches, and `pds_extract.py` can decode it. Decoding is not assembling.

Reject a tree when you see any of these:

- Z80: `ld a`, `computer=spectrum`, `skip 10`
- beebasm: `INCLUDE "file"`, `.label`, `{ }` scopes, `EQUB`, `MACRO` / `ENDMACRO`
- NESASM: `.inesprg`, `.bank`, `.org`, `.rsset`

PDS 6502 looks like column-0 labels, `name macro`, `defb` / `cbm`, `org $fffa`, and `send computer1` next to `$2002` or `$4016`.
