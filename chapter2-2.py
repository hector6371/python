#define an int
a = 3
print (type(a))

#define an string
b = '4.6'
print (type(b))

#define a float
c = 5.5
print (type(c))

#adding two floats returns a float, even if it has no decimal value
d = 0.5
e = d+c
print (type(e)) #float

#dividing two ints, returns a float
f = 9
print (type(f/a)) #float

#convert to number
print ('converting to number')
print('converting to int:', type(int(b)))
print('converting to float:',type(float(b)))

#input
g = input( "Write something please")
print ("You wrote: " + g) # same than print("You wrote:", g)