# string-decorator

Python Module to have fun with strings. The module also makes use of python decorators<br>
[![PyPI version](https://badge.fury.io/py/string-decorator.svg)](https://badge.fury.io/py/string-decorator) [![Downloads](https://static.pepy.tech/badge/string-decorator)](https://pepy.tech/project/string-decorator) [![Downloads](https://static.pepy.tech/badge/string-decorator/month)](https://pepy.tech/project/string-decorator) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Usage
### Example 1 -> Calculating expression from given string
```py
from string_decorator import calculate
print(calculate("(123+23) * 23 / 32"))
```
#### Output
```
104.9375
```
### Example 2 -> Validating text based on given conditions
```py
from string_decorator import validate_text
print(validate_text("imEternity1234@strings", length = 13, uppercase = 1, lowercase = 5, numbers = 4, special_characters=1))
```
#### Output
```
True
```
### Example 3 -> Converting the string to random cases
```py
from string_decorator import randcase
print(randcase("hello"))
```
#### Output
```
hELlO
```
### Example 4 -> Extracting numbers from the given string
```py
from string_decorator import num_extract
print(num_extract("hello123 23,211 42.23 -134 g00d"))
```
#### Output
```
['123', '23,211', '42.23', '-134', '00']
```
### Example 5 -> Changing string to CONSTANT_CASE
```py
from string_decorator import constantcase
print(constantcase("hello there"))
```
#### Output
```
HELLO_THERE
```

## Using String Decorators
## Example 1 -> Calculating Expression From String
```py
from string_decorator.decorators import calculate
@calculate
def calc():
  print("The answer is:", end = " ")

print(calc("843 + sin(32)"))
```
#### Output
```
The answer is: 843.5514266812417
```
### Example 2 -> Validating text based on given conditions
```py
@validate_text
def validate():
    return

print(validate("imEternity1234@strings", length = 13, uppercase = 1, lowercase = 5, numbers = 4, special_characters=1))
```
#### Output
```
True
```

## Documentation
`text` is a common parameter for all the functions
| Name | Description |
|:--|:--|
| `randcase` | Changes the given text to random cases (upper or lower) |
| `snakecase` | Changes the given text to `snake_case` |
| `constantcase` |  Changes the given text to `CONSTANT_CASE` |
| `kebabcase` | Changes the given text to `kebab-case` |
| `headercase` | Changes the given text to `PascalCase` |
| `camelcase` | Changes the given text to `camelCase` |
| `dotcase` | Changes the given text to `dot.case` |
| `pathcase` | Changes the given text to `path/case` |
| `swapcase` | Changes each upper characters to lower and vice versa |
| `scramble_sentence` | Returns the sentence in random order  Eg: `'Hello my friend'` might change to `'my friend Hello'` |
| `sentence_reverse` | Reverses given sentence  Eg: `'Hello world'` changes to `'world Hello'` |
| `random_string` | Generates a random string comprising of lower cased or upper cased characters, numbers, symbols |
| `str_encode` | Encodes the given text into bytes format |
| `bytes_decode` | Decodes bytes back to string |
| `num_extract` | Extracts numbers from the given strings<br>*parameters:*<br>- `string:` Set it to True to return numbers in a list of strings
| `validate_email` | Validates the text to check if the email format is correct
| `validate_text` | Validates the text to check if it is right according to the conditions specified<br>*parameters:*<br>- `length:` The minimum length of the text<br>- `uppercase:` The minimum number of uppercase letters in the text. Set to 'all' if all letters have to be in uppercase.<br>- `lowercase:` The minimum number of lowercase letters in the text. Set to 'all' if all letters have to be in lowercase.<br>- `numbers:` The minimum number of numbers (positive integers) in the text. Set to 'all' if all are numbers.<br>- `special_characters:` The minimum number of special characters in the text. Set to 'all' if all are special characters.
| `calculate` | Evaluates the given string<br>Eg: "5+2" gives 7

