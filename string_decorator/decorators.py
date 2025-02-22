import random
from colorama import Fore, Style
import base64
from ._NumericParser import __Math__
import re
import sys

class ValueException(Exception):
    """raised when given value is not the required datatype"""

class NoInput(Exception):
    """raised when an empty string is provided"""

class InvalidEncodedString(Exception):
    """raised when the provided bytes is invalid"""


def randcase(func) -> str:
    """Changes the given text to random cases (upper or lower)"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            return ''.join(random.choice((str.upper, str.lower))(x) for x in text)
    return wrapper

def snakecase(func) -> str:
    """Changes the given text to snake_case"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            return '_'.join(text.lower().split())
    return wrapper

def constantcase(func) -> str:
    """Changes the given text to CONSTANT_CASE"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            return '_'.join(text.upper().split())
    return wrapper

def kebabcase(func) -> str:
    """Changes the given text to kebab-case"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            return '-'.join(text.lower().split())
    return wrapper

def headercase(func) -> str:
    """Changes the given text to Header-Case"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            return '-'.join(text.title().split())
    return wrapper

def pascalcase(func) -> str:
    """Changes the given text to PascalCase"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            return ''.join(text.title().split())
    return wrapper

def camelcase(func) -> str:
    """Changes the given text to camelCase"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            text_list = text.split()
            return text_list[0].lower()+''.join(i.title() for i in text_list[1:])
    return wrapper

def dotcase(func) -> str:
    """Changes the given text to dot.case"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            return '.'.join(text.lower().split())
    return wrapper

def pathcase(func) -> str:
    """Changes the given text to path/case"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            return '/'.join(text.lower().split())
    return wrapper

def swapcase(func) -> str:
    """Changes each upper characters to lower and vice versa"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            new_text = ''
            for i in text:
                if i.isupper():
                    new_text += i.lower()
                else:
                    new_text += i.upper()
            return new_text
    return wrapper

def scramble_sentence(func) -> str:
    """Returns the sentence in random order\n
    Eg: 'Hello my friend' might change to 'my friend Hello'"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            text_list = text.split()
            random.shuffle(text_list)
            return ' '.join(text_list)
    return wrapper

def sentence_reverse(func) -> str:
    """
    Reverses given sentence\n
    Eg: 'Hello world' changes to 'world Hello'
    """
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            text_list = text.split()
            return ' '.join(i for i in text_list[-1::-1])
        
    return wrapper

def random_string(func) -> str:
    """Generates a random string comprising of lower cased or upper cased characters, numbers, symbols"""
    def wrapper(length: int, *args, **kwargs):
        if type(length) != int:
            raise ValueException(f"Length can only be {Fore.GREEN}'int'{Style.RESET_ALL} not {Fore.GREEN}'{type(length).__name__}'{Style.RESET_ALL}")
        else:
            func(*args, **kwargs)
            string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
            return ''.join(random.choice(string) for i in range(length))
    return wrapper

def str_encode(func) -> bytes:
    """Encodes the given text into bytes format"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            return base64.b64encode(text.encode("utf-8"))
    return wrapper

