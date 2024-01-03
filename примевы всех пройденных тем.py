# урок1: Переменные 
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

name = input("Введите ваше имя: ")
print("Привет,", name)

# урок2: Списки и их метод, Кортежи и их методы
p = [ ]
p = [ 5 ] 
p = [ 1, 4.12]

my_tuple = (1, 2, 3, 2, 4)
index_3 = my_tuple.index(3)
print(index_3)  

# урок3: Циклы While и For
word = "Python"
for letter in word:
    print(letter)

is_running = True
while is_running:
    user_input = input("Введите 'exit' для выхода: ")
    if user_input.lower() == 'exit':
        is_running = False
    else:
        print(f"Вы ввели: {user_input}")

# урок4: Как работать со списками, используя циклы (for и While)
numbers = [1, 2, 3, 4, 5]

index = 0
while True:
    print(numbers[index])
    index += 1
    if index >= len(numbers):
        break


numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# урок5:List comprehension
squares = [x**2 for x in range(10)]
print(squares)



words = ['apple', 'banana', 'cherry']
word_lengths = [len(word) for word in words]
print(word_lengths)

# урок6: Методы применяемые со словарями
my_dict = dict()

keys = ['name', 'age', 'city']
default_value = 'unknown'
person = dict.fromkeys(keys, default_value)

user_info = {'name': 'John', 'age': 30}
additional_info = {'city': 'New York', 'gender': 'Male'}
user_info.update(additional_info)

# урок7: Функции (Functions)
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print(sum_result)  

# урок8: lambda, args и kwargs

a = lambda x:x**2
print(a(10))    

b = lambda y,u:y+u
print(b(2,3))

def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, "apple", True) 

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=25, city="Wonderland")

# урок9: метод class
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

my_dog = Dog()
my_cat = Cat()

my_dog.speak()  
my_cat.speak()  

# урок10: Наследование (Inheritance)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

my_dog.speak() 
my_cat.speak()  

# урок11: Sqlite3
import sqlite3


conn = sqlite3.connect('example.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')


cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 25))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 30))


conn.commit()

conn.close()

# урок12: telegram bot
import telebot
from telebot.types import ReplyKeyboardRemove
from buttons import kb

# Создать объект бота
bot = telebot.TeleBot('6769812309:AAHQDL4OkscI00iAYluWwKX_Blu0E-duC-Y')


# Обработка команды start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'Приветствую! Добро пожаловать в мой первый бот)',
                     reply_markup=kb)


# Обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def text_message(message):
    user_id = message.from_user.id

    if message.text.lower() == 'википедия':
        bot.send_message(user_id, 'Введите слово', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, wiki)
    elif message.text.lower() == 'переводчик':
        bot.send_message(user_id, 'Введите слово для перевода', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, tran)
    else:
        bot.send_message(user_id, 'Неизвестная операция')

def wiki(message):
    user_id = message.from_user.id

    if message.text.lower() == 'райан гослинг':
        bot.send_message(user_id, 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%81%D0%BB%D0%B8%D0%BD%D0%B3,_%D0%A0%D0%B0%D0%B9%D0%B0%D0%BD')
        bot.send_message(user_id, 'Готово, что еще?', reply_markup=kb)
        bot.register_next_step_handler(message, text_message)
    else:
        bot.send_message(user_id, 'Неизвестная операция')
        bot.register_next_step_handler(message, wiki)


def tran(message):
    user_id = message.from_user.id

    if message.text.lower() == 'hello':
        bot.send_message(user_id,
                         'Привет')
        bot.send_message(user_id, 'Готово, что еще?', reply_markup=kb)
        bot.register_next_step_handler(message, text_message)
    else:
        bot.send_message(user_id, 'Неизвестная операция')
        bot.register_next_step_handler(message, tran)

        
# Запуск бота
bot.polling(non_stop=True)






