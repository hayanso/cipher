####### Declaration #######
eng_alphabet_small = "abcdefghijklmnopqrstuvwxyz"
eng_alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plain_text = ""
out_come_dic = {}

####### Definition #######
def caesar_decrypt(cipher_text):
    global plain_text
    for shift_num in range(26):
        for index_num in range(0, len(cipher_text)):
            index_str = cipher_text[index_num]
            if index_str.islower() == True:
                position_num = eng_alphabet_small.index(index_str)
                replace_position_num = (position_num - shift_num) % 26
                plain_text += eng_alphabet_small[replace_position_num]
            elif index_str.isupper() == True:
                position_num = eng_alphabet_big.index(index_str)
                replace_position_num = (position_num - shift_num) % 26
                plain_text += eng_alphabet_big[replace_position_num]
            elif index_str.isalpha() == False:
                plain_text += index_str
        out_come_dic[shift_num] = plain_text
        plain_text = ""
        
    return out_come_dic