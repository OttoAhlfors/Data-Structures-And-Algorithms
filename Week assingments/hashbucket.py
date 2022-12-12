class HashBucket:
    def __init__(self, size, bucket):
        self.size = size
        self.table = [None] * bucket
        for i in range(bucket):
            b = [None] * int(size / bucket)
            self.table.append(b)
        print(self.table)
        for i in range(int(self.size / 2)):
            print(self.table[i][1])
        

    def insert(self, key):
        for i in range(self.size):
            if self.table[i] == key:
                return
        i = sum(ord(ch) for ch in key) % self.size
        print(key)
        print(i)
        if i > self.numberOfBukets:
            print("Table spot ", self.table[i])
        else:
            print("Bucket spot ", self.table[i])


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
    table = HashBucket(8, 4)
    #table.insert("BM40A1500")
    #table.insert("fOo")
    #table.insert("123")
    #table.insert("Bar1")
    #table.insert("10aaaa1")
    #table.insert("BM40A1500")
    #table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
    #table.delete("fOo")
    #table.delete("Some arbitary string which is not in the table")
    #table.delete("123")
    #table.print()   # BM40A1500 Bar1 10aaaa1