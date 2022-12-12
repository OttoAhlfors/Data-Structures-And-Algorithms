#https://www.geeksforgeeks.org/what-is-linked-list/
#https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/?ref=lbp
#https://realpython.com/linked-lists-python/
#https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

from locale import currency


class Node:
    #Tehdään data ja next joilla voidaan säilyttää dataa ja viittata seuraavaan nodeen
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    #Tehdään head joka viittaa ensimmäiseen nodeen
    def __init__(self):
        self.head = None

    #Append lisää uuden noden listan loppuun
    def append(self, data):
        #Jos listassa ei ole yhtään nodea, niin data laitetaan ensimmäiseen nodeen
        if self.head is None:
            self.head = Node(data)
        else:
            #Muuten käydään listaa läpi kunnes löytyy viimeinen node
            current = self.head
            while current.next is not None:
                current = current.next
            #Data laitetaan viimeiseen
            current.next = Node(data)

    #Insert lisää uuden noden listan haluttuun indeksiin
    def insert(self, data, index):
        new = Node(data)
        #Jos muokataan listan ensimmäistä nodea
        if index == 0:
            new.next = self.head
            self.head = new
        #Muuten käydään listaa läpi kunnes löytyy haluttu node
        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            #Data pitää siirtää seuraavaan nodeen ennen sen asettamista haluttuun nodeen
            new.next = current.next
            current.next = new

    #Poistetaan haluttu node
    def delete(self, removekey):
        current = self.head
        
        #Jos poistetaan listan ensimmäinen node
        if (current is not None):
            if (removekey == 0):
                self.head = current.next
                current = None
                return
        
        #Etsitään poistettava node
        for i in range(removekey):
            #Tallennetaan edellinen node
            previous = current
            if current is not None:
                current = current.next

        #Jos nodea ei löydy
        if (current == None):
            return
        
        #Poistetaan node
        previous.next = current.next
        current = None

    #Palautetaan halutun noden indeksi
    def index(self, data):
        current = self.head
        index = 0
        #Käydään listaa läpi kunnes löytyy haluttu node
        while current is not None:
            #Jos node löytyy, palautetaan indeksi
            if current.data == data:
                return index
            current = current.next
            index += 1
        #Jos nodea ei löydy, palautetaan -1
        return -1
    
    #Printataan lista
    def print(self):
        current = self.head
        while current is not None:
            if current.next is not None:
                print(current.data, end=" -> ")
            else:
                print(current.data)
            current = current.next


if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(2)
    L.append(2)
    L.append(3)
    L.append(3)
    L.append(1)
    L.append(4)
    L.append(4)
    L.print()           # 15 -> 1 -> 10 -> 3
    L.delete(0)
    L.delete(1)
    L.delete(4)
    L.delete(5)
    L.print()           # 1 -> 10 -> 3