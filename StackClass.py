""" Quastions. A python programm to create a stake class that
 can perform some important operation"""
# Stack Class - Save this as Stack.py

class Stack:
    def __init__(self):
        self.st=[]
    def isempty(self):
        return self.st==[]
    def __push__(self,element):
        self.st.append(element)
    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.st.pop()
    def peep(self):
        n=len(self.st)
        return self.st[n-1]
    def search(self,element):
        if self.isempty():
            return -1
        else:
            try:
                n=self.st.index(element)
                return len(self.st)-n
            except ValueError:
                return -2
    def Display(self):
        return self.st