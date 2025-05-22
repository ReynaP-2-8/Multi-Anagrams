import twl

word_length = int(input("Number of Letters: "))
for input_word in set(twl.iterator()):
    if len(input_word) == word_length:
        temp_list = list(twl.anagram(input_word))
        fin_list = []
        for temp_word in temp_list:
            if len(temp_word) == word_length:
                fin_list.append(temp_word)
        counter = 0
        letter_list = list(input_word)
        for fin_word in fin_list:
            if fin_word[0] in letter_list:
                letter_list.remove(fin_word[0])
                counter += 1
        if counter == word_length:
            print(fin_list)
