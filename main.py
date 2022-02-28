def transliterate(name):
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'u', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
              'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'C', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'U', 'Я': 'Ya', ',': '', '?': '', ' ': ' ', '~': '', '!': '', '@': '', '#': '',
              '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '-', '=': '', '+': '',
              ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}

    for key in slovar:
        name = name.replace(key, slovar[key])
    return name


inputString = """Антонов 	5 	5 	5
Бобров 	5 	3 	2 
Вяткин 	5 	5 	5 
Дедов	4	4	4
Емельянова	5	5	5
Кротов 	2 	3 	3 
Марьин	5	4	5
Новиков	2	3	2
Подлесный	2	3	3
Полежаев	5	5	5
Соснин 	4 	4 	4 """


splitted = [i.split("\t") for i in inputString.split("\n")]
#print(splitted)


def formatData(data):
    data = data.strip()
    if data.isdigit():
        return int(data)
    else:
        return '\'' + transliterate(data) + '\''


for i in range(len(splitted)):
    lineArray = [formatData(j) for j in splitted[i]]
    print('student(', end='')
    for j in range(len(lineArray)):
        if j != 0:
            print(', ', end='')
        print(lineArray[j], end='')
    print(').')
