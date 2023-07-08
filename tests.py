from main import first_unic_symbol

# Тест 1: Орієнтовний тест, данні взяти з прикладу вирішення
string = '"The Tao gave birth to machine language.  Machine language gave birth to the assembler. The assembler gave birth to the compiler.  Now there are ten thousand languages. Each language has its purpose, however humble.  Each language expresses the Yin and Yang of software.  Each language has its place within the Tao. But do not program in COBOL if you can avoid it.         -- Geoffrey James, "The Tao of Programming"'
expected_output = "m"
assert first_unic_symbol(string) == expected_output

# Тест 2: Пошук першого символу першого униікального слова
string = "C makes it easy for you to shoot yourself in the foot. C++ makes that harder, but when you do, it blows away your whole leg. (с) Bjarne Stroustrup"
expected_output = "e"
assert first_unic_symbol(string) == expected_output

# Тест 3: Перевірка роботи при відсутності унікального слова в тексті
string = "1 1"
expected_output = 'No unique symbols'
assert first_unic_symbol(string) == expected_output

# Тест 4: Перевірка роботи при символах екранування
string = "\n \n 1"
expected_output = "1"
assert first_unic_symbol(string) == expected_output

# Тест 5: Перевірка роботи при введені порожньої строки
string = ""
expected_output = "Entering an empty string"
try:
    first_unic_symbol = first_unic_symbol(string)
except ValueError as e:
    assert expected_output == str(e)

# Тест 6: Перевірка роботи при введені невідповідного типу даних
string = []
expected_output = "Input_text variable must be string type"
try:
    first_unic_symbol = first_unic_symbol(string)
except TypeError as e:
    assert expected_output == str(e)

print("Всі тести успішно пройдено!")
