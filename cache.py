import functools
from functools import cache, lru_cache
from cachetools import LRUCache

cache = LRUCache(maxsize=1)



def sample(num):
    print("testing lRU")
    if num in cache:
        print(f"retriving from cache:{num}")
        return cache[num]
    else:
        print("Not in cache ...cacling")
        res=num*num
        cache[num]=res
        return res

    return (num**num)

print(sample(2))
print(sample(3))
print(sample(2))
print(list(cache.items()))

