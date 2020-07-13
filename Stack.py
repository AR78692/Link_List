"""Qustions. A Python programm to perform various 
operations on a stack using Stack Class"""
#Using the Stack Class of Stack.py Program
from StackClass import Stack
# Create empty stack object
s=Stack()
#Display Menu
Choice=0
while Choice<5:
    print('_______Stack Operation_______')
    print('1. Push Element')
    print('2. Pop Element')
    print('3. Peep Element')
    print('4. Search for Element')
    print('5. Exit')
    Choice=int(input('Enter your Choice:'))
    
    # Perform a task depending on user choice
    if Choice==1:
        element=int(input('Enter Element:'))
        s.__push__(element)
    elif Choice==2:
        element=s.pop()
        if element== -1:
            print('The Stack Is Empty')
        else:
            print('Popped element=',element)
    elif Choice==3:
        element=s.peep()
        print('Topmost Element=',element)
    elif Choice==4:
        element=int(input('Enter element:'))
        pos=s.search(element)
        if pos== -1:
            print('The Stack Is Empty')
        elif pos== -2:
            print('Element not Found in this Stack!')
        else:
            print('Element Found at Position:',pos)
    else:
        break
    print('Stack= ',s.Display())
