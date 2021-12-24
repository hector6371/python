astr = 'holi'
try:
    istr = int(astr)
    print ('Everything went fine')
except:
    istr = -1
    print ('Oops. Can\'t convert value', astr)
print (istr)


