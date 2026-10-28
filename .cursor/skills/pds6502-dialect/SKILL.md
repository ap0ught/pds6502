---
name: pds6502-dialect
description: >-
  Applies PDS 6502 assembler option 0, SETUP.PDS, stop_at_end, and zero-page
  versus absolute addressing. Use when editing pds6502.py, byte selectors,
  option 0, SETUP.PDS, bank placement, or an instruction that changed size.
---

# Dialect switches

## Option 0

`<expr` and `>expr` each return one byte of a 16-bit value. Assembler option 0 chooses which arrow is the low byte (editor manual 9.2.3):

| `option 0,n` | `>$1234` | `<$1234` |
| --- | --- | --- |
| 0 | `$12` | `$34` |
| 1 | `$34` | `$12` |

1 is the 6502 manual default: the arrow points at the byte. Super Robin Hood never sets the switch in the program. PDS loaded `SETUP.PDS` from the project directory first (editor manual 9.2.8). `examples/SETUP.PDS` is that file, and it selects 1. `ROBIN.PRJ` is the file list, not the setup.

Magician does not use `SETUP.PDS`. `X0.PDS` begins with `option 0,0`, and the assembler honors that directive. Do not add a Magician `SETUP.PDS`.

`run_all` resets `selector_swap` to the setup default at the start of each attempt. `run_file` does not, so a directive set earlier in the same assembler still applies.

## stop_at_end

`stop_at_end` defaults to True. A source `end` finishes the PDS program. Super Robin Hood relies on that: `END` in `ENDCODE.ROU` skips `JUNK`.

Magician's build sets `stop_at_end = False` on both `Assembler` constructors. `X7.PDS` ends Eurocom's program, and `src/magician` overlays assemble after it. Setting the flag on only the slot-search constructor leaves the project pass with the default, and those overlays write nothing.

## Addressing

A value under `$100` is zero page, including an expression such as `address7+1`. Do not reintroduce the expression-forces-absolute addressing rule. Forcing those expressions to absolute matched one store and broke the stores the cartridge encodes as zero page.
