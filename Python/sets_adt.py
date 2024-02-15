my_set = set()
set_2 = set()
my_set.add(1)
my_set.add(3)
my_set.update([3,4,5])
# my_set.remove(3)

set_2.update([2,3,4,5,6,6,7])
for element in my_set:
    print(element, end="--")
print("\n")
for element in set_2:
    print(element, end="--")

symdiff = set_2 ^ my_set
diff = set_2 - my_set
union = set_2 | my_set
intersect = set_2 & my_set

print(f"\nsymmetric diff: {symdiff}, difference: {diff}, union: {union},intersect: {intersect}")
