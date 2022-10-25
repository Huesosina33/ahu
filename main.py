f1=open('Z.txt', 'r')
s = f1.readlines()
numbers = [int(x) for x in s]
print(min(numbers)+max(numbers))
f1.close()