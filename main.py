print('Укажите пол допрашиваемого человека(1 - "мужчина" / 2 - "женщина"): ')
pol = str(input())

if pol == "1":
    print("Введите ваш текст: ")
    text = str(input())
    #print(text.split())
    text1 = text.split()
    text2 = [list.replace("Я", "Он") for item in text1]
    text3 = [item.replace("я", "он") for item in text2]
    res01 = ' '.join(text3)
    text3_1 = res01.split(sep="--")
    text4 = [item.replace("Ко мне", "К нему") for item in text3_1]
    text5 = [item.replace("ко мне", "к нему") for item in text4]
    text6 = [item.replace("Мы", "Они") for item in text5]
    text7 = [item.replace("мы", "они") for item in text6]
    res = ' '.join(text7)
    print(text1)
    print(text2)
    print(text3)
    print(res01)
    print(text3_1)
    print(text4)
    print(text5)
    print(text6)
    print(text7)
    print(res)
elif pol == "2":
    print("Введите ваш текст: ")
    text = str(input())
    print(text.split())
    text1 = text.split()
    text2 = [item.replace("Я", "Она") for item in text1]
    text3 = [item.replace("я", "она") for item in text2]
    res01 = ' '.join(text3)
    text3_1 = res01.split(sep="--")
    text4 = [item.replace("Ко мне", "К ней") for item in text3_1]
    text5 = [item.replace("ко мне", "к ней") for item in text4]
    text6 = [item.replace("Мы", "Они") for item in text5]
    text7 = [item.replace("мы", "они") for item in text6]
    res = ' '.join(text7)
    print(text1)
    print(text2)
    print(res)
else:
    print('Ошибка, неправильно указан пол (1 - "мужчина"/ 2 - "женщина")')