import unittest.case

class HashTableSymbolTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def lookup(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None


    def display(self):
        return self.table


class TestHashTableSymbolTable(unittest.TestCase):
    def test_insert_and_lookup(self):
        table = HashTableSymbolTable()
        table.insert(1, 15)
        table.insert(17, 13)
        self.assertEqual(table.lookup(1), 15)
        self.assertEqual(table.lookup(17), 13)

    def test_insert_overwrite(self):
        table = HashTableSymbolTable()
        table.insert(1, 15)
        table.insert(1, 13)
        self.assertEqual(table.lookup(1), 15)

    def test_lookup_nonexistent_key(self):
        table = HashTableSymbolTable()
        self.assertIsNone(table.lookup(31))


if __name__ == '__main__':
    unittest.main()

