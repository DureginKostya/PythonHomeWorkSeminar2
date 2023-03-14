'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3'''
try:
    sumNumbers = int(input('Введите сумму двух натуральных чисел: '))
    multiplicationNumbers = int(input('Введите произведение двух натуральных чисел: '))
    if sumNumbers < 0 or multiplicationNumbers < 0:
        print('Введено отрицательное(-ые) значение(-ия)')
    else:
        discriminant = sumNumbers ** 2 - 4 * multiplicationNumbers
        if discriminant >= 0:
            if discriminant == 0:
                numberFirst = sumNumbers / 2
                numberSecond = sumNumbers - numberFirst
            else:
                numberFirst = (sumNumbers - discriminant ** 0.5) / 2
                numberSecond = (sumNumbers + discriminant ** 0.5) / 2
            if numberFirst == int(numberFirst) and numberSecond == int(numberSecond):
                print(f'Загаданы натуральные числа: {int(numberFirst)} и {int(numberSecond)}')       
            else:
                print(f'Нет натуральных чисел, которые бы отвечали условию задачи') 
        else:
            print(f'Задача не имеет решения')
except:
    print('Введено не допустимое значение')