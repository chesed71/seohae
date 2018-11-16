import random

def shffle_number(quiz_size, max_size):    
    pos_correct = random.choice(range(quiz_size))
    
    numbers = list(range(max_size))
    random.shuffle(numbers)
    random_num = numbers.pop()
    
    pos_wrongs = set()
    while len(pos_wrongs) < quiz_size - 1:
        pos_wrong = numbers.pop()
        if pos_wrong != pos_correct:
            pos_wrongs.add(pos_wrong)
    
    # print('correct : {}, wrong : {}'.format(pos_correct, pos_wrongs))
    return pos_correct, pos_wrongs