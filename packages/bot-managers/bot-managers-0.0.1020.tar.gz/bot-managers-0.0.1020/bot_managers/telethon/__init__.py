message = """Метод `strip()` в Python удаляет только пробельные символы (пробелы, табуляции, символы новой строки) с начала и конца строки. Он не удаляет символы новой строки, если они не являются начальными или конечными пробельными символами.\n\nЕсли вам нужно удалить символы новой строки в начале и конце строки, вы можете воспользоваться методом `strip()` с аргументом, указывающим, какие символы нужно удалить. В вашем случае, вам нужно указать символ новой строки (`\'\\n\'`) в качестве аргумента метода `strip()`. \n\nВот пример:\n\n```python\nstring = "\\nHello, World!\\n"\nnew_string = string.strip(\'\\n\')\nprint(new_string)  # Вывод: "Hello, World!"\n```\n\nТаким образом, передавая символ новой строки в качестве аргумента методу `strip()`, вы сможете удалить его из начала и конца строки."""


def get_lang(message: str, i: int, end: int):
    """
    Get the language of the code block.
    :param message:
    :param i:
    :param end:
    :return:
    """
    lang = ''
    # Find the position of the first newline character after
    # the end of the first delimiter
    start_code = message.find('\n', i)

    # If no newline is found, assume that no language is
    # specified
    if not start_code == -1:
        lang = message[i:start_code].strip()
        # If the language does not match the regular expression,
        # assume that no language is specified
        if re.compile(r'[a-zA-Z0-9_-]{1,32}').fullmatch(lang) is not None:
            code_block = message[start_code:end - 1].strip()
            print(f'{code_block=}')
            print(f'{message[end:]=}')
            message = message[:i] + code_block + message[end - 1:]
            end = i + len(code_block)
    return lang, message, end