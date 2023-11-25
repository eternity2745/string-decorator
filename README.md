# string-decorator

Python Module to have fun with strings

## Usage
```py
from string_decorator import string_decorator 
print(string_decorator.randcase("hello"))
```
#### Output

```
hElLo
```
You can also import it as 
```py
from string_decorator.string_decorator import randcase
print(randcase("hello"))
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
