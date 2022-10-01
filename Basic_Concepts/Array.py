# import array
import array as arr
a = arr.array('d',[1.1,2.1,3.1,4.1,5.1])
b = arr.array('i',[1,2,3,4,5])
print(a)
print(b)
print(b[4])

# append an element-----------
a.append(6.1)
b.append(6)

print(a)
print(b)

# extend (add many element)-----------
a.extend([6.1,7.1,8.1])
b.extend([6,7,8])

print(a)
print(b)

# insert an element at any index-------------
a.insert(5,9.1)
b.insert(5,9)

print(a)
print(b)

# finding length of an array----------------
print(len(a))
print(len(b))

# removint element ---------------------
# "pop()" function will return the removed element but "remove()" will not return --------
print("Popping last element",a.pop())
print("Popping last element",b.pop())

print("poppint 5th element",a.pop(4))
print("poppint 5th element",b.pop(4))

a.remove(2.1)
b.remove(2)

print(a)
print(b)

# concatinate a new array------------
c = arr.array('i',[11,12,13,14,15])
d = b+c
print("after concatinate\n",d)


# array slicing------------------
print("Array slicing from 0 to 4",a[0:4])
print("Array slicing from 0 to 4",b[0:4])
print("Array slicing from 0 to end",a[0:])
print("Array slicing from 0 to end",b[0:])