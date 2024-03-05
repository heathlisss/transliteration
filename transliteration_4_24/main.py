# --------------------------------------------------------------------------------------------------------------
# Реализовать программу транслитерации текста на русском языке английскими символами
# --------------------------------------------------------------------------------------------------------

translit_table = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ь': '', 'ы': 'y', 'ъ': 'ie', 'э': 'e', 'ю': 'iu', 'я': 'ia'
}


def transliterate(text):
    result = ''
    for char in text:
        if char.lower() in translit_table:
            result += translit_table[char.lower()]
        else:
            result += char
    return result


def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        return text


def write_to_file(text, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


input_file_name = "test1.txt"
russian_text = read_from_file(input_file_name)

transliterated_text = transliterate(russian_text)

write_to_file(transliterated_text, "result_" + input_file_name)
