import random, time, copy
WIDTH = 60
HEIGTH = 20

#create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # create a new column
    for y in range(HEIGTH):
        if random.randint(0,1) == 0:
            column.append('#') # add living cell
        else:
            column.append(' ') # add dead cell
    nextCells.append(column)

while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGTH):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or the space.
        print()

    # Calcualte the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGTH):
            # Get neighborign coordinates:
            # `% WIDTH` ensure left coordinate is always between 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGTH
            belowCoord = (y - 1) % HEIGTH

            # Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.


             # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.