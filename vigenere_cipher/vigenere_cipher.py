eng_alphabet_small = "abcdefghijklmnopqrstuvwxyz"
eng_alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_text = ""
index_key_l1 = []

def vignere_encript(plain_text, key):
    global index_key_l1
    global cipher_text
    for index_key_num in range(0, len(key)):
        index_key = key[index_key_num]
        if index_key.isupper() == True:
            index_key_num = eng_alphabet_big.index(index_key)
            index_key_l1.append(index_key_num)
        elif index_key.islower() == True:
            index_key_num = eng_alphabet_small.index(index_key)
            index_key_l1.append(index_key_num)
        elif index_key.isalpha() == False:
            index_key_l1.append(index_key)
    print(index_key_l1)
    a = 0
    for index_num in range(0, len(plain_text)):
        index_str = plain_text[index_num]
        if a == 3:
            a = 0
        if index_str.islower() == True:
            position_num = eng_alphabet_small.index(index_str)
            replace_position_num = (position_num + index_key_l1[a]) % 26
            cipher_text += eng_alphabet_small[replace_position_num]
        elif index_str.isupper() == True:
            position_num = eng_alphabet_big.index(index_str)
            replace_position_num = (position_num + index_key_l1[a]) % 26
            cipher_text += eng_alphabet_big[replace_position_num]
            a += 1
        elif index_str.isalpha() == False:
            cipher_text += index_str
            a += 1
    return cipher_text
print(vignere_encript("divert troops to east ridge", "sky"))