
f = open('input.txt', 'r')
f2 = open('output.txt','w')
url_list = []
i=0
for line in f:
    if(i%3==0):
        item = line.replace("\"","\'").replace("\n",",\n")
        print(item)
        print("i")
        url_list.append(item)
        f2.write(item)
    i += 1

f.close()
f2.close()
