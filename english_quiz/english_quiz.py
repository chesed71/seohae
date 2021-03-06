import pandas as pd
import random 

filename = '../data/word_list.csv'
df = pd.read_csv(filename, delimiter="\t")
en_word_list = df['En']
ko_word_list = df['Ko']

for i in range(len(en_word_list)):
    en = en_word_list[i]
    answer = ko_word_list[i]
    pos_correct = random.choice(range(4))
    numbers = list(range(len(en_word_list)))
    random.shuffle(numbers)
    random_num = numbers.pop()
    
    pos_wrongs = set()
    while len(pos_wrongs) < 3:
        pos_wrong = numbers.pop()
        if pos_wrong != pos_correct:
            pos_wrongs.add(pos_wrong)

    while True:
        print("{}의 뜻으로 맞는 것은 무엇일까요?\n".format(en))
        temp_wrongs = set(pos_wrongs)
        for i in range(4):
            if i == pos_correct:
                print("{}. {}".format(i + 1, answer))
            else:
                print("{}. {}".format(i + 1, ko_word_list[temp_wrongs.pop()]))

        user_answer = input()
        if user_answer.lower() == 'q':
            exit()
        if user_answer == str(pos_correct + 1):
            print("정답입니다.\n{}\n\n".format("*" * 30))
            break
        else:
            print("틀렸습니다. 다시 시도해보세요\n\n")