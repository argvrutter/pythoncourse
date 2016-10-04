def spam():
    global eggs
    eggs = 'spam' #dis global

def bacon():
    eggs = 'bacon' #dis local

def ham():
    print(eggs) #dis da global

eggs = 42 # dis also global
spam()
print(eggs)
