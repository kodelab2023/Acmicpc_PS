num = int(input())
cnt = 0

for x in range(num):
    word = input()
    wordlist = list(word)
    checklist = []
    for y in range(len(wordlist)):
        if y == 0:
            checklist.append(wordlist[y])
        elif wordlist[y] == wordlist[y-1]:
            continue
        else:
            if wordlist[y] not in checklist:
                checklist.append(wordlist[y])
            else:
                cnt+=1
                break
print(num-cnt)                        