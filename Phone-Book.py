import sqlite3

db = sqlite3.connect('PhoneBook.db')

cursor = db.cursor()


# создание БД
# cursor.execute("""CREATE TABLE PhoneBook(
#     name VARCHAR(30),
#     number VARCHAR(30),
#     notes VARCHAR(30)
#     )""")


while True:

    # количество записей в Phone Book

    cursor.execute("""SELECT COUNT(name) FROM PhoneBook""")
    total = cursor.fetchall()

    # Всего записей в базе данных
    for i in total:
        print(f'В Phone Book {" ".join(map(str, i))} контактов')

    print('#' * 30)

    # быстрый поиск по фамилии

    user_input = input('Быстрый поиск (Y/N): ')
    if user_input == 'Y':
        name = input('Введите имя: ')
        values = [name]
        cursor.execute("""SELECT * FROM PhoneBook WHERE name == (?)""", values)
        peopl = cursor.fetchall()

        for human in peopl:
            print(" // ".join(map(str, human)))
    print('#' * 30)

    # вывод телефонной книги
    print('<<<<<<<<<<<вывод телефонной книги>>>>>>>>>>>')

    cursor.execute("""SELECT * FROM PhoneBook GROUP BY name""")
    rows = cursor.fetchall()


    # построчный вывод фамилия/номер
    for i in rows:
        print(" // ".join(map(str, i)))
    print('#' * 30)

    # добавить контакт в телефонную книгу
    user_input = input('Добавить контакт (Y/N): ')
    if user_input == 'Y':
        name = input('Введите имя: ')
        number = input('Введите номер: ')
        notes = input('Введите заметки: ')
        values = [name, number, notes]
        cursor.execute("""INSERT INTO PhoneBook (name, number, notes) VALUES(?, ?, ?)""", values)
        db.commit()

    print('#' * 30)

    # изменить телефонный номер


    user_input = input("Изменить номер (Y/N): ")
    if user_input == 'Y':
        new_number = input('Введите новый номер: ')
        name = input('Кому изменить номер: ')
        values = [new_number, name]
        cursor.execute("""UPDATE PhoneBook SET number == (?) WHERE name == (?)""", values)
        db.commit()
    print('#' * 30)

    # изменить заметки

    user_input = input("Изменить notes (Y/N): ")
    if user_input == 'Y':
        new_notes = input('Введите примечания: ')
        name = input('Кому изменить примечания: ')
        values = [new_notes, name]
        cursor.execute("""UPDATE PhoneBook SET notes == (?) WHERE name == (?)""", values)
        db.commit()
    print('#' * 30)







    # удалить контакт

    user_input = input('Удалить контакт (Y/N): ')

    if user_input == 'Y':
        name = input('Введите имя: ')
        number = input('Введите номер: ')
        values = [name, number]

        cursor.execute("""DELETE FROM PhoneBook WHERE name == (?) AND number == (?)""", values)
        db.commit()

    print('#' * 30)


    repeat = input(f'Повторить поиск по Phone Book (Y/N): ')
    if repeat == 'Y':
        continue
    else:

        print('Goodbye')
        db.close()

        break
