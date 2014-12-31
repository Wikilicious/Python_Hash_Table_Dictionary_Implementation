__author__ = 'Thomaz'
import hash_table_dictionary
import random, string

htd = hash_table_dictionary.HashTableMap()

htd.add(1, 'value1')
htd.add('1', 'value2')
htd.add('1', 'new value2')

print "key '1' exists so operation ignored"
print htd.get('1')

htd.insert('1', 'new value2')

print "insert() can add and override if key already exists"
print htd.get('1')

htd.insert(34, 99)
htd.add('Hello', 'World!')


for k, v in htd.get_all():
    print k, v


for i in xrange(0, 1000):
    a = ''.join(random.choice(string.ascii_letters) for i in range(5))
    htd.insert(a, a)

print htd.size()
for k, v in htd.get_all():
    htd.delete(k)
print htd.size()