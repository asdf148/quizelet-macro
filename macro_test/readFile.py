import sys

# sys.stdout = open("voca.txt", mode ="rt", encoding="euc-kr")

vocaArr = []
voca = []

r = open("voca.txt", mode ="r", encoding="euc-kr")


# word = r.readline()
# point = r.tell()
# print(word)
# r.close()

# print(word)



for i in range(0, 10):
    word = r.readline()
    print(word.split()[1])
    word = r.readline()
    print(word.split()[1])
    word = r.readline()

    voca.append(english.split()[1])
    voca.append(mean.split()[1])

    vocaArr.append(voca)
    voca = []

r.close()

# r = open("voca.txt", mode ="rt", encoding="euc-kr")
# word = r.readline()
# r.close()
# print(word)

# sys.stdout.readline()
# sys.stdout.close()
# print(english)


# sys.stdout = open("voca.txt", mode ="rt", encoding="euc-kr")
# mean = sys.stdout.readline()
# sys.stdout.close()
# print(mean)

# sys.stdout.close()