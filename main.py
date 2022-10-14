
def welcome(name):
  print("Hello "+name+"!")

def berechne(a,b):
    return(a+b*3*4*6*7)


print('Hallo Welt')
print('1')
print(5*10+3.4)
name = input('Bitte Namen eingeben: ')

#name = 'robert'
alter = 43
print(name+" "+str(33))
mybool=True


if(name=="Robert"):

    print('true!')
    welcome(name)
    ergebnis=berechne(2,3)
    print(ergebnis);


    mylist=["Apfel","Banane","Kirsche"]
    print(mylist)
    print("Länge der List", len(mylist))
    mylist.append("Weintraube")
    print(mylist)
    print("Länge der List",len(mylist))
    mylist.remove("Banane")
    print(mylist)
    print("Länge der List",len(mylist))
    mylist.pop(0)
    print(mylist)
    print("Länge der List", len(mylist))


    for x in mylist:
        print (x)


    for x in range(len(mylist)):
        print(mylist[x])




#    print(mylist[0])
#    print(mylist[0:2])
#    print(len(mylist))

    for x in range(1, 100, 1):
        print(str(x)+" ",end="")

else:
    print('false!')

input('any key')
