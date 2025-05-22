import twl

for input_word in set(twl.iterator()):
    if len(input_word) == 4:
        temp_list = list(twl.anagram(input_word))
        fin_list = []
        for temp_word in temp_list:
            if len(temp_word) == 4:
                fin_list.append(temp_word)
        counter=0
        letter_list = list(input_word)
        for fin_word in fin_list:
            if fin_word[0] in letter_list:
                letter_list.remove(fin_word[0])
                counter += 1
        if counter == 4:
            print(fin_list)