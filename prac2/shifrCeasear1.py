def shifrCeasearCode(text, lang):
    '''
    Функция для кодирования текста шифром цезаря.
    Получает на вод текст и язык текста, возвращает закодированный текст.
    '''
    if lang == 'eng':
        return ''.join([eng_letters_code[letter] for letter in text])
    elif lang == 'rus':
        return ''.join([rus_letters_code[letter] for letter in text])


def shifrCeasearDecode(text, lang):
    '''
    Функция для декодирования текста шифром цезаря.
    Получает на вод текст и язык текста, возвращает декодированный текст.
    '''
    if lang == 'eng':
        return ''.join([eng_letters_decode[letter] for letter in text])
    elif lang == 'rus':
        return ''.join([rus_letters_decode[letter] for letter in text])

def langCheck(text):
    '''
    Определяет язык текста.
    Получает на вход текст, возвращает язык текста.
    '''
    if text[0] in eng_letters_code:
        return 'eng'
    else:
        return 'rus'


eng_letters_code = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
                    'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
                    'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a', ' ': ' '}
eng_letters_decode = {'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i',
                      'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r',
                      't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y', 'a': 'z', ' ': ' '}
rus_letters_code = {'а': 'б', 'б': 'в', 'в': 'г', 'г': 'д', 'д': 'е', 'е': 'ж', 'ж': 'з', 'з': 'и', 'и': 'й', 'й': 'к',
                    'к': 'л', 'л': 'м', 'м': 'н', 'н': 'о', 'о': 'п', 'п': 'р', 'р': 'с', 'с': 'т', 'т': 'у', 'у': 'ф',
                    'ф': 'х', 'х': 'ц', 'ц': 'ч', 'ч': 'ш', 'ш': 'щ', 'щ': 'ъ', 'ъ': 'ы', 'ы': 'ь', 'ь': 'э', 'э': 'ю',
                    'ю': 'я', 'я': 'а', ' ': ' '}
rus_letters_decode = {'б': 'а', 'в': 'б', 'г': 'в', 'д': 'г', 'е': 'д', 'ж': 'е', 'з': 'ж', 'и': 'з', 'й': 'и',
                      'к': 'й', 'л': 'к', 'м': 'л', 'н': 'м', 'о': 'н', 'п': 'о', 'р': 'п', 'с': 'р', 'т': 'с',
                      'у': 'т', 'ф': 'у', 'х': 'ф', 'ц': 'х', 'ч': 'ц', 'ш': 'ч', 'щ': 'ш', 'ъ': 'щ', 'ы': 'ъ',
                      'ь': 'ы', 'э': 'ь', 'ю': 'э', 'я': 'ю', 'а': 'я', ' ': ' '}

text = '123'
while text != '0':
    text = input('Введите текст для кодирования/декодирования или 0 для завершения программы: ').lower()
    lang = langCheck(text)
    code_decode_choice = input('Введите 1 для кодирования или 2 для декодирования: ')
    if code_decode_choice == '1':
        print(shifrCeasearCode(text, lang))
    else:
        print(shifrCeasearDecode(text, lang))
