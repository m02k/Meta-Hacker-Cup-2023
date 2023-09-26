#read file
inputFile = open("input.txt", 'r').readlines()
outputFile = open("output.txt", 'w')




#get cases number
t = int(inputFile[0])#int(input("Enter numbers of cases: "))
#array to store s d and k
inputs = []



#get input for s d and cost
for i in range(t):
    readinputs = inputFile[i+1].split(' ')
    s = int(readinputs[0])#int(input("Enter cost of Single Cheeseburger: "))
    d = int(readinputs[1])#int(input("Enter cost of Double Cheeseburger: "))
    cost = int(readinputs[2])#int(input("Enter cost: "))
    inputs += [[s,d,cost]]
    


#arrays for number of total buns , slices of cheese and patties
buns = []
slices = []
patties = []


    

#main func to check wether decker can be created or not
def createDecker(buns, slices, patties):
    #for range of cases
    for i in range(t):
        #extract int from array for every case
        ibun = buns[i][0]
        islice = slices[i][0]
        ipatties = patties[i][0]

        if ipatties==islice and ibun>islice:
            print("Case #:",i+1," ",islice)
            outputFile.writelines("Case #"+str(i+1)+": "+str(islice)+"\n")
        elif ipatties==islice and ibun==islice and ibun>>0:
            print("Case #:",i+1," ",islice-1)
            outputFile.writelines("Case #"+str(i+1)+": "+str(islice-1)+"\n")
        elif ipatties==islice and ibun<islice:
            print("Case #:",i+1," ", ibun-1)
            outputFile.writelines("Case #"+str(i+1)+": "+str(ibun)-1+"\n")
        else:
            print("Case #:",i+1," ", ibun)
            outputFile.writelines("Case #"+str(i+1)+": "+str(ibun)+"\n")




for i in range(t):
    sb = 0
    db = 0
    if inputs[i][1]<=inputs[i][0]:
        while inputs[i][2]>=1:
            if inputs[i][2]>=inputs[i][1] and inputs[i][2]%inputs[i][1]==0:
                inputs[i][2] = inputs[i][2] - inputs[i][1]
                db += 1
                continue
            elif inputs[i][2]>=inputs[i][0]:
                inputs[i][2] = inputs[i][2] - inputs[i][0]
                sb += 1
                continue
            else:
                break

    if inputs[i][0]<=inputs[i][1]:
        while inputs[i][2]>=1:
            if inputs[i][2]>=inputs[i][0] and inputs[i][2]%inputs[i][0]==0:
                inputs[i][2] = inputs[i][2] - inputs[i][0]
                sb += 1
                continue
            elif inputs[i][2]>=inputs[i][1]:
                inputs[i][2] = inputs[i][2] - inputs[i][1]
                db += 1
                continue
            
            else:
                break

    inputs[i][0] = sb
    inputs[i][1] = db
    

#get numbers of ingredients of s and d
for i in range(t):
    buns += [[inputs[i][0]*2+inputs[i][1]*2]]
    slices += [[inputs[i][0]*1+inputs[i][1]*2]]
    patties += [[inputs[i][0]*1+inputs[i][1]*2]]

createDecker(buns, slices, patties)