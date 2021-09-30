import random
import csv

#choose any file name .csv here
csvFilePath = 'charitable-alien-nft-traits.csv'

#write header row
with open(csvFilePath, 'w', newline='') as file:
        writer = csv.writer(file)
        #replace each with your desired header columns
        writer.writerow(["#", "head", "eyes", "nose", "mouth", "neck", "headshape", "glow", "background"])

number = 0

#create a variable for each layer type, assign a value for each layer
#create a corresponding "weight" for each value i.e. headWeight[0] = 50 - therefore head 1 has a 50/100 chance of occuring where 100 is the
#sum of the integers within the headWeights list (the sum does not have to equal 100)
head = [1, 2]
headWeight = [50, 50]

eyes = [1, 2]
eyesWeight = [25, 75]

nose = [1, 2]
noseWeight = [10, 90]

mouth = [1, 2]
mouthWeight = [60, 40]

neck = [1, 2]
neckWeight = [80, 20]

headshape = [1, 2]
headshapeWeight = [50, 50]

glow = [1, 2]
glowWeight = [95, 5]

background = [1, 2]
backgroundWeight = [50, 50]

#iterate number of instances (change range(xxxx) to desired # of images)
for i in range(100):

    number += 1
    number_str = str(number)
    #number inside .zfill() is the number of digits that your text should be (i.e 5 means the first value would be '00001')
    zero_filled_number = number_str.zfill(5)
    
    #replace with your headers/variable names
    headValue = random.choices(head, k=1, weights = headWeight)
    eyesValue = random.choices(eyes, k=1, weights = eyesWeight)
    noseValue = random.choices(nose, k=1, weights = noseWeight)
    mouthValue = random.choices(mouth, k=1, weights = mouthWeight)
    neckValue = random.choices(neck, k=1, weights = neckWeight)
    headshapeValue = random.choices(headshape, k=1, weights = headshapeWeight)
    glowValue = random.choices(glow, k=1, weights = glowWeight)
    backgroundValue = random.choices(background, k=1, weights = backgroundWeight)

    with open(csvFilePath, 'a', newline='') as file:
        writer = csv.writer(file)
        #if you've changed variables, ensure they are updated here as well, leave [0] to indicate the 'first' result
        writer.writerow([zero_filled_number, headValue[0], eyesValue[0], noseValue[0], mouthValue[0], neckValue[0], headshapeValue[0], glowValue[0], backgroundValue[0]])
