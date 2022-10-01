x = "madam arora teaches us malayalam"
y=x.split()
for i in y:
    if i == i[::-1]:
        print(i)
        print(len(i))