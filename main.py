print('Введите кол-во сотрудников')

# Ввод количества сотрудников, цикл закончится тогда, когда пользователь введёт ЦЕЛОЕ число
while True:
    try:
        peoples = int(input())

    except ValueError as e:
        print("Введите число, а не текст!")

    else:
        break

summ = 0
index = 0

# Ввод переменных
v = list(range(peoples))

# Ввод всех дистанций, цикл закончится когда пользователь введёт ряд ЦЕЛЫХ чисел через ПРОБЕЛ
while True:
    try:
        raw_text = list(map(int, input('Введите все дистанции\n').split()))
        distances = [{
            "index": s + 1,
            "value": raw_text[s]
        } for s in range(len(raw_text))]
        distances1 = sorted(distances, key=lambda x: x['value'], reverse=True)

    except ValueError as e:
        print("Введите число, а не текст!")

    else:
        break

# Ввод тарифов, цикл закончится когда пользователь введёт ряд ЦЕЛЫХ чисел через ПРОБЕЛ
while True:
    try:
        raw_text = list(map(int, input('Введите все тарифы такси за 1 километр\n').split()))
        tariffs = [{
            "index": s + 1,
            "value": raw_text[s]
        } for s in range(len(raw_text))]
        tariffs1 = sorted(tariffs, key=lambda x: x['value'])

    except ValueError as e:
        print("Введите число, а не текст!")

    else:
        break

a = len(tariffs1)
b = len(distances1)

if a != peoples and b != peoples:
    print('Кол-во введёных тарифов и дистанций не соотвествует кол-ву введёных сотрудников')
    exit()

if a != peoples:
    print('Кол-во введёных тарифов не соотвествует кол-ву введёных сотрудников')
    exit()

if b != peoples:
    print('Кол-во введёных дистанций не соотвествует кол-ву введёных сотрудников')
    exit()

results = [
    {
        "s_id": distances1[i]['index'],
        "t_id": tariffs1[i]['index'],
        "cost": tariffs1[i]['value'] * distances1[i]['value']
    } for i in range(peoples)
]
kalka = "{t_id} - номер такси для {s_id}"

# Вывод результатов
print("\n".join(list(map(lambda i: kalka.format(**i), results))))
summ = sum(map(lambda x: x['cost'], results))
print(summ)
n = summ

# Вывод суммы словами
if n > 999999 or n < 1:
    print('Число не входит в заданный диапазон')
