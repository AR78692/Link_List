#A LinkList Stores a Group of String
#Create an Empty LinkList
LinkList=[]
#Add Some String type Element to LinkList
LinkList.append('West Bangal')
LinkList.append('Bihar')
LinkList.append('Assam')
LinkList.append('Utter Pardesh')
#Display the LinkList
print('The Existing List Is',LinkList)
#Create A Display Menu
Choice=0
while Choice<=6:
    print('LINK LIST OPERATION')
    print('1. Add Element')
    print('2. Remove Element')
    print('3. Replace Element')
    print('4. Search Element')
    print('5. Display')
    print('6. Exit')
    Choice=int(input('Enter your Choice:'))
    #Perforam A Task Depending on user
    #Logice For Add Element
    if Choice==1:
        element=input('Enter A Element For Add:')
        pos=int(input('Enter Element Position:'))
        LinkList.insert(pos,element)
    #Logic For Remove Element
    elif Choice==2:
        try:
            element=input('Enter your Remove Element:')
            LinkList.remove(element)
        except ValueError:
            print('Element Not Found!')
    #Logic For Replace Element
    elif Choice==3:
        element=input('Enter your Replace Element:')
        pos=int(input('Enter your Replace Position No:'))
        LinkList.pop(pos)
        LinkList.insert(pos,element)
    #Logic For Search Element
    elif Choice==4:
        element=input('Enter your Search Element:')
        try:
            pos=LinkList.index(element)
            print('Element Found At Position:',pos)
        except ValueError:
            print('Element Not Found!')
    elif Choice==5:
        print('_____Link List Value is_____')
        print(LinkList)
    else:
        break
    print('Link List Value Is')
    print(LinkList)

# #logic For Replace Element
#     if Choice==1:
#         try:
#             element=input('Enter your Repace element:')
#             if element in ll:
#                 pos=ll.index(element)
#                 ll.remove(element)
#                 element1=input('Enter your new element:')
#                 ll.insert(pos,element1)
#             else:
#                 break
#         except ValueError:
#             print('Value not Found')
#_____________Another Way__________________

#Link List
# link_list=[]
# link_list.append('Bishahar')
# link_list.append('Gorahar')
# link_list.append('Raiganj')
# link_list.append('Uttar DinajPur')
# print(link_list)
# Choice=0
# while Choice<=6:
#     print('____Link List Operation____')
#     print('1. Add Element')
#     print('2. Delete Element')
#     print('3. Replace Element')
#     print('4. Search Element')
#     print('5. Display')
#     print('6. Exit')
#     Choice=int(input('Enter your Choice:'))
    
#     if Choice==1:
#         Last_End=0
#         while Last_End<=4:
#             print('___Where You Want To Add A Value___')
#             print('1. Append Mode')
#             print('2. Chose Position Mode')
#             print('3. Exit')
#             Last_End=int(input('Enter your Add Mode:'))

#             if Last_End==1:
#                 element=input('Enter your Append Element:')
#                 link_list.append(element)
#                 print('Element Add Successfully...')
#                 print(link_list)
#             elif Last_End==2:
#                 element=input('Enter your Add element:')
#                 position=int(input('Enter your Element Position:'))
#                 link_list.insert(position,element)
#                 print('Element Added Successfully...')
#                 print(link_list)
#             else:
#                 break
#     elif Choice==2:
#         try:
#             element=input('Enter your Delete Element:')
#             pos=link_list.index(element)
#             link_list.pop(pos)
#             print(link_list)
#         except ValueError:
#             print('Element Not Found!')
#     elif Choice==3:
#         try:
#             element=input('Enter your Replace element:')
#             if element in link_list:
#                 find=link_list.index(element)
#                 link_list.remove(element)
#                 element1=input('Enter your Replace Element:')
#                 link_list.insert(find,element1)
#                 print('Element Replace Element Successfully...')
#                 print(link_list)
#             else:
#                 print('Value Not Match!') 
#         except ValueError:
#             print('Value Not Found!')
#     elif Choice==4:
#         element=input('Enter your Search Element:')
#         try:
#             pos=link_list.index(element)
#             print('Element Found At Position:',pos)
#             print(link_list)
#         except ValueError:
#             print('Element not found!')
#     elif Choice==5:
#         print('______Display______')
#         print(link_list)
#     else:
#         break