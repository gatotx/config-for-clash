import os

l = os.listdir()
for i in l:
    if(".yaml" in i):
        os.remove(i)