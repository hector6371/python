smallest = None
for i in [3, 2, 1, 24, 43, 56, 22, 52]:
    if smallest == None:
        smallest = i
    elif i < smallest:
        smallest = i

print ('The smallest value is', smallest)