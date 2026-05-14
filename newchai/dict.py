PS C:\python-practice\newchai> python
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> chai={"ksihan":"kanpur","ginger"}
  File "<stdin>", line 1
    chai={"ksihan":"kanpur","ginger"}
                                   ^
SyntaxError: ':' expected after dictionary key
>>> chai={"ksihan":"kanpur","ginger":"jastya","kanpur":"shyamangar"}
>>> print(chai)
{'ksihan': 'kanpur', 'ginger': 'jastya', 'kanpur': 'shyamangar'}
>>> chai["ginger"]  
'jastya'
>>> chai.get("ginger")
'jastya'
>>> chai.get("gingers")
>>> chai={"ksihan":"kanpur","ginger":"jastya","kanpur":"shyamangar"}
>>> chai
{'ksihan': 'kanpur', 'ginger': 'jastya', 'kanpur': 'shyamangar'}
>>> chai["kanpur"]="Yashodangar"
>>> chai
{'ksihan': 'kanpur', 'ginger': 'jastya', 'kanpur': 'Yashodangar'}
>>> for x in chai:
...     print(chai)
... 
{'ksihan': 'kanpur', 'ginger': 'jastya', 'kanpur': 'Yashodangar'}
{'ksihan': 'kanpur', 'ginger': 'jastya', 'kanpur': 'Yashodangar'}
{'ksihan': 'kanpur', 'ginger': 'jastya', 'kanpur': 'Yashodangar'}
>>> for chai in chai:
...     print(chai)  
... 
ksihan
ginger
kanpur
>>> for x in chai: 
...     print(x,chai["x"])
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    print(x,chai["x"])
            ~~~~^^^^^
TypeError: string indices must be integers, not 'str'
>>>     print(x,chai[x])  
  File "<stdin>", line 1
        print(x,chai[x])
    ^
IndentationError: unexpected indent
>>> chai
'kanpur'
>>> chai={"ksihan":"kanpur","ginger":"jastya","kanpur":"shyamangar"}
>>> chai
{'ksihan': 'kanpur', 'ginger': 'jastya', 'kanpur': 'shyamangar'}
>>> for x in chai
  File "<stdin>", line 1
    for x in chai
                 ^
SyntaxError: expected ':'
>>> for x in chai:
...     print(x)
... 
ksihan
ginger
kanpur
>>> for x in chai:
...     print(x,chai[x])
... 
ksihan kanpur
ginger jastya
kanpur shyamangar
>>> for key, values in chai:
...     print[x]
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    for key, values in chai:
        ^^^^^^^^^^^
ValueError: too many values to unpack (expected 2)
>>> for key, values in chai.items():
...     print(key,vlaues)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    print(key,vlaues)
              ^^^^^^
NameError: name 'vlaues' is not defined. Did you mean: 'values'?
>>> for key, values in chai.items():
...     print(key,values)\  
... 
...     print(key,values) 
... 
ksihan kanpur
ksihan kanpur
ginger jastya
ginger jastya
kanpur shyamangar
kanpur shyamangar
>>> if "kanpur" in chai:
...     print("yes")
... 
yes
>>> print(len(chai))
3
>>> chai
{'ksihan': 'kanpur', 'ginger': 'jastya', 'kanpur': 'shyamangar'}
>>> chai["earl"]="testing"
>>> chai
{'ksihan': 'kanpur', 'ginger': 'jastya', 'kanpur': 'shyamangar', 'earl': 'testing'}
>>> chai.pop(ksihan)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai.pop(ksihan)
             ^^^^^^
NameError: name 'ksihan' is not defined
>>> chai.pop("ksihan")
'kanpur'
>>> chai
{'ginger': 'jastya', 'kanpur': 'shyamangar', 'earl': 'testing'}
>>> chai.popitem()                
('earl', 'testing')
>>> chai
{'ginger': 'jastya', 'kanpur': 'shyamangar'}
>>> del chai(:ginger")
  File "<stdin>", line 1
    del chai(:ginger")
             ^
SyntaxError: invalid syntax
>>> del chai("ginger")
  File "<stdin>", line 1
    del chai("ginger")
        ^^^^^^^^^^^^^^
SyntaxError: cannot delete function call
>>> del chai["ginger"]
>>> chai
{'kanpur': 'shyamangar'}
>>> chai_copy=chai.copy()
>>> chai
{'kanpur': 'shyamangar'}
>>> chai.copy
<built-in method copy of dict object at 0x0000023459299740>
>>> tea_shop={ 
... "chai":{"masala":"spicy","ginger":"jasty"}
... "chai":{"masala":"spicy","ginger":"jasty"},
  File "<stdin>", line 2
    "chai":{"masala":"spicy","ginger":"jasty"}
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> tea_shop={
... "chai":{"masala":"spicy","ginger":"jasty"},
... "tea":{"green":"fresh","black":"strong"}
... }
>>> tea
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea
NameError: name 'tea' is not defined
>>> tea_shop
{'chai': {'masala': 'spicy', 'ginger': 'jasty'}, 'tea': {'green': 'fresh', 'black': 'strong'}}
>>> print(tea_shop)
{'chai': {'masala': 'spicy', 'ginger': 'jasty'}, 'tea': {'green': 'fresh', 'black': 'strong'}}
>>> tea_shop["chai"]
{'masala': 'spicy', 'ginger': 'jasty'}
>>> tea_shop["chai"]["ginger"]
'jasty'
>>> squqre={x:x**2 for x in range(10)}
>>> squqre 
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> squqre.clear()
>>> squqre        
{}
>>> keys = ["masla","ginger","lemon"]
>>> keys
['masla', 'ginger', 'lemon']
>>> default_value="need"
>>> new_dict=dict.fromkeys(keys,default_value)
>>> new_dict
{'masla': 'need', 'ginger': 'need', 'lemon': 'need'}
>>> new_dict
{'masla': 'need', 'ginger': 'need', 'lemon': 'need'}
>>> 