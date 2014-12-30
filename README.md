Python Hash Table Dictionary Implementation
===========================================

A custom dictionary (key value pair) implementation in Python using hash tables.
Uses a load factor threshold for dynamic rehashing.

<hr>
<b>Example Usage:</b><br>

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
<b>Constructor **kwargs:</b><br>
'warnings' - Boolean, default: False, prints warnings<br>
'auto_rehash' - Boolean, default: True, dynamically rehashes<br>
'load_factor' - float, default: 0.66, threshold to rehash<br>
'buckets' - int, default: 211, number of hash tables<br>

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

