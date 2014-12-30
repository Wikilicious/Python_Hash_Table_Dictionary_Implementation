__author__ = 'Thomaz'
import time
import hash_table_dictionary as ht
import random
import string
from bettertimeit import bettertimeit


inserts = 100000
lookups = 100000
t0 = time.time()
kv = []
for i in xrange(0, inserts):
    kv.append(''.join(random.choice(string.ascii_letters) for i in range(5)))
# print kv


create_dt = time.time() - t0
print 'create dt', create_dt

t1 = time.time()
def hasht():
    d = ht.HashTableMap()
    for item in kv:
        d.insert(item, item)
    for i in range(0, lookups):
        a = d.get(kv[i])

# q = hasht()
print 'bti', bettertimeit(hasht)
ht_dt = time.time() - t1

print 'HT dt', ht_dt

t2 = time.time()
dic = {}
for item in kv:
    dic[item] = item


for i in range(0, lookups):
    b = dic.get(kv[i])
d_dt = time.time() - t2

print 'Dic dt:', d_dt
print ht_dt / d_dt, 'X faster'


# # list
# t3 = time.time()
# li = []
# for it in kv:
#     li.append([it, it])
# for i in range(0, lookups):
#     for item in li:
#         if item[0] == kv[i]:
#             pass
# li_dt = time.time() - t3
# print 'li dt:', li_dt
#
# print 'hashT', li_dt / ht_dt, 'X faster than li'

