__author__ = 'Thomaz'
import time
import hash_table_dictionary as ht
import random
import string

t0 = time.time()
kv = []
for i in xrange(0, 1000000):
    kv.append(''.join(random.choice(string.ascii_letters) for i in range(4)))

create_dt = time.time() - t0
print 'create dt', create_dt

t1 = time.time()
d = ht.HashTableMap()
for item in kv:
    d.insert(kv, kv)

for i in range(0, 10000):
    d.get(kv[i])

ht_dt = time.time() - t1
print 'HT dt', ht_dt

t2 = time.time()
dic = {}
for item in kv:
    dic[item] = item

for i in range(0, 10000):
    dic.get(kv[i])

d_dt = time.time() - t2
print 'Dic dt:', d_dt


print ht_dt / d_dt, 'X faster'

