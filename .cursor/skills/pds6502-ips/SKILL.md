---
name: pds6502-ips
description: >-
  Writes an IPS v1 patch that turns a reference .nes into a built ROM, and
  applies it back to check. Use when creating an IPS, a cart patch, or a
  byte patch between two NES images.
---

# IPS patch of one NES ROM

The patch turns the reference cart into the built ROM. Applying it to the reference yields the built file. The other direction is a different patch.

Patch the whole `.nes` files, header included, so every offset is a file offset. Both files must be the same kind of image. A raw PRG against a file that still has a header shifts every record by 16.

## IPSv1

The file starts with ASCII `PATCH` and ends with ASCII `EOF`.

Each record is a 3-byte big-endian offset, a 2-byte big-endian length, then that many data bytes. Length 0 means RLE: the next 2 bytes are the big-endian count, and the next byte is the fill value.

```
PATCH
00 00 10   offset 16
00 03      three bytes
0E 0E 0E
45 4F 46   EOF
```

Offset `0x454F46` is the bytes `EOF`. A record must not start there. If a run would start at that offset, start one byte earlier and include the preceding byte. Offsets are 24-bit. Refuse a file longer than 16 MiB, or a difference at or past `0x1000000`.

IPS cannot truncate. If the built ROM is shorter than the reference, warn and stop. The applied file would keep the extra tail.

## Write it

Walk both files. Emit one record for each maximal run of differing bytes. Split a run longer than 65535. Use RLE when every byte in the record is the same and the RLE record is smaller: a literal record is 5 + N bytes, an RLE record is 8, so RLE wins at 4 or more repeated bytes.

```python
EOF_OFF = 0x454F46

def ips_patch(reference: bytes, built: bytes) -> bytes:
    """IPS that turns the reference cart into the built ROM."""
    if len(built) < len(reference):
        raise ValueError("IPS cannot truncate; built ROM is shorter")
    if len(built) > 0x1000000:
        raise ValueError("IPSv1 offsets are 24-bit; refusing past 16 MiB")
    out = bytearray(b"PATCH")
    i = 0
    while i < len(built):
        old = reference[i] if i < len(reference) else None
        if old == built[i]:
            i += 1
            continue
        start = i
        i += 1
        while i < len(built) and (
            i >= len(reference) or reference[i] != built[i]
        ):
            i += 1
        if start == EOF_OFF:
            start -= 1
        emit_run(out, start, built[start:i])
    out += b"EOF"
    return bytes(out)

def emit_run(out: bytearray, start: int, data: bytes) -> None:
    pos = 0
    while pos < len(data):
        off = start + pos
        take = min(65535, len(data) - pos)
        if off + take == EOF_OFF and pos + take < len(data):
            take -= 1
        if off > 0xFFFFFF or off == EOF_OFF or take < 1:
            raise ValueError(f"bad IPS offset {off:#x}")
        chunk = data[pos:pos + take]
        if take >= 4 and chunk == bytes([chunk[0]]) * take:
            out += off.to_bytes(3, "big")
            out += b"\x00\x00"
            out += take.to_bytes(2, "big")
            out.append(chunk[0])
        else:
            out += off.to_bytes(3, "big")
            out += take.to_bytes(2, "big")
            out += chunk
        pos += take
```

## Check it

Apply the patch to the reference. The result must be identical to the built ROM.

```python
def apply_ips(reference: bytes, patch: bytes) -> bytes:
    if not patch.startswith(b"PATCH"):
        raise ValueError("missing PATCH")
    out = bytearray(reference)
    i = 5
    while patch[i:i + 3] != b"EOF":
        off = int.from_bytes(patch[i:i + 3], "big")
        ln = int.from_bytes(patch[i + 3:i + 5], "big")
        i += 5
        if ln == 0:
            count = int.from_bytes(patch[i:i + 2], "big")
            data = bytes([patch[i + 2]]) * count
            i += 3
        else:
            data = patch[i:i + ln]
            i += ln
        end = off + len(data)
        if end > len(out):
            out.extend(b"\x00" * (end - len(out)))
        out[off:end] = data
    return bytes(out)

# apply_ips(reference, ips_patch(reference, built)) == built
```
