# -*- coding: utf-8 -*-
__author__ = 'Thomaz Lago Santana'
import warnings


class HashTableMap(object):
    def __init__(self, **kwargs):
        self.warnings = kwargs.pop('warnings', False)
        self.__buckets = kwargs.pop('buckets', 7)
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
        elif type(key) is float:
            return self.__hash_str(str(key))
        else:
            if self.warnings:
                message = 'Key type has to be int or str or float. Key of type %s given.' % type(key)
                warnings.warn(message)
            return None

    def __get_index(self, key, hash_key):
        i = 0
        for b_list in self.__list[hash_key]:
            if b_list[0] == key:
                return i
            i += 1
        return None

    def __get(self, key, hash_key):
        index = self.__get_index(key, hash_key)
        if index is None:
            return None
        else:
            return self.__list[hash_key][index][1]

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

    def print_raw(self):
        print self.__list

    def delete(self, key):
        """Deletes a key value pair if it exists"""
        hash_key = self.__get_hash_key(key)
        if hash_key is None:
            pass
        else:
            index = self.__get_index(key, hash_key)
            if index is None:
                if self.warnings:
                    warnings.warn('Key does not exist. Operation ignored.')
            else:
                del self.__list[hash_key][index]

    def pop(self, key):
        """Returns the value of a key and deletes the key value pair."""
        hash_key = self.__get_hash_key(key)
        if hash_key is None:
            return None
        else:
            index = self.__get_index(key, hash_key)
            if index is None:
                if self.warnings:
                    warnings.warn('Key does not exist. Returned None.')
                return None
            else:
                value = self.__list[hash_key][index][1]
                del self.__list[hash_key][index]
                return value

import random, string
d = HashTableMap(warnings=True)

d.add('2.0', 'number one')
d.insert(2.0, 'q')
# for i in range(0, 10000):
#     k = ''.join(random.choice(string.ascii_letters) for i in range(3))
#     v = random.randrange(0, 1000)
#     d.insert(k, v)



print d.get('2.0')
print d.get(2.0)

# for k, v in d.get_all():
#     print type(k)
#     print k, v


d.print_raw()
print d.pop(2.01)
d.print_raw()