import random


class Casino:
    slots = [i for i in range(0, 37)]

    def __init__(self):
        self.__money = 1000

    @property
    def money(self):
        return self.__money

    def lose(self, amount):
        print(f'Вы проиграли {amount}$')
        self.__money -= amount

    def win(self, amount):
        print(f'Вы выиграли {amount}$')
        self.__money += amount

    def check(self, slot: str, amount: str):
        if slot == 'красное' or slot == 'черное':
            return True
        if slot.isnumeric():
            if 0 <= int(slot) <= 36:
                return True
        if amount.isnumeric():
            if 0 <= int(amount) <= self.money:
                return True
        return False

    def stavka(self, slot: str, amount: int):
        win_slot = random.choice(self.slots)
        if slot.isnumeric():
            slot = int(slot)
            if slot == win_slot:
                if slot == 0:
                    self.win(amount*10)
                else:
                    self.win(amount * 5)
            else:
                self.lose(amount)
        else:
            if slot == 'красное' and win_slot % 2 == 1:
                self.win(int(amount * 1.5))
            elif slot == 'черное' and win_slot % 2 == 0:
                self.win(int(amount * 1.5))
            else:
                self.lose(amount)


casino = Casino()
while True:
    command = input('Введите комманду q-выход s-поставить ставку: ')
    if command == 'q':
        print('Пока')
        break
    elif command == 's':
        slot = input('Введите слот ставки (красное, черное, число от 0 до 36): ')
        amount = input('Введите сумму ставки: ')
        if casino.check(slot.lower(), amount):
            casino.stavka(slot.lower(), int(amount))
        else:
            print('Неправильно сделана ставка!')
    else:
        print('Wrong command')
