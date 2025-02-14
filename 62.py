seconds = int(input("Введіть число: "))
dic = {'d':86400,'h':3600,'m':60}

for i in dic:
    val = seconds // dic.get(i)
    seconds %= dic.get(i)
    dic.update ({i: val})

dic_day = {
    1: "день",
    2: "дні",
    3: "дні",
    4: "дні",
    0: "днів",
    5: "днів",
    6: "днів",
    7: "днів",
    8: "днів",
    9: "днів"
}

val_day = dic_day[0] if dic["d"] % 100 in [11,12,13,14] else dic_day[dic["d"] % 10]
d,h,m,s = str(dic["d"]),str(dic["h"]).zfill(2),str(dic["m"]).zfill(2),str(seconds).zfill(2)
print (f'{d} {val_day} {h}:{m}:{s}')


