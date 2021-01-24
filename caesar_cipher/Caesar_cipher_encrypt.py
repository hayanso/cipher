####### Declaration #######
eng_alphabet_small = "abcdefghijklmnopqrstuvwxyz"
eng_alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_text = ""

####### Definition #######
def caesar_encrypt(plain_text, shift_num):
    global cipher_text
    for index_num in range(len(plain_text)):
        index_str = plain_text[index_num]
        if index_str.islower() == True:
            position_num = eng_alphabet_small.index(index_str)
            replace_position_num = (position_num + shift_num) % 26
            cipher_text += eng_alphabet_small[replace_position_num]
        elif index_str.isupper() == True:
            position_num = eng_alphabet_big.index(index_str)
            replace_position_num = (position_num + shift_num) % 26
            cipher_text += eng_alphabet_big[replace_position_num]
        elif index_str.isalpha() == False:
            cipher_text += index_str
            
    return cipher_text