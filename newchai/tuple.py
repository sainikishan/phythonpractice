>>> tea[0]="Lemon"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea[0]="Lemon"
    ~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> len(tea)
4
>>> more=("herbal","earl grey")
>>> all=more+tea
>>> all
('herbal', 'earl grey', 'black', 'Grre', 'list', 'test')
>>> if "green" in all:
...      print("U have a tea")
... 
>>> tea=("black","Grre","list","test")