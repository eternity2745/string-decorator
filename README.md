# string-decorator

Python Module to have fun with strings

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

## Documentation

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
