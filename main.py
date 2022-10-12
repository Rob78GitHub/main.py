
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

    for x in range(1, 100, 1):
        print(str(x)+" ",end="")

else:
    print('false!')

input('any key')
