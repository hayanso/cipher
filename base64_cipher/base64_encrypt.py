base_64_symbol = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def asc2bin(plain_text):
    ascii_list = []
    total_bin = ""
    binary_txt = ""
    for i in range(len(plain_text)):
        ascii_list.append(ord(plain_text[i]))
    for i in ascii_list:
        while True:
            div = i // 2
            mod = i % 2
            i = div
            binary_txt += str(mod)
            if div == 0:
                break
        total_bin += ("0" + binary_txt[::-1])
        binary_txt = ""
    return total_bin

def base64_encrypt(plain_text):
    l1 = []
    total = ""
    return_value = asc2bin(plain_text)
    while len(return_value) % 6 != 0:
        return_value += "0"
    index_bin = [return_value[i:i+6] for i in range(0, len(return_value), 6)]
    for i in index_bin:
        dec = 0
        pow_num = 0
        i = list(str(i))
        i = i[::-1]
        for bin_num in i:
            if bin_num == "1":
                dec += 2**pow_num
            pow_num += 1
        l1.append(dec)
    for num in l1:
        total += base_64_symbol[num]
    if len(total) % 4 == 2:
        total += "=="
    elif len(total) % 4 == 3:
        total += "="

    return total