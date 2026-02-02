# Card Calculator Logic Summary

Extracted from: https://www.idcubesystems.com/support/resource-center/card-calculator/

## General Logic
1. Convert Hexadecimal to Binary.
2. Pad/Truncate to the specific Bit Length (L).
3. The binary string `binValue` has length `L`.
4. Bit at index `i` (0-indexed) has weight `2^(L - 1 - i)`.
5. Extraction usually uses `binValue.substring(start, end)`, which includes indices `start` to `end-1`.

## Formats

### 26 Bit (Standard 26 Bit)
- **Facility Code**: `binValue.substring(1, 9)` (8 bits)
  - Indices: 1, 2, 3, 4, 5, 6, 7, 8
  - Powers: 2^24 to 2^17
  - Excel: `MOD(INT(DecimalValue / 2^17), 256)`
- **Card Number**: `binValue.substring(9, 25)` (16 bits)
  - Indices: 9 to 24
  - Powers: 2^16 to 2^1
  - Excel: `MOD(INT(DecimalValue / 2^1), 65536)`
- **Limits**: FC 0-255, CN 1-65535

### 34 Bit (Generic 34 Bit)
- **Facility Code**: `binValue.substring(1, 17)` (16 bits)
  - Indices: 1 to 16
  - Powers: 2^32 to 2^17
  - Excel: `MOD(INT(DecimalValue / 2^17), 65536)`
- **Card Number**: `binValue.substring(17, 33)` (16 bits)
  - Indices: 17 to 32
  - Powers: 2^16 to 2^1
  - Excel: `MOD(INT(DecimalValue / 2^1), 65536)`
- **Limits**: FC 0-65535, CN 1-65535

### 35 Bit (HID Corporate 1000 - 35 Bit)
- **Facility Code**: `binValue.substring(2, 14)` (12 bits)
  - Indices: 2 to 13
  - Powers: 2^32 to 2^21
  - Excel: `MOD(INT(DecimalValue / 2^21), 4096)`
- **Card Number**: `binValue.substring(14, 34)` (20 bits)
  - Indices: 14 to 33
  - Powers: 2^20 to 2^1
  - Excel: `MOD(INT(DecimalValue / 2^1), 1048576)`
- **Limits**: FC 0-4095, CN 1-1048575

### 37 Bit (37 Bit or 37 Bit with Facility Code)
- **Facility Code**: `binValue.substring(1, 17)` (16 bits)
  - Indices: 1 to 16
  - Powers: 2^35 to 2^20
  - Excel: `MOD(INT(DecimalValue / 2^20), 65536)`
- **Card Number**: `binValue.substring(1, 36)` (35 bits)
  - Indices: 1 to 35
  - Powers: 2^35 to 2^1
  - Excel: `MOD(INT(DecimalValue / 2^1), 34359738368)`
- **Card Number (Secondary)**: `binValue.substring(17, 36)` (19 bits)
  - Indices: 17 to 35
  - Powers: 2^19 to 2^1
  - Excel: `MOD(INT(DecimalValue / 2^1), 524288)`
- **Limits**: FC 0-65535, CN 1-34359738367 (Full) / 1-524287 (Secondary)

### 48 Bit (HID Corporate 1000 - 48 Bit)
- **Facility Code**: `binValue.substring(2, 24)` (22 bits)
  - Indices: 2 to 23
  - Powers: 2^45 to 2^24
  - Excel: `MOD(INT(DecimalValue / 2^24), 4194304)`
- **Card Number**: `binValue.substring(24, 47)` (23 bits)
  - Indices: 24 to 46
  - Powers: 2^23 to 2^1
  - Excel: `MOD(INT(DecimalValue / 2^1), 8388608)`
- **Limits**: FC 0-4194303, CN 1-8388607
