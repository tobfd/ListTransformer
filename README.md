# Lister
## Installation
``pip install lister`` coming soon

## Examples

````py
import py_lister

liste = py_lister.lister("123 123 123")
print(liste)
print(py_lister.str_list(liste))
````

### lister

- (required) str_list: ```str``` the text to convert to list
- (optional) typ: ``lister.Typ`` the method for example comma or space, default is that it is selected automatically  
  - Attributes ```lister.Typ.auto, lister.Typ.comma, lister.Typ.space``` the input format

#### Example

````py
import py_lister

print(py_lister.lister("123 123 123"))
print(py_lister.lister("123, 123, 123"))
````
#### First and secend Output
``['123', '123', '123']`` as ``list``

### str_list

- (required) list: ``list`` The list to be converted into a string
- (optional) split: ``lister.Splits`` The way in which the string should separate the entries  
  - Attributes ```lister.Splits.space, lister.Splits.comma``` the output format

#### Example

````py
import py_lister

liste = ["test1", "test2", "test3"]

print(py_lister.str_list(liste))
print(py_lister.str_list(liste, py_lister.Splits.space))
````
#### Outputs
``test1, test2, test3`` as ``string``  
``test1 test2 test3`` as ``string``