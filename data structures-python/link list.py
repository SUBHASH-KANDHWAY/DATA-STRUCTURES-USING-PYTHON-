
class node:
    def __init__(self , data ,next):
        self.data=data
        self.next=None;

class Linklist:
    def __init__(self):
        self.start=None;

    def deleteFirst(self):
        if self.start==None:
            print('List is empty')
        else:
            self.start=self.start.next

    def transverse(self):
        if self.start==None:
            print('List is empty')
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=' ')


    def Insertlast(self , value):
        newnode=node(value)
        if (self.start==None):
            self.start=newnode;
        else:
            temp=self.start
            while temp.next!=None :
                temp=temp.next
            temp.next=newnode

print('hello')
mylist=Linklist()
mylist.Insertlast(1)
mylist.Insertlast(4)
mylist.Insertlast(3)
mylist.Insertlast(0)
mylist.transverse()
print()
mylist.deleteFirst()
mylist.transverse()


if __name__=='__main__':
    pass