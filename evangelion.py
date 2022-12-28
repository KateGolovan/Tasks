class roman():
    def __init__(self, model, name, action):
        self.model = model
        self.name = name
        self.action = action
    def __str__(self):
        return self.model +' '+  self.name + '' +self.action


def main():
    # создаю три экземпляра класса романа
    first = roman('00', 'Раскольников', ', раскол - раздвоение, кого-то любит, а кому-то не повезло')
    second = roman('1', 'Процентщица', ', символ никчёмности, но тоже человек')
    third  = roman('2', 'София', ', несёт крест, верит в добро и справедливость')
    # словарь с ключами, провожу сортировку
    spisok = {1: first, 2: second, 3: third}
    for i,j in spisok.items():
        print('модель романа: ' + j.__str__() )

main()
