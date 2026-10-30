# pds6502

[![CI](https://github.com/ap0ught/pds6502/actions/workflows/ci.yml/badge.svg)](https://github.com/ap0ught/pds6502/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/ap0ught/pds6502)](https://github.com/ap0ught/pds6502/releases/latest)

PDS 1.26 assembler for the Super Robin Hood and Magician sources. Both games
assemble with this module. Each game keeps its own build script, because the
cartridges are different machines: Super Robin Hood is mapper 71 with 16 KiB
banks, and Magician is MMC3 with 8 KiB slots.

Clone this repository next to the game:

```
games/pds6502
games/SuperRobinHoodNESSource
games/magician-nes
```

Each game's `asm/pds6502.py` is a short loader. It imports `pds6502.py` from
the sibling checkout. `PDS6502_HOME` overrides that path when the checkout
lives somewhere else.

```
python3 asm/build_srh.py     # Super Robin Hood
python3 asm/build.py         # Magician
```

## Assembler option 0

`<expr` and `>expr` each return one byte of a 16-bit value. Which arrow is the
low byte is assembler option 0, the editor's "Swap < and >" switch (editor
manual, section 9.2.3):

| `option 0,n` | `>$1234` | `<$1234` |
| --- | --- | --- |
| 0 | `$12` | `$34` |
| 1 | `$34` | `$12` |

1 is the 6502 manual default: the arrow points at the byte. PDS loaded
`SETUP.PDS` from the project directory before assembling (editor manual,
section 9.2.8). [`examples/SETUP.PDS`](examples/SETUP.PDS) is that file for a
project whose source never sets the switch. It selects 1, which is what the
Super Robin Hood cartridge was built with.

Magician does not use that file. `X0.PDS` begins with `option 0,0`, and the
assembler honors the directive.

`radix 10` is the default. `send` is ignored. The listing switches in the
assembler menu do not change the bytes.

## Documentation

The `docs/` directory holds markdown transcriptions of the PDS manuals:

- `The_PDS_6502_Manual.md` — the assembler language this module implements
- `The_PDS_Editor_Manual.md` — the editor, including assembler option 0 and `SETUP.PDS`
- `P.D.S._Manual.md`, `PDS_guide_early_version.md`, `The_PDS_Z80_Manual.md` — the rest of the set

## What a game build owns

This module writes a flat PRG image and, on the last pass of `run_all`, records
the bytes each `bank` directive downloaded. Placing those bytes into an iNES
ROM is the game's build. Super Robin Hood files mapper 71 banks. Magician
searches MMC3 slots and reads the flat image. Pointing one game's build at the
other source will put the bytes in the wrong places.

## Releases

Tagged releases (`v*`) publish a source archive of the assembler via
[GitHub Actions](https://github.com/ap0ught/pds6502/actions/workflows/release.yml).
Push a tag, or run the Release workflow from the Actions tab:

```
git tag v1.0.1
git push origin v1.0.1
```

Game builds that clone this repository (or set `PDS6502_HOME`) do not need the
release artifacts; the tag is for pinned downloads and changelog tracking.
