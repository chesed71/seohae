import random

def roll(sides = 6):
    num_rolled = random.randint(1, sides)
    return num_rolled

sides = 6
rolling = True
while rolling:
    roll_again = input("주사위를 굴리세요 ENTER=굴리기. Q=종료.")
    if roll_again.lower() != "q":
        num_rolled = roll(sides)
        print("{}가 나왔습니다".format(num_rolled))
    else:
        rolling = False
print("감사합니다!")