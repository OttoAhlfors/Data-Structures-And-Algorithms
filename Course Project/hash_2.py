# Lähteet:
# Hash:
# https://moodle.lut.fi/mod/page/view.php?id=712862
# https://moodle.lut.fi/mod/page/view.php?id=712870
# https://moodle.lut.fi/mod/page/view.php?id=661710
#
# Linked list:
# https://moodle.lut.fi/mod/page/view.php?id=661707
#
# Previous work from the course was also used as a reference
# Week4 hashbucket.py, hashlinear.py and week3 linked.py

# Timeit used to measure the time it takes to run parts of the code
import timeit

# Node for the linked list that is used in the hash table
class Node:

    # Initialize the node:
    # Node has the value and a pointer to the next node.
    def __init__(self, value):
        self.value = value
        self.next = None

# Hash table class
class HashTable:

    # Initialize the hash table:
    # Hash table has a size and a table that is an empty list.
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    # Hash function:
    # The given value (string) is converted to an integer one character at a time
    # ord() returns the ASCII value of the character those values are added together.
    # If the value is an integer it is not converted and just used as it is.
    # The sum is then divided by the size of the hash table and the remainder is returned
    # as the key for the hash table.
    def hash(self, value):
        if type(value) != str:
            key = value % self.size
        else:
            key = sum(ord(character) for character in value) % self.size
        return key

    # Collision handling:
    # If the hash function returns the same key for two different values.
    # Variable node is created based on the slot in the hash table the value should have been in
    # from this node we can traverse the linked list until we find the end of the list and add the value there.
    # This is done by creating a new node with the value information to the end of the list.
    def collision(self, key, value):
        print("Collision")
        node = self.table[key]
        while node.next != None:
            node = node.next
        node.next = Node(value)
        print(f"Inserted value: {value} to key {key}")

    # Inserting a value to the hash table:
    # The hash() function is used to get the key for the value.
    # If the slot in the hash table is empty the value is inserted there
    # if not the collision() function is called to handle the collision.
    def insert(self, value):

        # Timer for measuring the time it takes to insert a value
        starttime = timeit.default_timer()

        key = self.hash(value)
        if self.table[key] == None:
            self.table[key] = Node(value)
            print(f"Inserted value: {value} to key {key}")
        else:
            self.collision(key, value)
    
        print("The insert took", timeit.default_timer() - starttime)

    # Deleting a value from the hash table:
    # Works the same way as the search() function just that we keep track of the previous node.
    # If the value is found we can delete it by changing the pointer of the previous node to the next node.
    def delete(self, value):

        # Timer for measuring the time it takes to delete a value
        starttime = timeit.default_timer()

        key = self.hash(value)
        node = self.table[key]
        previousNode = None
        while node != None:
            if node.value == value:
                if previousNode == None:
                    self.table[key] = node.next
                else:
                    previousNode.next = node.next
                print(f"Deleted value: {value}")
                print("The delete took", timeit.default_timer() - starttime)
                return
            previousNode = node
            node = node.next
        print(f"{value} not found")


    # Printing the hash table:
    # We go trough the table with the for loop and for each slot 
    # we print the values in the linked list until we reach the end of the list.
    def print(self):
        print()
        print("Hash table:")
        for i in range(self.size):
            print("[", end="")
            node = self.table[i]
            while node != None:
                print(node.value, end=" ")
                node = node.next
            print("]", end="")
        print()

    # Searching for a value in the hash table:
    # Fist we need the key for the value to speedup the search this is gotten with the hash() function.
    # Then we can start going trough the linked list in the slot in the hash table until we find the value.
    # If the value is not found we print "value not found".
    def search(self, value):

        # Timer for measuring the time it takes to search for a value
        starttime = timeit.default_timer()

        key = self.hash(value)
        node = self.table[key]
        while node != None:
            if node.value == value:
                print(f"Found value: {value}")
                print("The search took", timeit.default_timer() - starttime)
                return
            node = node.next
        print(f"{value} not found")

        print("The search took", timeit.default_timer() - starttime)

# Testing the hash table:
if __name__ == "__main__":
    table = HashTable(3)
    table.insert(12)
    table.print()
    table.insert('hashtable')
    table.print()
    table.insert(1234)
    table.print()
    table.insert(4328989)
    table.print()
    table.insert('BM40A1500')
    table.print()
    table.insert(-12456)
    table.print()
    table.insert('aaaabbbbcccc')
    table.print()
    table.search(-12456)
    table.search('hashtable')
    table.search(1235)
    table.print()
    table.delete('BM40A1500')
    table.delete(1234)
    table.delete('aaaabbbbcccc')
    table.print()