def url_convert():
    f = open('input.txt', 'r')
    f2 = open('output.txt','w')
    url_list = []
    i=0
    for (i,line) in enumerate(f) :
        if(i%3==0):
            item = line.replace("\"","")
            print(item)
            url_list.append(item)
            f2.write(item)
        i += 1

    f.close()
    f2.close()
