x = "○"
y = "●"
answer = ""
for i in range(4):
    for j in range(4):
        if i == j:
            answer += x
        else:
            answer += y
    answer += "\n"
print(answer)
