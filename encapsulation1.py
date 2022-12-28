class Character:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__X0 = 0
        self.__Y0 = 0
    # блок инкапсуляции: если значение больше 100 или меньше 0, то он выводит ошибку
    def set_health(self, value):
        if value < 0 or value > 100:
            print('Ошибка')
            return 1
        else:
            self.__health = value

    def health(self):
        return self.__health

    def start_move(self, direction):
        if direction == 'w' or direction == 'W':
            self.__Y0 += 1
        elif direction == 's' or direction == 'S':
            self.__Y0 -= 1
        elif direction == 'a' or direction == 'A':
            self.__X0 -= 1
        elif direction == 'd' or direction == 'D':
            self.__X0 += 1
        else:
            print('Направление некорректно')
        if self.__X0 == 5 and self.__Y0 == 5:
            print('Вы наступили на мину, будьте аккуратнее, Ваше здоровье уменьшилось на единицу')
            self.__health -=1
        print(f'Персонаж {self.name} переместился в точку {self.__X0, self.__Y0}. Текущее здоровье {self.__health}')


def main():
    name1 = input('Введите имя вашего персонажа: ')
    person = Character(name1)
    age = int(input('Введите здоровье персонажа от 1 до 100: '))
    person.set_health(age)
    # блок проверки на правильность
    while (1 == person.set_health(age)):
        age = int(input('Введите здоровье персонажа от 1 до 100 лет: '))
    while True:
        direction = input('Введите напраление "w", "a", "s", "d" или (-) чтобы закончить: ')
        if direction == '-':
            print('by')
            break
        person.start_move(direction)


main()