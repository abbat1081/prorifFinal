print('Укажите пол допрашиваемого человека(1 - "мужчина"/ 2 - "женщина"): ')
pol = int(input())

if pol == 1:
    print("Введи текст: ")
    text = str(input())
    print(text.split())
    text1 = text.split()
    text2 = [item.replace("Я", "Он") for item in text1]
    text3 = [item.replace("я", "он") for item in text2]
    res01 = ' '.join(text3)
    res001 = res01.replace(" Ко мне" or " Ко мне." or " Ко мне " or "Ко мне ", " К нему" or " К нему." or " К нему " or "К нему ")
    res0001 = res001.replace(" ко мне" or " ко мне." or " ко мне " or "ко мне ", " к нему" or " к нему." or " к нему " or "к нему ")
    #text4 = [item.replace("Ко" and "мне", "К нему" or "К нему") for item in text3]
    #text5 = [item.replace("ко" and "мне", "к нему" or "к нему") for item in text4]
    #text6 = [item.replace("Мы", "Они") for item in text5]
    #text7 = [item.replace("мы", "они") for item in text6]
    #res = ' '.join(text7)
    print(text1)
    print(text2)
    #print(res)
    print(res0001)
elif pol == 2:
    print("Введи текст: ")
    text = split(str(input()))
    text = text.replace("Я " or " Я " or " Я." or " Я", "Она " or " Она " or " Она." or "Она")
    text = text.replace("я " or " я " or " я." or " я", "она " or " она " or " она." or "она")
    text = text.replace(" Ко мне" or " Ко мне." or " Ко мне " or "Ко мне ", " К ней" or " К ней." or " К ней " or "К ней ")
    text = text.replace(" ко мне" or " ко мне." or " ко мне " or "ко мне ", " к ней" or " к ней." or " к ней " or "к ней ")
    text = text.replace("Мы " or " Мы " or " Мы." or " Мы", "Она " or " Она " or " Она." or "Она")
    text = text.replace("мы " or " мы " or " мы." or " мы", "они " or " они " or " они." or " они")
    print(text)
else:
    print('Ошибка, неправильно указан пол (1 - "мужчина"/ 2 - "женщина")')