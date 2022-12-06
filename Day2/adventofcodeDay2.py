def main():
    file = open("input.txt", "r")

    totalPoints = 0

    for line in file:

        points = 0

        elf = line.split()[0]
        me = line.split()[1]

        #Rename efl move
        if(elf == 'A'):
            elf = 'R'
        elif (elf == 'B'):
            elf = 'P'
        elif (elf == 'C'):
            elf = 'S'

        #Add points for my move and rename
        if(me == 'X'):
            me = 'L'
            points += 0
        elif (me == 'Y'):
            me = 'D'
            points += 3
        elif (me == 'Z'):
            me = 'W'
            points += 6

        #P L
        
        #Win/draw conditions
        if(elf == 'R'):

            if(me == 'D'): #Play Rock
                points += 1
            elif (me == 'W'): #Play Paper
                points += 2
            elif (me == 'L'): #Play Scissors
                points += 3

        elif(elf == 'P'): 

            if(me == 'D'): #Play Paper
                points += 2
            elif (me == 'W'): #Play Scissors
                points += 3
            elif (me == 'L'): #Play Rock
                points += 1

        elif(elf == 'S'):

            if(me == 'D'): #Play Scissors
                points += 3
            elif (me == 'W'): #Play Rock
                points += 1
            elif (me == 'L'): #Play Paper
                points += 2


        print(points)

        totalPoints += points

    print()
    print(totalPoints)



if __name__ == "__main__":
    main()