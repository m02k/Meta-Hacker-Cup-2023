#read file
inputFile = open("input.txt", 'r').readlines()
outputFile = open("output.txt", 'w')




#get cases number
t = int(inputFile[0])#int(input("Enter numbers of cases: "))
#array to store s d and k
inputs = []

#get input for s d and k
for i in range(t):
    readinputs = inputFile[i+1].split(' ')
    s = int(readinputs[0])#int(input("Enter numbers of Single Cheeseburger: "))
    d = int(readinputs[1])#int(input("Enter numbers of Double Cheeseburger: "))
    k = int(readinputs[2])#int(input("Enter numbers of Deckers: "))
    inputs += [[s,d,k]]


#arrays for number of total buns , slices of cheese and patties
buns = []
slices = []
patties = []

#get numbers of ingredients of s and d
for i in range(t):
    buns += [[inputs[i][0]*2+inputs[i][1]*2]]
    slices += [[inputs[i][0]*1+inputs[i][1]*2]]
    patties += [[inputs[i][0]*1+inputs[i][1]*2]]
    
#main func to check wether decker can be created or not
def createDecker(buns, slices, patties):
    #for range of cases
    for i in range(t):
        #extract int from array for every case
        ibun = buns[i][0]
        islice = slices[i][0]
        ipatties = patties[i][0]
        if inputs[i][2]==1:
            if ibun>=inputs[i][2] & islice>>inputs[i][2] & ipatties>>inputs[i][2]:
                print(i+1,"YES")
                outputFile.writelines("Case #"+str(i+1)+": YES\n")
            else:
                print(i+1,"NO")
                outputFile.writelines("Case #"+str(i+1)+": NO\n")
        elif inputs[i][2]>1:
            if (ibun-1)>=inputs[i][2] & islice>=inputs[i][2]  & ipatties>=inputs[i][2]:
                print(i+1,"YES")
                outputFile.writelines("Case #"+str(i+1)+": YES\n")
            else:
                print(i+1,"NO")
                outputFile.writelines("Case #"+str(i+1)+": NO\n")
        else:
            print(i+1,"NO")
            outputFile.writelines("Case #"+str(i+1)+": NO\n")
#run
createDecker(buns, slices, patties)