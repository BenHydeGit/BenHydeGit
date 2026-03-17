
def js_logic(hex_val, bits):
    val = int(hex_val, 16)
    bin_str = bin(val)[2:].zfill(bits)
    # Take the last 'bits' bits
    bin_str = bin_str[-bits:]

    if bits == 26:
        fc = int(bin_str[1:9], 2)
        cn = int(bin_str[9:25], 2)
        return fc, cn
    elif bits == 34:
        fc = int(bin_str[1:17], 2)
        cn = int(bin_str[17:33], 2)
        return fc, cn
    elif bits == 35:
        fc = int(bin_str[2:14], 2)
        cn = int(bin_str[14:34], 2)
        return fc, cn
    elif bits == 37:
        fc = int(bin_str[1:17], 2)
        cn_full = int(bin_str[1:36], 2)
        cn_part = int(bin_str[17:36], 2)
        return fc, (cn_full, cn_part)
    elif bits == 48:
        fc = int(bin_str[2:24], 2)
        cn = int(bin_str[24:47], 2)
        return fc, cn
    return None

def excel_logic(hex_val, bits):
    # Helper for Hex to Dec
    dec_val = int(hex_val, 16)
    # Truncate to bit length
    dec_val = dec_val % (2**bits)

    if bits == 26:
        fc = (dec_val // (2**17)) % 256
        cn = (dec_val // (2**1)) % 65536
        return fc, cn
    elif bits == 34:
        fc = (dec_val // (2**17)) % 65536
        cn = (dec_val // (2**1)) % 65536
        return fc, cn
    elif bits == 35:
        fc = (dec_val // (2**21)) % 4096
        cn = (dec_val // (2**1)) % 1048576
        return fc, cn
    elif bits == 37:
        fc = (dec_val // (2**20)) % 65536
        cn_full = (dec_val // (2**1)) % (2**35)
        cn_part = (dec_val // (2**1)) % (2**19)
        return fc, (cn_full, cn_part)
    elif bits == 48:
        fc = (dec_val // (2**24)) % (2**22)
        cn = (dec_val // (2**1)) % (2**23)
        return fc, cn
    return None

def test():
    test_cases = [
        ("1234567", 26),
        ("ABCDEF123", 34),
        ("76543210F", 35),
        ("1FFFFFFFFFF", 37),
        ("FFFFFFFFFFFF", 48),
        ("2000202", 26)
    ]

    for hex_val, bits in test_cases:
        js_res = js_logic(hex_val, bits)
        ex_res = excel_logic(hex_val, bits)
        print(f"Bits: {bits}, Hex: {hex_val}")
        print(f"  JS:    {js_res}")
        print(f"  Excel: {ex_res}")
        assert js_res == ex_res
        print("  MATCH!")

if __name__ == "__main__":
    test()
