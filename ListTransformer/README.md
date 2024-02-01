# ListTransformer
## Installation
``pip install ListTransformer``

## Examples

````py
import ListTransformer

liste = ListTransformer.lister("123 123 123")
print(liste)
print(ListTransformer.str_list(liste))
````

### lister

- (required) str_list: ```str``` the text to convert to list
- (optional) typ: ``lister.Typ`` the method for example comma or space, default is that it is selected automatically  
  - Attributes ```ListTransformer.Typ.auto, ListTransformer.Typ.comma, ListTransformer.Typ.space``` the input format

#### Example

````py
import ListTransformer

print(ListTransformer.lister("123 123 123"))
print(ListTransformer.lister("123, 123, 123"))
````
#### First and secend Output
``['123', '123', '123']`` as ``list``

### str_list

- (required) list: ``list`` The list to be converted into a string
- (optional) split: ``lister.Splits`` The way in which the string should separate the entries  
  - Attributes ```ListTransformer.Splits.space, ListTransformer.Splits.comma``` the output format

#### Example

````py
import ListTransformer

liste = ["test1", "test2", "test3"]

print(ListTransformer.str_list(liste))
print(ListTransformer.str_list(liste, ListTransformer.Splits.space))
````
#### Outputs
``test1, test2, test3`` as ``string``  
``test1 test2 test3`` as ``string``