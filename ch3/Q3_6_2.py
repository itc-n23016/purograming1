import random

x = [chr(i) for i in range(97, 97 + 26)]
num4 = "".join(random.sample(x, k=4))
while True:
    y = input()
    if y == num4:
        break
    if len(y) != 4:
        print("input 4 x.")
        continue
    answer = ""
    for i in range(4):
        if num4[i] == y[i]:
            answer += num4[i]
        else:
            answer += "a"
        print("->" + answer)
