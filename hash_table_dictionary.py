# -*- coding: utf-8 -*-
__author__ = 'Thomaz Lago Santana'
import warnings


class HashTableMap(object):
    """A custom dictionary (key value pair) implementation using hash tables.
    Constructor **kwargs:
        'warnings' - Boolean, default: False, prints warnings
        'auto_rehash' - Boolean, default: True, dynamically rehashes
        'load_factor' - float, default: 0.66, threshold to rehash
        'buckets' - int, default: 211, number of hash tables

    Functions:
        .size()
        .rehash()
        .get()
        .add()
        .insert()
        .get_all()
        .get_all_raw()
        .delete()
        .pop()
        .get_num_buckets()
    """
    def __init__(self, **kwargs):
        self.warnings = kwargs.pop('warnings', False)
        self.auto_rehash = kwargs.pop('auto_rehash', True)
        self.load_factor = kwargs.pop('load_factor', 0.66)
        self.__list_size = 0
        self.__buckets = kwargs.pop('buckets', 211)
        self.__list = []
        for i in range(0, self.__buckets):
            self.__list.append([])

    def __check_load_factor(self):
        if self.auto_rehash:
            current_load = self.__list_size / float(self.__buckets)
            if current_load > self.load_factor and self.__list_size > 100:
                buckets = self.__list_size * 3 + 1
                self.rehash(buckets)
            elif current_load < self.load_factor / 7.0 and self.__list_size > 100:
                buckets = self.__list_size * 2 + 1
                self.rehash(buckets)

    def __generate_new_list(self):
        self.__list = []
        self.__list_size = 0
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

    def __add(self, key, value, hash_key):
        self.__list[hash_key].append([key, value])
        self.__list_size += 1

    def size(self):
        """Get the size of the dictionary.

        :returns: The size.
        """
        return self.__list_size

    def rehash(self, buckets):
        """Rehashes the table with a new size.

        :param buckets: (int) Number to tables to hash to.
        """
        if type(buckets) is not int:
            pass
        else:
            temp_data = self.__list
            if self.warnings:
                print 'Rehashing from %s to %s buckets' % (self.__buckets, buckets)
            self.__buckets = buckets
            self.__generate_new_list()
            for bucket_list in temp_data:
                for key, value in bucket_list:
                    hash_key = self.__get_hash_key(key)
                    self.__add(key, value, hash_key)

    def get(self, key):
        """Get the value of a key.

        :param key: The key of the value to get.
        :returns: The value.
        """
        hash_key = self.__get_hash_key(key)
        if hash_key is None:
            return None
        else:
            return self.__get(key, hash_key)

    def add(self, key, value):
        """Add key-value pair and ignores operation if key already exists.

        :param key: The key.
        :param value: The data to store.
        """
        hash_key = self.__get_hash_key(key)
        if hash_key is None:
            pass
        elif self.__get(key, hash_key) is None:
            self.__add(key, value, hash_key)
            self.__check_load_factor()
        elif self.warnings:
            warnings.warn('Key already exists. Operation ignored.')

    def insert(self, key, value):
        """Inserts key-value pair and overrides value if key already exists.

        :param key: The key.
        :param value: The data to store.
        """
        hash_key = self.__get_hash_key(key)
        if hash_key is None:
            pass
        elif self.__get(key, hash_key) is None:
            self.__add(key, value, hash_key)
            self.__check_load_factor()
        else:
            for b_list in self.__list[hash_key]:
                if b_list[0] == key:
                    b_list[1] = value

    def get_all(self):
        """Generator object. Get key value pairs. Warning: Don't use any methods that mutates the data e.g. delete()
        Use get_all_raw() to iterate and mutate the data.

        :yields: Generator object.
        """
        for bucket_list in self.__list:
            for key_value in bucket_list:
                yield key_value

    def get_all_raw(self):
        """Get the full list of key value pairs.

        :returns: The whole list of key value pairs.
        """
        raw_list = []
        for bucket_list in self.__list:
            for key_value in bucket_list:
                raw_list.append(key_value)
        return raw_list

    def delete(self, key):
        """Deletes a key value pair if it exists

        :param key: The key of the value to delete.
        """
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
                self.__list_size -= 1

    def pop(self, key):
        """Get the value of a key and delete the key value pair.

        :param key: The key of the value to get and delete.
        :returns: The value.
        """
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

    def get_num_buckets(self):
        """Get the number of hash tables.

        :returns: The number of hash tables.
        """
        return self.__buckets

