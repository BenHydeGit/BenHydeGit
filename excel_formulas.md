# Card Calculator Excel Implementation

This guide provides the formulas to replicate the IDCUBE Card Calculator functionality in Excel.

## 1. Sheet Setup

Set up your Excel sheet with the following columns:

- **A2**: Hex Input (e.g., `1234567`)
- **B2**: Bit Length (Choose from: 26, 34, 35, 37, 48)
- **C2**: Decimal Value (Helper Formula)
- **D2**: Format Name
- **E2**: Facility Code
- **F2**: Card Number
- **G2**: Facility Code Limit
- **H2**: Card Number Limit

---

## 2. Formulas

### Decimal Value (Helper) - Cell C2
This formula converts the Hex input to a Decimal number, handling up to 48 bits (12 hex characters).
```excel
=IF(LEN(A2)<=8, HEX2DEC(A2), HEX2DEC(RIGHT(A2,8)) + HEX2DEC(LEFT(A2,LEN(A2)-8))*4294967296)
```

### Format Name - Cell D2
```excel
=SWITCH(B2, 26, "Standard 26 Bit", 34, "Generic 34 Bit", 35, "HID Corporate 1000 (35 Bit)", 37, "37 Bit (or 37 Bit with Facility Code)", 48, "HID Corporate 1000 (48 Bit)", "Invalid Bit Length")
```

### Facility Code - Cell E2
```excel
=SWITCH(B2,
  26, MOD(INT(C2/131072), 256),
  34, MOD(INT(C2/131072), 65536),
  35, MOD(INT(C2/2097152), 4096),
  37, "None (" & MOD(INT(C2/1048576), 65536) & ")",
  48, MOD(INT(C2/16777216), 4194304),
  "N/A"
)
```

### Card Number - Cell F2
```excel
=SWITCH(B2,
  26, MOD(INT(C2/2), 65536),
  34, MOD(INT(C2/2), 65536),
  35, MOD(INT(C2/2), 1048576),
  37, MOD(INT(C2/2), 34359738368) & " (" & MOD(INT(C2/2), 524288) & ")",
  48, MOD(INT(C2/2), 8388608),
  "N/A"
)
```

### Facility Code Limit - Cell G2
```excel
=SWITCH(B2, 26, "0 ~ 255", 34, "0 ~ 65535", 35, "0 ~ 4095", 37, "None (0 ~ 65535)", 48, "0 ~ 4194303", "")
```

### Card Number Limit - Cell H2
```excel
=SWITCH(B2, 26, "1 ~ 65535", 34, "1 ~ 65535", 35, "1 ~ 1048575", 37, "1 ~ 34359738367 (1 ~ 524287)", 48, "1 ~ 8388607", "")
```

---

## 3. Explanation of Constants
- `2^1 = 2`
- `2^17 = 131072`
- `2^19 = 524288`
- `2^20 = 1048576`
- `2^21 = 2097152`
- `2^24 = 16777216`
- `2^32 = 4294967296`
- `2^35 = 34359738368`
