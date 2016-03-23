# Vid Drobnič
# Gimnazija Vič, 3.b
# Intermediate 3
# Language: Python 3.5.1

char_split = input().split(" ")
i = int(char_split[1])
while i < len(char_split[0]):
    char_split[0] = char_split[0][:i] + char_split[2] + char_split[0][i:]
    i += int(char_split[1]) + 1
print(char_split[0])

strrem = input().split()
print(strrem[0].replace(strrem[1], ""))

strchr = input().split()
index = strchr[0].find(strchr[1])
if index == -1:
    print(strchr[0])
else:
    print(strchr[0][:index])

strtok = input().split()
i = 0
while i < len(strtok[0]):
    if strtok[0][i] == strtok[1]:
        strtok[0] = strtok[0][:i] + " " + strtok[0][i:]
        i += 1
    i += 1
print(strtok[0])

wordwrap = input().split()
i = 0
j = 0
while i < len(wordwrap[0]):
    if wordwrap[0][i] == wordwrap[2] or j == int(wordwrap[1]):
        wordwrap[0] = wordwrap[0][:i] + " " + wordwrap[0][i:]
        i += 1
        j = 0
    i += 1
    j += 1
print(wordwrap[0])
