import random
from colorama import Fore, Style
import base64

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
