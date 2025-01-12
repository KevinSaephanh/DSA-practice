class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index]
        return None

    def keys(self):
        my_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    my_keys.append(self.data_map[i][j])
        return my_keys

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = ((my_hash + ord(letter) * 23)) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i}: {val}")


my_hash_table = HashTable()
my_hash_table.set_item("hello", 123)
my_hash_table.set_item("world", 1234)
my_hash_table.set_item("HELLO WORLD", 12345)
print(my_hash_table.get_item("HELLO WORLD"))
print(my_hash_table.get_item("HELLO123"))
my_hash_table.print_table()
