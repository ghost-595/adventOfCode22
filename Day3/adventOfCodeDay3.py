from itertools import islice

def main():
    file = open("input.txt", "r")

    prioritySum = 0

    lines = file.readlines()

    numOfGroups = int((len(lines)+1)/3)

    with open("input.txt", "r") as input:
        for x in range(1,numOfGroups+1):
            group = list(islice(input, 3))

            intersectionSet = set(group[0].strip()).intersection(group[1].strip())
            intersectionSet2 = intersectionSet.intersection(group[2].strip())

            char = list(intersectionSet2)[0]

            print(char)

            if char.isalpha():
                if char.isupper():
                    prioritySum += (ord(char)-38)
                else:
                    prioritySum += (ord(char)-96)
            else:
                print("non-alpha character")


    print("total " + str(prioritySum))

if __name__ == "__main__":
    main()