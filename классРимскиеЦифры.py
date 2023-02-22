# создаем класс для перевода араб цифр в римские

class Romanian:
    def __init__(self, num):
        self.num = num

    def inRomanian(self):
        dict = {'0': '','1': 'I','2': 'II', '3':'III','4':'IV', '5': 'V', '6': 'VI',\
                '7': 'VII', '8': 'VIII', '9': 'IX', '10': 'X'}
        if 11 > int(self.num) > 0:
            rom = dict[self.num]
            return rom
        elif 40 > int(self.num) > 10:
            num2 = 'X' * int(self.num[0])
            index_num = self.num[1]
            rom2= num2 + dict[index_num]
            return rom2
        elif 90 > int(self.num) > 59:
            num3 = 'L'
            num2 = 'X' * (int(self.num[0]) - 5)
            index_num = self.num[1]
            rom3 =  num3 + num2 + dict[index_num]
            return rom3

        else:
            message = f'This number is not true.'
            return  message

num = Romanian(input('Give me a number:'))
print(num.inRomanian())