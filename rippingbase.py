import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('database.db') # Указываем имя базы к которой будем выводить подключение
cursor = conn.cursor()

# Получение списка всех таблиц
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Проверка наличия таблиц и вывод данных из каждой таблицы
if tables:
    print("Список всех данных из таблиц в базе данных:")
    for table in tables:
        table_name = table[0]  # Имя текущей таблицы
        print(f"\nТаблица: {table_name}")

        # Выполнение запроса для получения всех данных из текущей таблицы
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        # Вывод всех строк из таблицы
        if rows:
            for row in rows:
                print(row)
        else:
            print("Таблица пустая.")
else:
    print("В базе данных нет таблиц.")

# Закрываем соединение
conn.close()

print("""
++--------------------------------------------------------++
++--------------------------------------------------------++
||:::::::::  :::   :::      :::    :::  ::::::::    :::   ||
||:+:    :+: :+:   :+:      :+:    :+: :+:    :+: :+:+:   ||
||+:+    +:+  +:+ +:+        +:+  +:+        +:+    +:+   ||
||+#++:++#+    +#++:          +#++:+       +#+      +#+   ||
||+#+    +#+    +#+          +#+  +#+    +#+        +#+   ||
||#+#    #+#    #+#         #+#    #+#  #+#         #+#   ||
||#########     ###         ###    ### ########## ####### ||
||                                                        ||
++------------------.db checker---------------------------++
++--------------------------------------------------------++
""")  # Выводим свой логотип!