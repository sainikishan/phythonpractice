#array
['black', 'white', 'oolng', 'grren']
>>> tea[1:1]  
[]
>>> tea[1:1]=["test","test"]
>>> print(tea)              
['black', 'test', 'test', 'white', 'oolng', 'grren']
>>> tea[1:2]  
['test']
>>> tea[1:3]
['test', 'test']
>>> tea[1:3]=[]
>>> print(tea) 
['black', 'white', 'oolng', 'grren']
>>> exit()
>>> tea
['black', 'white', 'oolng']
>>> tea.insert(1,"green")
>>> tea
['black', 'green', 'white', 'oolng']
>>> tea.remove("grren")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea.remove("grren")
    ~~~~~~~~~~^^^^^^^^^
ValueError: list.remove(x): x not in list
>>> tea.remove("green")
>>> tea
['black', 'white', 'oolng']
>>> tea
['black', 'white', 'oolng']
>>> tea_copy=tea.copy()
>>> tea
['black', 'white', 'oolng']
>>> tea_copy.append("lemon")
>>> tea
['black', 'white', 'oolng']
>>> tea_copy           
['black', 'white', 'oolng', 'lemon']

    tea.remove("grren")
    ~~~~~~~~~~^^^^^^^^^
ValueError: list.remove(x): x not in list
>>> tea.remove("green")
>>> tea
['black', 'white', 'oolng']
>>> tea
['black', 'white', 'oolng']
>>> tea_copy=tea.copy()
>>> tea
['black', 'white', 'oolng']
>>> tea_copy.append("lemon")
>>> tea
['black', 'white', 'oolng']
>>> tea_copy           
['black', 'white', 'oolng', 'lemon']
>>> squared_nums=[x**2 for x in range(10)]
>>> range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> y = range(10)
>>> y
range(0, 10)
>>> squared_nums=[x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube=[x**3 for x in range(10)]
>>> cube
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]