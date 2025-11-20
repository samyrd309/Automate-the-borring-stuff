import time, sys
ident = 0 # How many spaces to ident.
identIncreasing = True # Whether the identation is increasing or not.

try:
    while True: #The main program loop.
        print(' ' * ident, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if identIncreasing: 
            # Increase the numer of spaces:
            ident = ident + 1
            if ident == 20:
                #Change direction:
                identIncreasing = False

            else:
                # Decrease the number of spaces:
                ident = ident - 1
                if ident == 0:
                    #Change direction:
                    identIncreasing = True
except KeyboardInterrupt:
    sys.exit()