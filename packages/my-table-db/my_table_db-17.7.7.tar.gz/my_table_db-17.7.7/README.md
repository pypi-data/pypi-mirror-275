# Библиотека my_table_db

Это библиотека для вывода в консоль таблицы из базы данных
***


## Использование
### Функция my_table_db 
Принимает именованные аргументы (rows,name_arg1, name_arg2, ..., name_arg7) и их соответствующие значения (arg1, arg2, ..., arg7). Она форматирует эти входные данные в аккуратную строку с каждой парой имя-значение, разделенной символом |. Функция может обрабатывать различное количество аргументов, от одного до семи пар.

# Параметры

* name_arg1 до name_arg7: Опциональные строки, представляющие имена аргументов.
* arg1 до arg7: Опциональные значения, соответствующие каждому имени.



# Возвращаемое значение
Форматированная строка, выравнивающая предоставленные пары имя-значение в столбцы.

***
### Функция my_table_db_full
Принимает именованные аргументы (rows, colum_name). Она выводит всю таблицу в консоль с использованием оригинальных названий столбцов, значения разделены символом |.

***

# Установка

` pip install my_table_db `

## Пример 1

Содержимое таблицы
```csv
id  Name    Salary
1   Alice   50000
2   Bob     60000
```
Код с использованием my_table_db_full

```python
import psycopg2
from my_table_db import my_table_db_full

def fetch_data():
    conn = None
    try:
        conn = con = psycopg2.connect(
            dbname=...,
            user=...,
            password=...,
            host=...,
            port=...)
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees")
        
        rows = cur.fetchall()   #Получаем все строки
        colum_name = [desc[0] for desc in cur.description]  #Получаем все названия колонок
        
        my_table_db_full(rows, colum_name)  #Выводим на экран всю табличку
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print()
            print("Database connection closed.")


fetch_data()
```

#### Вывод

```shell
id:    1    | Name:    Alice    | Salary:    50000
id:    2    | Name:    Bob      | Salary:    60000

Database connection closed.
```

## Пример 2
Код с использованием my_table_db

```python
import psycopg2
from my_table_db import my_table_db

def fetch_data():
    conn = None
    try:
        conn = con = psycopg2.connect(
            dbname=...,
            user=...,
            password=...,
            host=...,
            port=...)
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees")
        
        rows = cur.fetchall()   #Получаем все строки
        for row in rows:
            my_table_db(rows,'id',row[0],'Name',row[1],'Salary',row[2])  #Выводим на экран табличку 
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print()
            print("Database connection closed.")


fetch_data()
```
```shell
id:    1    | Name:    Alice    | Salary:    50000
id:    2    | Name:    Bob      | Salary:    60000

Database connection closed.
```
### Преймущества 2 способа в том что мы можем вывести не всю табличку, а только то что хотим, а так же мы можем указать собственное имя столбца. Например мы могли написать 
```python
my_table_db(rows,'Имя',row[1],'Зарплата',row[2])
```
И в этом случае вывелось бы:

```shell
Имя:    Alice    | Зарплата:    50000
Имя:    Bob      | Зарплата:    60000
```

***

# Заключение
#### Библиотека my_table_db полезна для форматирования и отображения наборов пар имя-значение в структурированном и читаемом формате. Она может обрабатывать различное количество аргументов и гарантирует, что вывод останется выровненным и легко читаемым.

***
### Автор

Автор: k0ng999
