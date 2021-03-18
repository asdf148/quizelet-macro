r = open("voca.txt", mode ="r", encoding="euc-kr")

# english = sys.stdout.readline()
# print(english)
# mean = sys.stdout.readline()
# print(mean)

# sys.stdout.close()

vocaArr = []
voca = []

for i in range(0, 69):
    r.read(4)
    english = r.readline()

    length = len(english)-2
    english = english[:length]
    english = english[1:]

    r.read(3)
    mean = r.readline()

    length = len(mean)-2
    mean = mean[:length]
    mean = mean[2:]

    r.readline()

    voca.append(english)
    voca.append(mean)

    vocaArr.append(voca)
    voca = []

r.close()

# for i in range(0, 69):
#     print(vocaArr[i])

print(vocaArr)

print(vocaArr[0][0])