__author__ = 'Thomaz Lago Santana'
import warnings


class HashTableMap(object):
    def __init__(self, buckets=997, warnings=False):
        self.warnings = warnings
        self.__buckets = buckets
        self.__list = []
        for i in range(0, self.__buckets):
            self.__list.append([])

    def __hash_str(self, key):
        sum_ord = 0
        for letter in key:
            sum_ord += ord(letter)
        return sum_ord % self.__buckets

    def __hash_int(self, key):
        return key % self.__buckets

    def __get_hash_key(self, key):
        if type(key) is str:
            return self.__hash_str(key)
        elif type(key) is int:
            return self.__hash_int(key)
        else:
            if self.warnings:
                message = 'Key type has to be int or str. Key of type %s given.' % type(key)
                warnings.warn(message)
            return None

    def __get(self, key, hash_key):
        for b_list in self.__list[hash_key]:
            if b_list[0] == key:
                return b_list[1]
        return None

    def get(self, key):
        hash_key = self.__get_hash_key(key)
        if hash_key is None:
            return None
        else:
            return self.__get(key, hash_key)

    def add(self, key, value):
        """Add key-value pair and ignores operation if key already exists."""
        hash_key = self.__get_hash_key(key)
        if hash_key is None:
            pass
        elif self.__get(key, hash_key) is None:
            self.__list[hash_key].append([key, value])
        elif self.warnings:
            warnings.warn('Key already exists. Operation ignored.')

    def insert(self, key, value):
        """Inserts key-value pair and overrides value if key already exists."""
        hash_key = self.__get_hash_key(key)
        if hash_key is None:
            pass
        elif self.__get(key, hash_key) is None:
            self.__list[hash_key].append([key, value])
        else:
            for b_list in self.__list[hash_key]:
                if b_list[0] == key:
                    b_list[1] = value

    def get_all(self):
        full_list = []
        for bucket_list in self.__list:
            for key_value in bucket_list:
                full_list.append(key_value)
        return full_list


import random, string
d = HashTableMap()

d.add('1', 'number one')
d.insert(2, 'q')
for i in range(0, 10000):
    k = ''.join(random.choice(string.ascii_letters) for i in range(3))
    v = random.randrange(0, 1000)
    d.insert(k, v)



print d.get('1')

for k, v in d.get_all():
    print k, v


