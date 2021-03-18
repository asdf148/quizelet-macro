voca = ""

r = open("voca.txt", mode ="r", encoding="euc-kr")

for i in range(0, 70):
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

    if i == 0:
        voca = {mean: english}
    else:
        voca[mean] = english


r.close()

# for i in range(0, 70):
#     print(vocaArr[i])

# print(type(vocaArr))

print(voca["완전히"])