# hashall


[![PyPI version](https://badge.fury.io/py/hashall.svg)](https://badge.fury.io/py/hashall)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This library was created to use indexed data structures such as list, tuple, str, bytes, and bytearray with keys like those used in dict (hash table)


## Installation


You can install `hashall` via pip:


```bash
pip install hashall
```


## Usage 


#### hlist 


```python
from hashall import hlist


x = hlist([1, 2, 3, 4, 5, 6])
print(x[3])
print(x[+3])
print(x["3"])
print(x["+3"])
print(x[-3])
print(x["-3"])
print(x["three"])
print(x["+three"])
print(x["-three"])
```


### Output


```bash
4
4
4
4
4
4
4
4
4
```


#### htuple


```python
from hashall import htuple


x = htuple([1, 2, 3, 4, 5, 6])
print(x[3])
print(x[+3])
print(x["3"])
print(x["+3"])
print(x[-3])
print(x["-3"])
print(x["three"])
print(x["+three"])
print(x["-three"])
```


### Output


```bash
4
4
4
4
4
4
4
4
4
```


#### hstr


```python
from hashall import hstr


x = hstr("hashall")
print(x[3])
print(x[+3])
print(x["3"])
print(x["+3"])
print(x[-4])
print(x["-4"])
print(x["three"])
print(x["+three"])
print(x["-four"])
```


### Output


```bash
h
h
h
h
h
h
h
h
h
```


#### hbytes


```python
from hashall import hbytes


x = hbytes(b"hashall")
print(x[3])
print(x[+3])
print(x["3"])
print(x["+3"])
print(x[-4])
print(x["-4"])
print(x["three"])
print(x["+three"])
print(x["-four"])
```


### Output


```bash
104
104
104
104
104
104
104
104
104
```

#### hbytearray


```python
from hashall import hbytearray


x = hbytearray(b"hashall")
print(x[3])
print(x[+3])
print(x["3"])
print(x["+3"])
print(x[-4])
print(x["-4"])
print(x["three"])
print(x["+three"])
print(x["-four"])
```


### Output


```bash
104
104
104
104
104
104
104
104
104
```


### Note


You can use all the methods you've been using with these data structures 


## License


This project is licensed under the MIT LICENSE - see the [LICENSE](https://opensource.org/licenses/MIT) for more details.
