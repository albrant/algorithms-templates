def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

k = 0
for x in range(1000):
    oct_num = convert_base(x, 8)
    hex_num = convert_base(x, 16)
    if len(oct_num) == 3 and len(hex_num) == 3 and hex_num[0:2] == '1D' and oct_num[1] == '3':
        k += 1
        print(x,  oct_num, hex_num, k)