def bytes_decode(func) -> str:
    """Decodes bytes back to string"""
    def wrapper(text: bytes, *args, **kwargs):
        if type(text) != bytes:
            raise ValueException(f"Text can only be {Fore.GREEN}'bytes'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        elif len(text) % 4 != 0:
            raise InvalidEncodedString(f"Number of characters cannot be {Fore.GREEN}{len(text)}{Style.RESET_ALL}, it should be a multiple of {Fore.GREEN}4{Style.RESET_ALL}")
        else:
            func(*args, **kwargs)
            return base64.b64decode(text).decode("utf-8")
    return wrapper

def num_extract(func) -> list[int] | list[str]:
    """Extracts numbers from the given string and returns it as a list of numbers
    :parameters:
        :attr:`string:`
            Set it to True to return numbers in a list of strings\n
            eg: ['1', '23.21', '21,232']\n
            Setting it to False returns numbers as a list of numbers itself\n
            eg: [1,23.21,21232]
    """
    def wrapper(text: str, string: bool = True, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif type(string) != bool:
            raise ValueException(f"String parameter can only be a {Fore.GREEN}'bool'{Style.RESET_ALL} not {Fore.GREEN}'{type(string).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            expression = r'[-\d]+[.,\d]+|[-\d]*[.][\d]+|[-\d]+'
            numbers = re.findall(expression, text)

            if string == True:
                return numbers
            else:
                l = []
                for i in numbers:
                    false_i = i
                    num = false_i.replace(',', '').replace('-', '')
                    check_int = num.isnumeric()
                    if ',' in i:
                        l.append((float(i.replace(',', '')) if check_int == False else int(i.replace(',',''))))
                    else:
                        l.append(float(i) if check_int==False else int(i))
                return l
    return wrapper


def validate_email(func) -> bool:
    """Validates the text to check if the email format is correct"""
    def wrapper(text: str, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        else:
            func(*args, **kwargs)
            expression = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if re.match(expression, text):
                return True
            else:
                return False
    return wrapper

def validate_text(func) -> bool:
    """Validates the text to check if it is right according to the conditions specified.
    :parameters:
        :attr:`length:`
            The minimum length of the text.
        :attr:`uppercase:`
            The minimum number of uppercase letters in the text. Set to 'all' if all letters have to be in uppercase.
        :attr:`lowercase:`
            The minimum number of lowercase letters in the text. Set to 'all' if all letters have to be in lowercase.
        :attr:`numbers:`
            The minimum number of numbers (positive integers) in the text. Set to 'all' if all are numbers.
        :attr:`special_characters:`
            The minimum number of special characters in the text. Set to 'all' if all are special characters.
    """
    def wrapper(text: str, length=6, uppercase=1, lowercase=1, numbers=1, special_characters=1, *args, **kwargs):
        if type(text) != str:
            raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
        elif type(length) != int:
                raise ValueException(f"Length can only be an{Fore.GREEN}'integer'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL} ")
        elif len(text) == 0:
            raise NoInput("Text can't be empty")
        func(*args, **kwargs)
        flag = True
        if len(text) < length:
            flag = False
        if uppercase:
            if type(uppercase) not in (str, int):
                raise ValueException(f"Uppercase parameter can only be {Fore.GREEN}'all'{Style.RESET_ALL}or an{Fore.GREEN}'integer'{Style.RESET_ALL}")
            count = 0
            if uppercase == 'all':
                if not(text.isupper()):
                    flag = False
            else:
                for i in text:
                    if i.isupper():
                        count += 1

                if count < uppercase:
                    flag = False
        if lowercase:
            if type(lowercase) not in (str, int):
                raise ValueException(f"Lowercase parameter can only be {Fore.GREEN}'all'{Style.RESET_ALL}or an{Fore.GREEN}'integer'{Style.RESET_ALL}")
            count = 0
            if lowercase == 'all':
                if not(text.islower()):
                    flag = False
            else:
                for i in text:
                    if i.islower():
                        count += 1

                if count < lowercase:
                    flag = False

        if numbers:
            if type(numbers) not in (str, int):
                raise ValueException(f"Numbers parameter can only be {Fore.GREEN}'all'{Style.RESET_ALL}or an{Fore.GREEN}'integer'{Style.RESET_ALL}")
            count = 0
            if numbers == 'all':
                if not(text.isdigit()):
                    flag = False
            else:
                for i in text:
                    if i.isdigit():
                        count += 1

                if count < numbers:
                    flag = False

        if special_characters:
            if type(special_characters) not in (str, int):
                raise ValueException(f"Special Characters parameter can only be {Fore.GREEN}'all'{Style.RESET_ALL}or an{Fore.GREEN}'integer'{Style.RESET_ALL}")
            count = 0
            characters = "!@#$%^&*()-+?_=,<>/"
            if special_characters == 'all':
                for i in text:
                    if i in characters:
                        count += 1
                if count < len(text):
                    flag = False
            else:
                for i in text:
                    if i in characters:
                        count += 1

                if count < special_characters:
                    flag = False  

        if flag == False:
            return False
        else:
            return True
    return wrapper

def calculate(func) -> float | int:
    """
    Evaluates the given string\n
    eg: '2+3' gives 5
    """
    def wrapper(text: str, *args, **kwargs):
        func(*args, **kwargs)
        string_parser = __Math__()
        return string_parser.eval(text)
    return wrapper
    
