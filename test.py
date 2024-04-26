import re

# Исходная строка
match_info = ["2024-04-24 20:30:00+03:00 Stade Nyonnais", "Vaduz 12 @ 1.247"]

cleaned_string = re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', '', match_info[0])
print(cleaned_string.replace('  ', ''))