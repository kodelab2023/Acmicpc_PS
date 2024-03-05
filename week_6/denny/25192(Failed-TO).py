num = int(input())
cnt = 0
wordlist = []
checklist = []

for x in range(num):
    word = input()
    wordlist.append(word)

for y in range(len(wordlist)):
    if wordlist[y] == 'ENTER':
        checklist = []
        for z in range(y+1, len(wordlist)):
            if wordlist[z] != 'ENTER' and wordlist[z] not in checklist:
                cnt += 1
                checklist.append(wordlist[z])
print(cnt)
