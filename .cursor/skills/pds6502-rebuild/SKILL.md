---
name: pds6502-rebuild
description: >-
  Rebuilds Super Robin Hood and Magician with the shared PDS 6502 assembler
  and judges the result. Use when changing pds6502.py, a game's asm/pds6502.py
  loader, asm/build_srh.py, or Magician asm/build.py.
---

# Rebuild both games

Clone this repo next to the games. Each game's `asm/pds6502.py` is a loader. It imports `pds6502.py` from `PDS6502_HOME` or from the sibling checkout `../pds6502`. Each game keeps its own build script. Super Robin Hood is mapper 71 with 16 KiB banks. Magician is MMC3 with 8 KiB slots. Do not point one game's build at the other source.

From `SuperRobinHoodNESSource`:

```
python3 asm/build_srh.py
```

From `magician-nes`:

```
python3 asm/build.py
```

Run both after an assembler change. Magician takes about half a minute.

## What success means

Magician must stay byte-identical to its previous assembler output. The PRG comparison is the check. A symbol-count change with a matching PRG is still a failure until the missing name is explained. `loop` in `X0.PDS` is a column-0 label (`loop bne loop` on the same logical line as `cli`). Indenting it makes the word the `do`/`loop` directive and drops the symbol.

Super Robin Hood's cart match is not byte-perfect. Do not "fix" palette `$0E` versus `$0D`, the credits layout, or the reset vector unless the user asks. The source writes `&0e`. The reset vector stays one byte low because zero-page addressing was kept. Record a newly found cart difference. Do not apply it in the same change.
