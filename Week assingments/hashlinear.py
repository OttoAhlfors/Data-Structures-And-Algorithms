# "sum(ord(ch) for ch in key)" Taken from:
# https://stackoverflow.com/questions/12492137/python-sum-of-ascii-values-of-all-characters-in-a-string

class HashLinear:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key):
        for i in range(self.size):
            if self.table[i] == key:
                return
        i = sum(ord(ch) for ch in key) % self.size
        if self.table[i] == None:
            self.table[i] = key
        else:
            while self.table[i] != None:
                i = (i + 1) % self.size
            self.table[i] = key


    def delete(self, key):
        for i in range(self.size):
            if self.table[i] == key:
                self.table[i] = None

    def print(self):
        if self.table == None:
            print("Empty")
        else:
            for i in range(self.size):
                if self.table[i] != None:
                    print(self.table[i], end=" ")
        print()


if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1