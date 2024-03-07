import sys
input = sys.stdin.readline
result = 0

word = input().rstrip()
wordlist = list(word)
rev_wordlist = list(reversed(wordlist))

if wordlist == rev_wordlist:
    result = 1
else:
    result = 0        
print(result)                            