if ((n // 100000) % 10) == 1:
    print('сто ', end='')
if ((n // 100000) % 10) == 2:
    print('двести ', end='')
if ((n // 100000) % 10) == 3:
    print('триста ', end='')
if ((n // 100000) % 10) == 4:
    print('четыреста ', end='')
if ((n // 100000) % 10) == 5:
    print('пятьсот ', end='')
if ((n // 100000) % 10) == 6:
    print('шестьсот ', end='')
if ((n // 100000) % 10) == 7:
    print('семьсот ', end='')
if ((n // 100000) % 10) == 8:
    print('восемьсот ', end='')
if ((n // 100000) % 10) == 9:
    print('девятьсот ', end='')
if ((n // 10000) % 10 == 1):
    if (n // 1000 % 10) == 0:
        print('десять тысяч ', end='')
    if (n // 1000 % 10) == 1:
        print('одинадцать тысяч ', end='')
    if (n // 1000 % 10) == 2:
        print('двенадцать тысяч ', end='')
    if (n // 1000 % 10) == 3:
        print('тринадцать тысяч ', end='')
    if (n // 1000 % 10) == 4:
        print('четырнадцать тысяч ', end='')
    if (n // 1000 % 10) == 5:
        print('пятьнадцать тысяч ', end='')
    if (n // 1000 % 10) == 6:
        print('шестнадцать тысяч ', end='')
    if (n // 1000 % 10) == 7:
        print('семьнадцать тысяч ', end='')
    if (n // 1000 % 10) == 8:
        print('восемьнадцать тысяч ', end='')
    if (n // 1000 % 10) == 9:
        print('девятьнадцать тысяч ', end='')
if ((n//10000) % 10) == 2:
    print('двадцать ', end='')
if ((n//10000) % 10) == 3:
    print('тридцать ', end='')
if ((n//10000) % 10) == 4:
    print('сорок ', end='')
if ((n//10000) % 10) == 5:
    print('пятьдесят ', end='')
if ((n//10000) % 10) == 6:
    print('шестьдесят ', end='')
if ((n//10000) % 10) == 7:
    print('семьдесят ', end='')
if ((n//10000) % 10) == 8:
    print('восемьдесят ', end='')
if ((n//10000) % 10) == 9:
    print('девяноста ', end='')
if ((n//10000) % 10 != 1) and len(str(n)) >= 4:
    if (n//1000) % 10 == 0:
        print('тысяч ', end='')
    if (n//1000) % 10 == 1:
        print('одна тысяча ', end='')
    if (n//1000) % 10 == 2:
        print('две тысячи ', end='')
    if (n//1000) % 10 == 3:
        print('три тысячи ', end='')
    if (n//1000) % 10 == 4:
        print('четыре тысячи ', end='')
    if (n//1000) % 10 == 5:
        print('пять тысяч ', end='')
    if (n//1000) % 10 == 6:
        print('шесть тысяч ', end='')
    if (n//1000) % 10 == 7:
        print('семь тысяч ', end='')
    if (n//1000) % 10 == 8:
        print('восемь тысяч ', end='')
    if (n//1000) % 10 == 9:
        print('девять тысяч ', end='')
if (n//100) % 10 == 1:
    print('сто ', end='')
if (n//100) % 10 == 2:
    print('двести ', end='')
if (n//100) % 10 == 3:
    print('триста ', end='')
if (n//100) % 10 == 4:
    print('четыреста ', end='')
if (n//100) % 10 == 5:
    print('пятьсот ', end='')
if (n//100) % 10 == 6:
    print('шестьсот ', end='')
if (n//100) % 10 == 7:
    print('семьсот ', end='')
if (n//100) % 10 == 8:
    print('восемьсот ', end='')
if (n//100) % 10 == 9:
    print('девятьсот ', end='')
if ((n//10) % 10 == 1):
    if n % 10 == 0:
        print('десять рублей ', end='')
    if n % 10 == 1:
        print('одинадцать рублей ', end='')
    if n % 10 == 2:
        print('двенадцать рублей ', end='')
    if n % 10 == 3:
        print('тринадцать рублей ', end='')
    if n % 10 == 4:
        print('четырнадцать рублей ', end='')
    if n % 10 == 5:
        print('пятьнадцать рублей ', end='')
    if n % 10 == 6:
        print('шестнадцать рублей ', end='')
    if n % 10 == 7:
        print('семьнадцать рублей ', end='')
    if n % 10 == 8:
        print('восемьнадцать рублей ', end='')
    if n % 10 == 9:
        print('девятьнадцать рублей ', end='')
if (n//10) % 10 == 2:
    print('двадцать ', end='')
if (n//10) % 10 == 3:
    print('тридцать ', end='')
if (n//10) % 10 == 4:
    print('сорок ', end='')
if (n//10) % 10 == 5:
    print('пятьдесят ', end='')
if (n//10) % 10 == 6:
    print('шестдесят ', end='')
if (n//10) % 10 == 7:
    print('семьдесят ', end='')
if (n//10) % 10 == 8:
    print('восемьдесят ', end='')
if (n//10) % 10 == 9:
    print('девяносто ', end='')
if ((n//10) % 10) != 1:
    if n % 10 == 0:
        print('рублей', end='')
    if n % 10 == 1:
        print('один рубль', end='')
    if n % 10 == 2:
        print('два рубля', end='')
    if n % 10 == 3:
        print('три рубля', end='')
    if n % 10 == 4:
        print('четыре рубля', end='')
    if n % 10 == 5:
        print('пять рублей', end='')
    if n % 10 == 6:
        print('шесть рублей', end='')
    if n % 10 == 7:
        print('семь рублей', end='')
    if n % 10 == 8:
        print('восемь рублей', end='')
    if n % 10 == 9:
        print('девять рублей', end='')
