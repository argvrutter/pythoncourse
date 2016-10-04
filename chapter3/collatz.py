def collatz(arg):
    
    while arg != 1:
        if arg % 2 == 0:
        
            arg = arg / 2
            print(int(arg))
            
        else:
        
            arg = (arg * 3) + 1
            print(int(arg))
while True: 
    print('Input an integer.')
    try:
        arg = int(input())
    except ValueError:
        print('Please enter an integer value next time.')
        break

    collatz(arg)


    


