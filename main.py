import time
import sys
import json
import csv
import os


def tri():
    time.sleep(2)


def igra():
     print(
         'Цель: выжить за Джека, если вы потеряли одного из друзей, то игра продолжится\nСамое главное, чтобы Вы были живы, но если вы потеряли свой облик, то это будет считаться, как поражение')
     tri()
     hi = "Приветствую"
     ga = "милой"
     go = "Вас"
     lol = "игре ^.^"
     privet = (f"{hi} {go} в своей {ga} {lol}")
     print(privet)
     tri()
     people = ["Джек", "Лучезар", "Тихон"]
     monsters = {"призрак", "вурдалак", "зомби"}
     inventar = {"оружие": "топор", "тип оружия": "ближнее", "сложность": "зависит от человека"}
     pred = "немного о персонажах"
     print(pred.upper())
     tri()
     print(
         'Имя: Джек\tИмя: Лучезар\tИмя: Тихон\nВозраст: 16\tВозраст: 16\t Возраст: 16\nХобби: дотa\tХобби: Футбол\t Хобби: Гонки')
     tri()
     invent = 'Вы имеете небольшой инвентарь: топор'
     print(invent)
     tri()
     print('Вы закончили 9 класс, сдали успешно все экзамены и решили после такого триумфа отдохнуть')
     tri()
     print('Вы коллективно решили снять дом для отдыха на несколько дней')
     tri()
     print('Вы зашли в дом...')
     tri()
     while True:
        try:
            deistvie = int(input('Осмотреться?\n1. Самому\n2. Попросить Лучезара\n'))
        except ValueError:
            continue
        if deistvie == 1:
            print('Огромный дом, всего 3 этажа, но комнат бесчисленное множество')
            tri()
            print(
                'Вы решили походить по дому и нактнулись на одну интересную комнату с кучей мебели и там был довольно красивый шкаф...')
            tri()
            while True:
                try:
                    deistvie2 = int(input('открыть?\n1. Да\n2. Нет\n'))
                except ValueError:
                    continue
                if deistvie2 == 1:
                    print('Там куча белья и резко одно из них начинает шевелиться...')
                    tri()
                    while True:
                        try:
                            deistvie3 = int(input(
                                'Это призрак, попытаться убежать или всё же как-то сразиться с ним?\n1. Убежать\n2. Сразиться\n'))
                        except ValueError:
                            continue
                        if deistvie3 == 1:
                            print(
                                'Вы успешно убежали, но заблудились в доме и пытаетесь до кричаться до друзей, но на крик появляется вовсе не ваш друг...')
                            tri()
                            print('Вурдалак с голодом смотрит на вас, но бежать варианта нет')
                            tri()
                            while True:
                                try:
                                    deistvie4 = int(input(
                                        'Попытаться сразиться, ведь в инвентаре имеется топор\n1.Да \n2.Принять свою судьбу такой, какая она есть\n'))
                                except ValueError:
                                    continue
                                if deistvie4 == 1:
                                    print('Вы обезглавили вурдалака, но нервишки шалят и вы теряете сознание')
                                    tri()
                                    print(
                                        'Вы просыпаетесь окутанные пледом, а рядом ваши друзья, вы спрашиваете как они тебя нашли. Они высмеяли вас и сказали, что вы псих и никаких вурдалаков не было')
                                    tri()
                                    while True:
                                        try:
                                            deistvie5 = int(input('Сойти с ума?\n1. Да \n2. Нет\n'))
                                        except ValueError:
                                            continue
                                        if deistvie5 == 1:
                                            print(
                                                'Вы решаете, что так продолжаться не может и решаете уехать в психбольницу, к слову, это поражение, но стоит отметить, что оно довольно приятное')
                                            while True:
                                                try:
                                                    vybor1 = int(input(
                                                        'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                                except ValueError:
                                                    continue
                                                if vybor1 == 1:
                                                    data = read_data_from_csv('data.csv')
                                                    write_data_to_csv('data.csv', data)
                                                    save_name = input('Введите название сохранения: ')
                                                    sohr = {
                                                        'Выжившие персонажи': 'Лучезар, Тихон, Джек',
                                                        'Выбранные действия': '1,1,1,1,1'
                                                    }
                                                    with open(f'{save_name}.json', 'w') as file:
                                                        json.dump(sohr, file)
                                                        data = [
                                                            ['Выжившие персонажи', 'Лучезар, Тихон, Джек'],
                                                            ['Выбранные действия', '1,1,1,1,1']
                                                        ]
                                                        with open('output.csv,', 'w', newline='') as file:
                                                            writer = csv.writer(file)
                                                            for row in data:
                                                                writer.writerow(row)
                                                        menu()
                                                if vybor1 == 2:
                                                    menu()
                                        if deistvie5 == 2:
                                            print('Вы пошли к тому месту и там действительно было пусто...')
                                            tri()
                                            print(
                                                'Вы теряете реальность и не понимаете что к чему, но вдруг раздаются громкие крики')
                                            tri()
                                            while True:
                                                try:
                                                    deistvie6 = int(input(
                                                        'Сходить посмотреть?\n1.Конечно\n2. Они вам не друзья, есть только дота\n'))
                                                except ValueError:
                                                    continue
                                                if deistvie6 == 1:
                                                    print(
                                                        'Вы видите очень неприятную картину: зомби доедает Лучезара, Тихона рядом нет')
                                                    tri()
                                                    print(
                                                        'Вы замечаете, что Тихон уже был трапезой данного персонажа и надо пытаться себя спасти')
                                                    tri()
                                                    while True:
                                                        try:
                                                            deistvie7 = int(input(
                                                                'Сделать рагу из зомби?\n1. Да\n2. Нет \n3. Не знаю\n '))
                                                        except ValueError:
                                                            continue
                                                        if deistvie7 == 1:
                                                            print(
                                                                'Зомби больше нет, но соответсвенно и врагов тоже, ЭТО ПОБЕДА!!!!! Но с неприятным привкусом, друзей-то больше нет или они не друзья...')
                                                            while True:
                                                                try:
                                                                    vybor2 = int(input(
                                                                        'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                                                except ValueError:
                                                                    continue
                                                                if vybor2 == 1:
                                                                    data = read_data_from_csv('data.csv')
                                                                    write_data_to_csv('data.csv', data)
                                                                    save_name = input('Введите название сохранения: ')
                                                                    sohr = {
                                                                        'Выжившие персонажи': 'Джек',
                                                                        'Выбранные действия': '1,1,1,1,2,1,1'
                                                                    }
                                                                    with open(f'{save_name}.json', 'w') as file:
                                                                        json.dump(sohr, file)
                                                                        data = [
                                                                            ['Выжившие персонажи',
                                                                             'Джек'],
                                                                            ['Выбранные действия', '1,1,1,1,2,1,1']
                                                                        ]
                                                                        with open('output.csv,', 'w',
                                                                                  newline='') as file:
                                                                            writer = csv.writer(file)
                                                                            for row in data:
                                                                                writer.writerow(row)
                                                                        menu()
                                                                if vybor2 == 2:
                                                                    menu()
                                                        if deistvie7 == 2:
                                                            print('Зомби увидело вас и начало бежать')
                                                            tri()
                                                            print('Кроме как достать топор вариантов нет или есть...')
                                                            tri()
                                                            while True:
                                                                try:
                                                                    deistvie8 = int(input(
                                                                        'Быстро закончить разговор с зомби?\n1. Да\n2. Уже в целом не так и грустно\n'))
                                                                except ValueError:
                                                                    continue
                                                                if deistvie8 == 1:
                                                                    print(
                                                                        'Вот незадача, зомби-то оказался сильнее) Это было печальное зрелище...')
                                                                    while True:
                                                                        try:
                                                                            vybor3 = int(input(
                                                                                'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                                                        except ValueError:
                                                                            continue
                                                                        if vybor3 == 1:
                                                                            data = read_data_from_csv('data.csv')
                                                                            write_data_to_csv('data.csv', data)
                                                                            save_name = input(
                                                                                'Введите название сохранения: ')
                                                                            sohr = {
                                                                                'Выжившие персонажи': 'Отсутствуют',
                                                                                'Выбранные действия': '1,1,1,1,2,1,2,1'
                                                                            }
                                                                            with open(f'{save_name}.json', 'w') as file:
                                                                                json.dump(sohr, file)
                                                                                data = [
                                                                                    ['Выжившие персонажи',
                                                                                     'Отсутствуют'],
                                                                                    ['Выбранные действия', '1,1,1,1,2,1,2,1']
                                                                                ]
                                                                                with open('output.csv,', 'w',
                                                                                          newline='') as file:
                                                                                    writer = csv.writer(file)
                                                                                    for row in data:
                                                                                        writer.writerow(row)
                                                                                menu()
                                                                        if vybor3 == 2:
                                                                            menu()
                                                                if deistvie8 == 2:
                                                                    print(
                                                                        'Исход понятен, поражение, но это не повод грустить, ведь друзья тоже проиграли ха-ха-ха')
                                                                    while True:
                                                                        try:
                                                                            vybor4 = int(input(
                                                                                'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                                                        except ValueError:
                                                                            continue
                                                                        if vybor4 == 1:
                                                                            data = read_data_from_csv('data.csv')
                                                                            write_data_to_csv('data.csv', data)
                                                                            save_name = input(
                                                                                'Введите название сохранения: ')
                                                                            sohr = {
                                                                                'Выжившие персонажи': 'Отсутствуют',
                                                                                'Выбранные действия': '1,1,1,1,2,1,2,2'
                                                                            }
                                                                            with open(f'{save_name}.json', 'w') as file:
                                                                                json.dump(sohr, file)
                                                                                data = [
                                                                                    ['Выжившие персонажи',
                                                                                     'Отсутствуют'],
                                                                                    ['Выбранные действия', '1,1,1,1,2,1,2,2']
                                                                                ]
                                                                                with open('output.csv,', 'w',
                                                                                          newline='') as file:
                                                                                    writer = csv.writer(file)
                                                                                    for row in data:
                                                                                        writer.writerow(row)
                                                                                menu()
                                                                        if vybor4 == 2:
                                                                            menu()
                                                        if deistvie7 == 3:
                                                            print('Думать времени нет, зомби увидел вас')
                                                            tri()
                                                            print('Кроме как достать топор вариантов нет или есть...')
                                                            tri()
                                                            while True:
                                                                try:
                                                                    deistvie9 = int(
                                                                        input('Попытаться его убить?\n1. Да\n2. Нет\n'))
                                                                except ValueError:
                                                                    continue
                                                                if deistvie9 == 1:
                                                                    print(
                                                                        'Зомби оказался умнее вас и легко вас убил...))')
                                                                    while True:
                                                                        try:
                                                                            vybor5 = int(input(
                                                                                'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                                                        except ValueError:
                                                                            continue
                                                                        if vybor5 == 1:
                                                                            data = read_data_from_csv('data.csv')
                                                                            write_data_to_csv('data.csv', data)
                                                                            save_name = input(
                                                                                'Введите название сохранения: ')
                                                                            sohr = {
                                                                                'Выжившие персонажи': 'Отсутствуют',
                                                                                'Выбранные действия': '1,1,1,1,2,1,2,3',
                                                                                'Выбранные действия2': '1'
                                                                            }
                                                                            with open(f'{save_name}.json', 'w') as file:
                                                                                json.dump(sohr, file)
                                                                                data = [
                                                                                    ['Выжившие персонажи',
                                                                                     'Отсутствуют'],
                                                                                    ['Выбранные действия', '1,1,1,1,2,1,2,3'],
                                                                                    ['Выбранные действия2,','1']
                                                                                ]
                                                                                with open('output.csv,', 'w',
                                                                                          newline='') as file:
                                                                                    writer = csv.writer(file)
                                                                                    for row in data:
                                                                                        writer.writerow(row)
                                                                                menu()
                                                                        if vybor5 == 2:
                                                                            menu()
                                                                if deistvie9 == 2:
                                                                    print(
                                                                        'Зомби сделал из вас зимние заготовки, будет что кушать бедному')
                                                                    while True:
                                                                        try:
                                                                            vybor6 = int(input(
                                                                                'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                                                        except ValueError:
                                                                            continue
                                                                        if vybor6 == 1:
                                                                            data = read_data_from_csv('data.csv')
                                                                            write_data_to_csv('data.csv', data)
                                                                            save_name = input(
                                                                                'Введите название сохранения: ')
                                                                            sohr = {
                                                                                'Выжившие персонажи': 'Отсутствуют',
                                                                                'Выбранные действия': '1,1,1,1,2,1,2,3',
                                                                                'Выбранные действия2': '2'
                                                                            }
                                                                            with open(f'{save_name}.json', 'w') as file:
                                                                                json.dump(sohr, file)
                                                                                data = [
                                                                                    ['Выжившие персонажи',
                                                                                     'Отсутствуют'],
                                                                                    ['Выбранные действия', '1,1,1,1,2,1,2,3'],
                                                                                    ['Выбранные действия2', '2']
                                                                                ]
                                                                                with open('output.csv,', 'w',
                                                                                          newline='') as file:
                                                                                    writer = csv.writer(file)
                                                                                    for row in data:
                                                                                        writer.writerow(row)
                                                                                menu()
                                                                        if vybor6 == 2:
                                                                            menu()
                                                if deistvie6 == 2:
                                                    print('Вы  решили пойти на третий этаж, невзирая на крики')
                                                    tri()
                                                    print('Вы поднялись на третий этаж...')
                                                    tri()
                                                    print('Там была одна комната и одно окно...')
                                                    tri()
                                                    print('Также было множество различных вещей')
                                                    tri()
                                                    print('Кроме этого там был сундук, который был приоткрыт')
                                                    tri()
                                                    while True:
                                                        try:
                                                            deistvie10 = int(input('Открыть?\n1. Да\n2. Нет\n'))
                                                        except ValueError:
                                                            continue
                                                        if deistvie10 == 1:
                                                            print('В сундуке ничего интересного не было')
                                                            tri()
                                                            print('Вы развернулись и решили пойти к выходу')
                                                            tri()
                                                            print('Вы спустились вниз...')
                                                            tri()
                                                            print(
                                                                'Вдали коридора вы увидели медленно идущего к Вам зомби')
                                                            tri()
                                                            print('Бежать вам по большому счёту некуда')
                                                            tri()
                                                            print(
                                                                'Вам остаётся лишь только достать топор и убить зомби')
                                                            tri()
                                                            print('Вам удалось его убить и теперь вы убегаете из дома')
                                                            tri()
                                                            print('Вы выбежали из дома и у вас начинается истерика')
                                                            tri()
                                                            print('Вы теряете рассудок и начинаете свою жизнь в лесу')
                                                            tri()
                                                            print('Теперь вы дотер-отшельник и Вам это нравится')
                                                            while True:
                                                                try:
                                                                    vybor7 = int(input(
                                                                        'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                                                except ValueError:
                                                                    continue
                                                                if vybor7 == 1:
                                                                    data = read_data_from_csv('data.csv')
                                                                    write_data_to_csv('data.csv', data)
                                                                    save_name = input(
                                                                        'Введите название сохранения: ')
                                                                    sohr = {
                                                                        'Выжившие персонажи': 'Отсутствуют',
                                                                        'Выбранные действия': '1,1,1,1,2,1,2,3',
                                                                        'Выбранные действия2': '1'
                                                                    }
                                                                    with open(f'{save_name}.json', 'w') as file:
                                                                        json.dump(sohr, file)
                                                                        data = [
                                                                            ['Выжившие персонажи',
                                                                             'Отсутствуют'],
                                                                            ['Выбранные действия', '1,1,1,1,2,1,2,3'],
                                                                            ['Выбранные действия2', '1']
                                                                        ]
                                                                        with open('output.csv,', 'w',
                                                                                  newline='') as file:
                                                                            writer = csv.writer(file)
                                                                            for row in data:
                                                                                writer.writerow(row)
                                                                        menu()
                                                                if vybor7 == 2:
                                                                    menu()
                                                        if deistvie10 == 2:
                                                            while True:
                                                                try:
                                                                    deistvie11 = int(
                                                                        input('Вернуться?\n1. Да\n2. Нет\n'))
                                                                except ValueError:
                                                                    continue
                                                                if deistvie11 == 1:
                                                                    print('Вы увидели как зомби вошёл в одну из комнат')
                                                                    tri()
                                                                    print('Вы тихо спускаетесь на первый этаж')
                                                                    tri()
                                                                    print(
                                                                        'Вы убегаете из дома, быстро забрав свои вещи')
                                                                    tri()
                                                                    print("Вы успешно сбежали, это победа ^.^")
                                                                    while True:
                                                                        try:
                                                                            vybor8 = int(input(
                                                                                'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                                                        except ValueError:
                                                                            continue
                                                                        if vybor8 == 1:
                                                                            data = read_data_from_csv('data.csv')
                                                                            write_data_to_csv('data.csv', data)
                                                                            save_name = input(
                                                                                'Введите название сохранения: ')
                                                                            sohr = {
                                                                                'Выжившие персонажи': 'Джек',
                                                                                'Выбранные действия': '1,1,1,1,2,1,2,3',
                                                                                'Выбранные действия2': '1'
                                                                            }
                                                                            with open(f'{save_name}.json', 'w') as file:
                                                                                json.dump(sohr, file)
                                                                                data = [
                                                                                    ['Выжившие персонажи',
                                                                                     'Джек'],
                                                                                    ['Выбранные действия', '1,1,1,1,2,1,2,3'],
                                                                                    ['Выбранные действия2','1']
                                                                                ]
                                                                                with open('output.csv,', 'w',
                                                                                          newline='') as file:
                                                                                    writer = csv.writer(file)
                                                                                    for row in data:
                                                                                        writer.writerow(row)
                                                                                menu()
                                                                        if vybor8 == 2:
                                                                            menu()
                                if deistvie4 == 2:
                                    print('Вы понравились на вкус вурдалаку, но это всё же поражение((((')
                                    while True:
                                        try:
                                            vybor9 = int(input(
                                                'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                        except ValueError:
                                            continue
                                        if vybor9 == 1:
                                            data = read_data_from_csv('data.csv')
                                            write_data_to_csv('data.csv', data)
                                            save_name = input(
                                                'Введите название сохранения: ')
                                            sohr = {
                                                'Выжившие персонажи': 'Тихон, Лучезар',
                                                'Выбранные действия': '1,1,1,2'
                                            }
                                            with open(f'{save_name}.json', 'w') as file:
                                                json.dump(sohr, file)
                                                data = [
                                                    ['Выжившие персонажи', 'Тихон, Лучезар'],
                                                    ['Выбранные действия', '1,1,1,2']
                                                ]
                                                with open('output.csv,', 'w', newline='') as file:
                                                    writer = csv.writer(file)
                                                    for row in data:
                                                        writer.writerow(row)
                                                menu()
                                        if vybor9 == 2:
                                            menu()
                        if deistvie3 == 2:
                            print('В этой неравной схватке вы проиграли и были убиты...')
                            tri()
                            print('Но не стоит грустить, ваши друзья стали обедом для вурдалака и зомби \u263A')
                            while True:
                                try:
                                    vybor10 = int(input(
                                        'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                except ValueError:
                                    continue
                                if vybor10 == 1:
                                    data = read_data_from_csv('data.csv')
                                    write_data_to_csv('data.csv', data)
                                    save_name = input(
                                        'Введите название сохранения: ')
                                    sohr = {
                                        'Выжившие персонажи': 'Отсутствуют',
                                        'Выбранные действия': '1,1,2',
                                    }
                                    with open(f'{save_name}.json', 'w') as file:
                                        json.dump(sohr, file)
                                        data = [
                                            ['Выжившие персонажи', 'Отсутствуют'],
                                            ['Выбранные действия', '1,1,2']
                                        ]
                                        with open('output.csv,', 'w', newline='') as file:
                                            writer = csv.writer(file)
                                            for row in data:
                                                writer.writerow(row)
                                        menu()
                                if vybor10 == 2:
                                    menu()
                if deistvie2 == 2:
                    print('Вы продолжаете осматриваться и замечаете движение штор')
                    tri()
                    print('Вы натыкаетесь на призрака')
                    tri()
                    while True:
                        try:
                            deistvie12 = int(input('Сразиться?\n1. Да\n2. Нет\n'))
                        except ValueError:
                            continue
                        if deistvie12 == 1:
                            print('Вы оказались слабее призрака(')
                            while True:
                                try:
                                    vybor11 = int(input(
                                        'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                except ValueError:
                                    continue
                                if vybor11 == 1:
                                    data = read_data_from_csv('data.csv')
                                    write_data_to_csv('data.csv', data)
                                    save_name = input(
                                        'Введите название сохранения: ')
                                    sohr = {
                                        'Выжившие персонажи': 'Лучезар, Тихон',
                                        'Выбранные действия': '1,2,1',
                                    }
                                    with open(f'{save_name}.json', 'w') as file:
                                        json.dump(sohr, file)
                                        data = [
                                            ['Выжившие персонажи', 'Лучезар, Тихон'],
                                            ['Выбранные действия', '1,2,1']
                                        ]
                                        with open('output.csv,', 'w', newline='') as file:
                                            writer = csv.writer(file)
                                            for row in data:
                                                writer.writerow(row)
                                        menu()
                                if vybor11 == 2:
                                    menu()
                        if deistvie12 == 2:
                            print('призрак повеселился над вами')
                            while True:
                                try:
                                    vybor12 = int(input(
                                        'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                except ValueError:
                                    continue
                                if vybor12 == 1:
                                    data = read_data_from_csv('data.csv')
                                    write_data_to_csv('data.csv', data)
                                    save_name = input(
                                        'Введите название сохранения: ')
                                    sohr = {
                                        'Выжившие персонажи': 'Лучезар, Тихон',
                                        'Выбранные действия': '1,2,2',
                                    }
                                    with open(f'{save_name}.json', 'w') as file:
                                        json.dump(sohr, file)
                                        data = [
                                            ['Выжившие персонажи', 'Лучезар, Тихон'],
                                            ['Выбранные действия', '1,2,2']
                                        ]
                                        with open('output.csv,', 'w', newline='') as file:
                                            writer = csv.writer(file)
                                            for row in data:
                                                writer.writerow(row)
                                        menu()
                                if vybor12 == 2:
                                    menu()
        if deistvie == 2:
            print('Лучезар растворился в таком огромном доме')
            tri()
            print('Лучезар не откликается на крики')
            tri()
            while True:
                try:
                    deistvie13 = int(input('Кто сходит посмотреть, Вы или Тихон?\n1.Вы\n2. Тихон\n'))
                except ValueError:
                    continue
                if deistvie13 == 1:
                    print('Вы нашли Лучезара, но он был неподвижен')
                    tri()
                    print('Вы спросили что с ним, но он бледный и молчит')
                    print(
                        'Вы взяли его за руку и тут резко стало темно и свет загорелся на кровати, а там вурдалак, который рад видеть вас обоих')
                    tri()
                    while True:
                        try:
                            deistvie14 = int(
                                input('Что делать??\n1. Отдать Лучезара ему и убежать\n2. Устроить битву\n'))
                        except ValueError:
                            continue
                        if deistvie14 == 1:
                            print('Вы успешно убежали, но поступили крайне ужасно и вас начинает грызть совесть')
                            tri()
                            print('Вы решаете сознаться в сделанном Тихону, но он не одобрил и началась драка')
                            tri()
                            while True:
                                try:
                                    deistvie15 = int(input('Достать топор?\n1. Да\n2. Решить вопрос честно\n'))
                                except ValueError:
                                    continue
                                if deistvie15 == 1:
                                    print('Вы легко порешали Тихона, но чувствуете резкую боль в голове и падаете')
                                    tri()
                                    print(
                                        'Вы просыпаетесь в какой-то комнате, смотрите на руки, а они не человеческие, вы стали одним из вурдалаков этого дома. Добрый вурдалак предложил вам покушать Лучезара и запить пивом')
                                    tri()
                                    while True:
                                        try:
                                            deistvie16 = int(input('Согласиться?\n1. Да\n2. Нет\n'))
                                        except ValueError:
                                            continue
                                        if deistvie16 == 1:
                                            print(
                                                'Это был прекрасный пир, но по факту это поражение из-за утраты человеческого облика, но дотер-вурдалак звучит прикольно')
                                            while True:
                                                try:
                                                    vybor13 = int(input(
                                                        'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                                except ValueError:
                                                    continue
                                                if vybor13 == 1:
                                                    data = read_data_from_csv('data.csv')
                                                    write_data_to_csv('data.csv', data)
                                                    save_name = input(
                                                        'Введите название сохранения: ')
                                                    sohr = {
                                                        'Выжившие персонажи': 'Джек не в своем обличии',
                                                        'Выбранные действия': '2,1,1,1,1',
                                                    }
                                                    with open(f'{save_name}.json', 'w') as file:
                                                        json.dump(sohr, file)
                                                        data = [
                                                            ['Выжившие персонажи', 'Джек не в своем обличии'],
                                                            ['Выбранные действия', '2,1,1,1,1']
                                                        ]
                                                        with open('output.csv,', 'w', newline='') as file:
                                                            writer = csv.writer(file)
                                                            for row in data:
                                                                writer.writerow(row)
                                                        menu()
                                                if vybor13 == 2:
                                                    menu()
                                        if deistvie16 == 2:
                                            print('Вы стали вурдалаком-изгоем(((')
                                            while True:
                                                try:
                                                    vybor14 = int(input(
                                                        'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                                except ValueError:
                                                    continue
                                                if vybor14 == 1:
                                                    data = read_data_from_csv('data.csv')
                                                    write_data_to_csv('data.csv', data)
                                                    save_name = input(
                                                        'Введите название сохранения: ')
                                                    sohr = {
                                                        'Выжившие персонажи': 'Джек-вурдалак-изгой',
                                                        'Выбранные действия': '2,1,1,1,2'
                                                    }
                                                    with open(f'{save_name}.json', 'w') as file:
                                                        json.dump(sohr, file)
                                                        data = [
                                                            ['Выжившие персонажи', 'Джек-вурдалак-изгой'],
                                                            ['Выбранные действия', '2,1,1,1,2']
                                                        ]
                                                        with open('output.csv,', 'w', newline='') as file:
                                                            writer = csv.writer(file)
                                                            for row in data:
                                                                writer.writerow(row)
                                                        menu()
                                                if vybor14 == 2:
                                                    menu()
                                if deistvie15 == 2:
                                    print('Вы проиграли и были задушены Тихоном')
                                    while True:
                                        try:
                                            vybor15 = int(input(
                                                'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                        except ValueError:
                                            continue
                                        if vybor15 == 1:
                                            data = read_data_from_csv('data.csv')
                                            write_data_to_csv('data.csv', data)
                                            save_name = input(
                                                'Введите название сохранения: ')
                                            sohr = {
                                                'Выжившие персонажи': 'Тихон',
                                                'Выбранные действия': '2,1,1,1,2'
                                            }
                                            with open(f'{save_name}.json', 'w') as file:
                                                json.dump(sohr, file)
                                                data = [
                                                    ['Выжившие персонажи', 'Тихон'],
                                                    ['Выбранные действия', '2,1,1,1,2']
                                                ]
                                                with open('output.csv,', 'w', newline='') as file:
                                                    writer = csv.writer(file)
                                                    for row in data:
                                                        writer.writerow(row)
                                                menu()
                                        if vybor15 == 2:
                                            menu()
                        if deistvie14 == 2:
                            print('Вы успешно смогли обезглавить сие чудище, Лучезар резко ожил')
                            tri()
                            print('Вы спросили как его самочувствие, но ответа не последовало')
                            tri()
                            print('Вы посмотрели в его лицо, а его глаза чёрные')
                            tri()
                            print('Резко Лучезар взял вас за руку и начал орать')
                            tri()
                            print('Вы попытались вырваться')
                            tri()
                            print('Лучезар тянется ртом к вашей руке')
                            tri()
                            while True:
                                try:
                                    deistvie17 = int(input('Ударить Лучезара кулаком?\n1. Да\n2. Нет\n'))
                                except ValueError:
                                    continue
                                if deistvie17 == 1:
                                    print('Ничего толком не произошло')
                                    tri()
                                    print('Лучезар кусает вас.....')
                                    tri()
                                    print('Вы теряете сознание')
                                    tri()
                                    print('Вы очнулись, но вы продолжили лежать в этой комнате')
                                    tri()
                                    print('Вы смотрите на руки, а они серые...')
                                    tri()
                                    print('Вы вампир, поздравляю!!!!!!!!')
                                    while True:
                                        try:
                                            vybor16 = int(input(
                                                'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                        except ValueError:
                                            continue
                                        if vybor16 == 1:
                                            data = read_data_from_csv('data.csv')
                                            write_data_to_csv('data.csv', data)
                                            save_name = input(
                                                'Введите название сохранения: ')
                                            sohr = {
                                                'Выжившие персонажи': 'Тихон, вампир-Лучезар, вампир-Джек',
                                                'Выбранные действия': '2,1,2,1',
                                            }
                                            with open(f'{save_name}.json', 'w') as file:
                                                json.dump(sohr, file)
                                                data = [
                                                    ['Выжившие персонажи', 'Тихон, вампир-Лучезар, вампир-Джек'],
                                                    ['Выбранные действия', '2,1,2,1']
                                                ]
                                                with open('output.csv,', 'w', newline='') as file:
                                                    writer = csv.writer(file)
                                                    for row in data:
                                                        writer.writerow(row)
                                                menu()
                                        if vybor16 == 2:
                                            menu()
                                if deistvie17 == 2:
                                    print('Лучезар впивается клыками в Вашу кожу')
                                    tri()
                                    print('Лучезар выпил Вашу кровь')
                                    tri()
                                    print('Вы погибли от значительной потери крови, досадно конечно')
                                    while True:
                                        try:
                                            vybor17 = int(input(
                                                'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                        except ValueError:
                                            continue
                                        if vybor17 == 1:
                                            data = read_data_from_csv('data.csv')
                                            write_data_to_csv('data.csv', data)
                                            save_name = input(
                                                'Введите название сохранения: ')
                                            sohr = {
                                                'Выжившие персонажи': 'Тихон, вампир-Лучезар',
                                                'Выбранные действия': '2,1,2,2',
                                            }
                                            with open(f'{save_name}.json', 'w') as file:
                                                json.dump(sohr, file)
                                                data = [
                                                    ['Выжившие персонажи', 'Тихон, вампир-Лучезар'],
                                                    ['Выбранные действия', '2,1,2,2']
                                                ]
                                                with open('output.csv,', 'w', newline='') as file:
                                                    writer = csv.writer(file)
                                                    for row in data:
                                                        writer.writerow(row)
                                                menu()
                                        if vybor17 == 2:
                                            menu()
                if deistvie13 == 2:
                    print('Вам становится холодно')
                    tri()
                    while True:
                        try:
                            deistvie18 = int(input('Попытаться согреться?\n1. Да\n'))
                        except ValueError:
                            continue
                        if deistvie18 == 1:
                            print('Да, на улице лето')
                            tri()
                            print('Холодно стало из-за свойств дома')
                            tri()
                            print('Вы замерзли окончательно')
                            while True:
                                try:
                                    vybor18 = int(input(
                                        'Выберите действие:\n1. Сохраниться\n2. Не сохраняться\n'))
                                except ValueError:
                                    continue
                                if vybor18 == 1:
                                    data = read_data_from_csv('data.csv')
                                    write_data_to_csv('data.csv', data)
                                    save_name = input(
                                        'Введите название сохранения: ')
                                    sohr = {
                                        'Выжившие персонажи': 'Отсутствуют',
                                        'Выбранные действия': '2,2,1',
                                    }
                                    with open(f'{save_name}.json', 'w') as file:
                                        json.dump(sohr, file)
                                    data = [
                                        ['Выжившие персонажи', 'Отсутствуют'],
                                        ['Выбранные действия','2,2,1']
                                    ]
                                    with open ('output.csv,','w', newline='') as file:
                                        writer = csv.writer(file)
                                        for row in data:
                                            writer.writerow(row)
                                        menu()
                                if vybor18 == 2:
                                    menu()


def prosmotr_json():
    print("Для просмотра введите название json файла")
    filename = input("Введите название json файла: ")
    try:
        with open(filename) as json_file:
            sohr = json.load(json_file)
            print(sohr)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")


def view_json_file():
    print("Чтобы вы смогли просмотреть JSON файл вам надо ввесли - название сохранения.json")
    filename = input("Введите название JSON файла: ")
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            print(data)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")

def delete_save():
    print("Чтобы удалить сохранение вам достаточно написать его название")
    save_name = input("Введите название сохранения для удаления: ")
    try:
        os.remove(f"{save_name}.json")
        print(f"Сохранение '{save_name}' удалено.")
    except FileNotFoundError:
        print(f"Сохранение '{save_name}' не найдено.")

def load_save(save_name):
    try:
        with open(f"{save_name}.json", "r") as file:
            game_data = json.load(file)
            print(f"Сохранение '{save_name}' успешно загружено.")
    except FileNotFoundError:
        print(f"Сохранение '{save_name}' не найдено.")

def read_data_from_csv(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def write_data_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def menu():
    while True:
        try:
            deistivee = int(input('Главное меню\n1. Играть\n2. Загрузить игру\n3. Выйти из игры\n'))
        except ValueError:
            continue
        if deistivee == 1:
            igra()
        if deistivee == 2:
            while True:
                try:
                    deistviee = int(input(
                        '1. Загрузить сохранение\n2, Удалить сохранение\n3. Просмотр сохранения\n4. Вернуться в меню\n'))
                except ValueError:
                    continue
                if deistviee == 1:
                    save_name = input('Введите название сохранения: ')
                    load_save(save_name)
                if deistviee == 2:
                    delete_save()
                if deistivee == 3:
                    view_json_file()
                if deistviee == 4:
                    menu()
        if deistivee == 3:
            sys.exit()
menu()

