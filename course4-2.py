def greet (lang):
    if lang == 'es':
        print ('Hola')
    elif lang == 'en':
        print ('Hello')
    else:
        print ('Bonjour')

greet ('es')
greet ('en')
greet (7)

def returnGreet (lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'en':
        return 'Hello'
    else:
        return 'Bonjour'

print (returnGreet('es'))
