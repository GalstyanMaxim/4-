import re

vowels = set('аеёиоуыэюя')
file_name = "poem.txt"
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        poem = file.read()
except FileNotFoundError:
    print(f"Файл {file_name} не найден.")
    poem = ""


print("Стихотворение:")
print(poem)


words = re.findall(r'\b\w+\b', poem.lower())  # Слова, игнорируя пунктуацию
vowel_start = 0
consonant_start = 0

for word in words:
    if word and word[0] in vowels:
        vowel_start += 1
    elif word:
        consonant_start += 1

if vowel_start > consonant_start:
    print("Больше слов, начинающихся на гласную.")
elif consonant_start > vowel_start:
    print("Больше слов, начинающихся на согласную.")
else:
    print("Количество слов, начинающихся на гласную и согласную, равно.")
print(f"На гласную: {vowel_start}, на согласную: {consonant_start}")