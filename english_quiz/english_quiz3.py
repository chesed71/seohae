import file_handler

from shuffler import shffle_number

fileHandler = file_handler.FileHandler()

class QuizMaker:
    def __init__(self, filename):
        self.en_word_list, self.ko_word_list = fileHandler.readFile(filename)
        self.list_size = len(self.en_word_list)

    def showQuiz(self):
        for i in range(self.list_size):
            en = self.en_word_list[i]
            answer = self.ko_word_list[i]
            
            pos_correct, pos_wrongs = shffle_number(4, self.list_size)
            
            while True :
                print("{}의 뜻으로 맞는 것은 무엇일까요?".format(en))
                temp_wrongs = set(pos_wrongs)
                for i in range(4):
                    if i == pos_correct:
                        print("{}. {}".format(i + 1, answer))
                    else:
                        print("{}. {}".format(i + 1, self.ko_word_list[temp_wrongs.pop()]))

                user_answer = input()
                if user_answer.lower() == 'q':
                    exit()
                if user_answer == str(pos_correct + 1):
                    print("정답입니다.\n{}\n\n".format("*" * 30))
                    break
                else:
                    print("틀렸습니다. 다시 시도해보세요\n\n")


if __name__ == "__main__":
    quiz_maker = QuizMaker('../data/word_list.csv')
    quiz_maker.showQuiz()