# 2. Давайте представим, что мы занимаемся проектированием CRM для сервисного центра по обслуживанию и ремонту техники.
# Реализуйте класс Заявка. Каждая заявка должна иметь следующие поля: уникальный идентификатор (присваивается в момент)
# создания заявки автоматически, дата и время создания заявки (автоматически), имя пользователя, серийный номер
# оборудования, статус (активная заявка или закрытая например, статусов может быть больше). Id заявки сделать приватным
# полем.
# У заявки должны быть следующие методы:
# - метод, возвращающий, сколько заявка находится в активном статусе (если она в нём)
# - метод, изменяющий статус заявки
# - метод, возвращающий id заявки
# import datetime
from datetime import datetime
import uuid


class Ticket:
    __all_status = ["active", "new", "in progress"]

    def __init__(self, user_name, serial):
        self.name = user_name
        self.serial = serial
        self.date = datetime.now()
        self.__id = uuid.uuid4()
        self.status = "active"
        print(f"Доброго времени суток {self.name}, заявка создана под номером - {self.__id}")

    def time_hold(self):
        if self.status == "active":
            date1 = datetime.now() - self.date
            res = f"Время сколько заявка находится в активном статусе - {date1}"
            return res
        return "Заявка еще не была взята в работу."

    def change_status(self, new_status):
        if new_status in Ticket.__all_status:
            if self.status == new_status:
                return f"Нельзя изменить так как статус уже - {new_status}"
            self.status = new_status
            return f"Статус изменен на - {new_status}"
        else:
            return f"Неверный статус, заявка в статусе {self.status}"

    def get_id(self):
        return f"Номер заявки - {self.__id}"


tickets1 = Ticket("Сергей", "sdf")
print(tickets1.time_hold())
print(tickets1.get_id())
print(tickets1.change_status("new"))
print(tickets1.change_status("ne1w"))
