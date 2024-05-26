
from collections import Counter

def mostMember(collection):
    counter = Counter(collection)
    return counter.most_common(1)[0][0]

def find_one(collection, func):
    for item in collection:
        if func(item):
            return item
    return None