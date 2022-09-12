'''
1.
Write a python script to sort (assending and descending) a dictionary by value 
input = {0:1,1:2,2:1,3:4,4:3}
output = 
        [(0,0),(2,1),(1,2),(4,3),(3,4)]
        [(3,4),(4,3),(1,2),(2,1),(0,0)]

'''

# x={0:0,1:2,2:1,3:4,4:3}
# l=list(x.items())
# l.sort()
# print("Ascending: ",l)
# t=list(x.items())
# t.sort(reverse=True)
# print("Descending: ",t)




'''
2. Write a python program to remove the nth index character from a non empty string 
input =python 
	 3
output=pyhon
'''

# word = input("Enter your Input : ")
# index = int(input("Enter index to remove Element: "))
# output = word[:index - 1] + word[index : ]
# print(output)





'''
3. use x list as the key and y list as value of z dictionary

input = 
x=[1,2,3,4]
y=[‘sachin’,’sourav’,’rahul’,’dhoni’]
z={1:’sachin’, 2:’sourav’,3:’rahul’,r:’dhoni’]
'''


# size = int(input("Enter size : "))
# dic ={}
# for i in range(size):
#     key = input("Key: ")
#     elem = input("Element: ")
#     dic[key] = elem
# print(dic)




'''
4. 
x={ 10:{‘a’:11},5:{‘b’:21},{7:{‘c’:9},3:{‘d’:15},11:{} }
Considering the above mentioned dictionary suppose
a,b,c,d-> passenger name
10 ( for a) ,5 (for b) ,7 (for c) ,3 (for d), 11 (empty) -> compartment no
11 ( for a) ,21 (for b) ,9 (for c) ,15 (for d) -> seat no of the passenger
Write a python program to  search the compartment no and seat no of any passenger taking the passenger name as input and also display which compartment is empty

input =
                x={ 10: {‘a’:11}, 5:{‘b’:21}, {7:{‘c’:9},3: {‘d’:15}, 11:{}  }
                c
output=
seat no=9
compartment no=7
empty compartment no =11
input=
   x={ 10: {‘a’:11}, 5:{‘b’:21}, {7:{‘c’:9},3: {‘d’:15}, 11:{}  }
   k
output=
passenger name not found
empty compartment no =11
'''



x = {10:{'a':11},5:{'b':21},7:{'c':9},3:{'d':15},11:{} }

empty =[]
bool = 0
ch = input("Enter passenger's Name : ")

for k, dic in x.items():
    if len(dic) == 0:
        empty.append(k)
    elif ch in list(dic.keys()):
            print("compartment no: " + str(k))
            print("seat no: " + str(dic[ch]))
            bool = 1

if (bool == 0):
    print("passenger not found")
    
print("empty compartments : " + str(empty))





