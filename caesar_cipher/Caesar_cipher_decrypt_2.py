####### Declaration #######
eng_alphabet_small = "abcdefghijklmnopqrstuvwxyz"
eng_alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plain_text = ""

####### Definition #######
def caesar_decrypt(cipher_text, key):
    global plain_text
    for index_num in range(0, len(cipher_text)):
        index_str = cipher_text[index_num]
        if index_str.islower() == True:
            position_num = eng_alphabet_small.index(index_str)
            replace_position_num = (position_num - key) % 26
            plain_text += eng_alphabet_small[replace_position_num]
        elif index_str.isupper() == True:
            position_num = eng_alphabet_big.index(index_str)
            replace_position_num = (position_num - key) % 26
            plain_text += eng_alphabet_big[replace_position_num]
        elif index_str.isalpha() == False:
            plain_text += index_str
    return plain_text