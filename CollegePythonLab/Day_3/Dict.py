# # 1.--------------------------------
# x = [ 'sachin','sourav','dhoni']
# y = [100,200,300]
# z = dict.fromkeys(x)
# j = 0
# for i in z:
#     z[i] = y[j]
#     j += 1
# print(z) 



# # 2.---------------------------------
x = {1:{'a':10},2:{"b":20},3:{"c":30}}
name = input("Enter name : ")
res = 0
for i in x.values():
    if name in i.keys():
        res =i
        break

if res!=0:
    print("Found :)")
    print(res)
else:
    print("Not Found :( ")