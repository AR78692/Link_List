#Link List
link_List=[]
Choice=0
while Choice<=6:
    print('___________Link List Operation____________')
    print('1. Add Element')
    print('2. Delete Element')
    print('3. Replace Element')
    print('4. Search Element')
    print('5. Clear')
    print('6. Exit')
    Choice=int(input('Enter your Choice:'))
    if Choice==1:
        element=input('Enter Your Add Element:')
        link_List.append(element)
        print('Element SuccessFully Added....!')
        print('______LinkList______')
        print(link_List)
    elif Choice==2:
        try:
            element=input('Enter your Delete Element:')
            link_List.remove(element)
            print('Element SuccessFully Deleted...!')
            print('______LinkList______')
            print(link_List)
        except ValueError:
            print('Value Not Found...!')
    elif Choice==3:
        try:
            element=input('Enter your Replace Element:')
            position=link_List.index(element)
            link_List.remove(element1)
            element=input('Enter your New Element:')
            link_List.insert(position,element)
            print('Element Replace SuccessFully...!')
            print('______LinkList______')
            print(link_List)
        except ValueError:
            print('Element Not Match For Replace...!')
    elif Choice==4:
        try:
            element=input('Enter your Search Element:')
            position=link_List.index(element)
            print('Element Found At Position:',position)
            print('______LinkList______')
            print(link_List)
        except ValueError:
            print('Search Element not Match in Link List...!')
    elif Choice==5:
        link_List.clear()
        print('Link List Clear Sucessfully...!')
        print(link_List)
    else:
        break
