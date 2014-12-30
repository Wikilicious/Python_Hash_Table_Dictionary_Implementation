Python_Hash_Table_Dictionary_Implementation
===========================================

A custom dictionary (key value pair) implementation in Python using hash tables.

<hr>
<b>Example Usage:</b>
import hash_table_dictionary


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
    
  <hr>
  <b>Constructor **kwargs:</b>
        'warnings' - Boolean, default: False, prints warnings
        'auto_rehash' - Boolean, default: True, dynamically rehashes
        'load_factor' - float, default: 0.66, threshold to rehash
        'buckets' - int, default: 211, number of hash tables

    <b>Functions:</b>
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
