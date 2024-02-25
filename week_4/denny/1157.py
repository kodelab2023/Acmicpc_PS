word = input().lower()
wordlist = list(word)
count = {}

for i in wordlist:
    try:
        count[i] += 1
    except:
        count[i] = 1

max_count = max(count.values())
max_keys = [key for key, value in count.items() if value == max_count]

if len(max_keys) > 1:
    print("?")
else:
    for key, value in count.items():
        if value == max_count:
            print(str(key).upper())
