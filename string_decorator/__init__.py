import random
from colorama import Fore, Style
import base64
from .NumericParser import Math
import re

class ValueException(Exception):
    """raised when given value is not the required datatype"""

class NoInput(Exception):
    """raised when an empty string is provided"""

class InvalidEncodedString(Exception):
    """raised when the provided bytes is invalid"""


def randcase(text: str):
    """Changes the given text to random cases (upper or lower)"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        return ''.join(random.choice((str.upper, str.lower))(x) for x in text)

def snakecase(text: str):
    """Changes the given text to snake_case"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        return '_'.join(text.lower().split())
    
def constantcase(text: str):
    """Changes the given text to CONSTANT_CASE"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        return '_'.join(text.upper().split())
    
def kebabcase(text: str):
    """Changes the given text to kebab-case"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        return '-'.join(text.lower().split())

def headercase(text: str):
    """Changes the given text to Header-Case"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        return '-'.join(text.title().split())
    
def pascalcase(text: str):
    """Changes the given text to PascalCase"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        return ''.join(text.title().split())
    
def camelcase(text: str):
    """Changes the given text to camelCase"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        text_list = text.split()
        return text_list[0].lower()+''.join(i.title() for i in text_list[1:])
    
def dotcase(text: str):
    """Changes the given text to dot.case"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        return '.'.join(text.lower().split())
    
def pathcase(text: str):
    """Changes the given text to path/case"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        return '/'.join(text.lower().split())
    
def swapcase(text: str):
    """Changes each upper characters to lower and vice versa"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        new_text = ''
        for i in text:
            if i.isupper():
                new_text += i.lower()
            else:
                new_text += i.upper()
        return new_text
    
def scramble_sentence(text: str):
    """Returns the sentence in random order\n
    Eg: 'Hello my friend' might change to 'my friend Hello'"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        text_list = text.split()
        random.shuffle(text_list)
        return ' '.join(text_list)
    
def sentence_reverse(text: str):
    """
    Reverses given sentence\n
    Eg: 'Hello world' changes to 'world Hello'
    """
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        text_list = text.split()
        return ' '.join(i for i in text_list[-1::-1])
    
def random_string(length: int):
    """Generates a random string comprising of lower cased or upper cased characters, numbers, symbols"""
    if type(length) != int:
        raise ValueException(f"Length can only be {Fore.GREEN}'int'{Style.RESET_ALL} not {Fore.GREEN}'{type(length).__name__}'{Style.RESET_ALL}")
    else:
        string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        return ''.join(random.choice(string) for i in range(length))
    
def str_encode(text: str):
    """Encodes the given text into bytes format"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        return base64.b64encode(text.encode("utf-8"))
    
def bytes_decode(text: bytes):
    """Decodes bytes back to string"""
    if type(text) != bytes:
        raise ValueException(f"Text can only be {Fore.GREEN}'bytes'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    elif len(text) % 4 != 0:
        raise InvalidEncodedString(f"Number of characters cannot be {Fore.GREEN}{len(text)}{Style.RESET_ALL}, it should be a multiple of {Fore.GREEN}4{Style.RESET_ALL}")
    else:
        return base64.b64decode(text).decode("utf-8")

def num_extract(text: str, string: bool = True):
    """Extracts numbers from the given string and returns it as a list of numbers
    :parameters:
        :attr:`string:`
            Set it to True to return numbers in a list of strings\n
            eg: ['1', '23.21', '21,232']\n
            Setting it to False returns numbers as a list of numbers itself\n
            eg: [1,23.21,21232]
    """
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif type(string) != bool:
        raise ValueException(f"String parameter can only be a {Fore.GREEN}'bool'{Style.RESET_ALL} not {Fore.GREEN}'{type(string).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        expression = '[-\d]+[.,\d]+|[-\d]*[.][\d]+|[-\d]+'
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
        
def validate_email(text: str):
    """Validates the text to check if the email format is correct"""
    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    else:
        expression = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(expression, text):
            return True
        else:
            return False
        
def validate_text(text: str, length=6, uppercase=1, lowercase=1, numbers=1, special_characters=1):
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

    if type(text) != str:
        raise ValueException(f"Text can only be a {Fore.GREEN}'string'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL}")
    elif type(length) != int:
            raise ValueException(f"Length can only be an{Fore.GREEN}'integer'{Style.RESET_ALL} not {Fore.GREEN}'{type(text).__name__}'{Style.RESET_ALL} ")
    elif len(text) == 0:
        raise NoInput("Text can't be empty")
    
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

def calculate(text: str):
    """
    Evaluates the given string\n
    eg: '2+3' gives 5
    """
    string_parser = Math()
    return string_parser.eval(text)
