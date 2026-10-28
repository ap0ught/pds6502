---
name: pds6502-nes-check
description: >-
  Judges a built .nes against a reference by the PRG after the iNES header,
  not by a same-offset score. Use when comparing a rebuilt Super Robin Hood
  or Magician ROM, reading a cart mismatch, or deciding whether the
  assembler caused a difference.
---

# Check a built .nes

The assembler writes a flat PRG. The game build wraps it in a 16-byte iNES header. Compare the PRG after the header. Compare the header only when the task is the header.

Same-offset percent is the wrong first verdict. One inserted or removed byte makes every later byte look wrong.

## What the mismatch is

Classify each difference before calling it a failure:

- Identical runs. A long match after a slip is an insertion or a deletion, not a ruined program.
- One-byte zero-page versus absolute slips. An instruction that changed size shifts every later byte.
- `$FF` or `$00` padding. An `$FF` run that also exists elsewhere is not missing code.
- Real content. Bytes that differ and do not slide back into alignment.

## Known Super Robin Hood facts

Do not fix these unless the user asks. The cart match is not byte-perfect. Record a newly found difference. Do not apply it in the same change.

- Palette: the source writes `&0E`. The cart has `$0D`. That is 39 bytes.
- Credits layout.
- `add16toval` of a negative at `lidy`: `bcc` / `inc` versus `adc #$FF`.
- One `flybackvar` `!1` collision, at `lookingathiscores`.
- The Taiwan lock is still in `START.ROU`.
- Reset vector `$C283` versus the cart `$C284`. Expressions under `$100` stay zero page. Forcing absolute was reverted.

## Diff the source first

If a second tree matches worse, diff the source before blaming the assembler.

`SuperRobinHood/original_source` `ENDCODE.ROU` still has the loop that `defs &4000,0` across banks 0–11. `master equ 1`, so the `else` of `if master=0` runs. Those downloads share mapper 71 slots with banks 12–14, so they wipe the image. `SuperRobinHoodNESSource` removed that loop.

Nine `$FF` pads in `MUSIC1.MUS`, and `zlim` / `varlim` in `VARS.PDS`, are source edits in the NES tree, not missing assembler features. The data files (`DATA3` and the PP1 blobs) are present.

## Rebuild

From `SuperRobinHoodNESSource`:

```
python3 asm/build_srh.py
```

From `magician-nes`:

```
python3 asm/build.py
```

Magician must stay byte-identical to its previous image.

From `SuperRobinHood` the same command assembles `original_source`:

```
python3 asm/build_srh.py
```

That tree still has the bank-wipe loop. A worse match there is the source.
