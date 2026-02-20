name= 'kishan'
for i in name:
    print(i)
    if(i=="s"):
        print("s is found")
        break
#list
colors=["red","green","blue","yellow"]
for color in colors:
    print(color)
    for letter in color:
        print(letter)
    # if color=="blue":
    #     print("blue is found")
    #     break
    #range
    for k in range(5):
        print(k+1)

    for k in range(1, 10, 2):
        print(k)