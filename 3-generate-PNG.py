from PIL import Image

import json
#number is the starting place minus one (so should equal zero if you're looking to compile the 1st image)
number = 0 

#range is the number of images to produce
for i in range(1000):

    #update to match your json file name
    f = open('charitable-alien-nft-traits.json',)

    data = json.load(f)

    number += 1
    number_str = str(number)
    #number inside .zfill() is the number of digits that your text should be (i.e 5 means the first value would be '00001')
    zero_filled_number = number_str.zfill(5)

    #replace with the second bracket with the 'keys' in your json file
    x = data[zero_filled_number]['head'].splitlines()[0]
    y = data[zero_filled_number]['eyes'].splitlines()[0]
    z = data[zero_filled_number]['nose'].splitlines()[0]
    q = data[zero_filled_number]['mouth'].splitlines()[0]
    s = data[zero_filled_number]['neck'].splitlines()[0]
    r = data[zero_filled_number]['headshape'].splitlines()[0]
    t = data[zero_filled_number]['glow'].splitlines()[0]
    u = data[zero_filled_number]['background'].splitlines()[0]

    #replace the source path 
    head = Image.open("source/head/head{}.png".format((x))).convert('RGBA')
    eyes = Image.open(("source/eyes/eyes{}.png".format(y))).convert('RGBA')
    nose = Image.open(("source/nose/nose{}.png".format(z))).convert('RGBA')
    mouth = Image.open(("source/mouth/mouth{}.png".format(q))).convert('RGBA')
    neck = Image.open(("source/neck/neck{}.png".format(s))).convert('RGBA')
    headshape = Image.open(("source/headshape/headshape{}.png".format(r))).convert('RGBA')
    glow = Image.open(("source/glow/glow{}.png".format(t))).convert('RGBA')
    background = Image.open(("source/background/background{}.png".format(u))).convert('RGBA')

    #start from the background layer and work towards the front-most layer
    backgroundGlow = Image.alpha_composite(background, glow)
    glowHeadshape = Image.alpha_composite(backgroundGlow, headshape)
    headshapeHead = Image.alpha_composite(glowHeadshape, head)
    headEyes = Image.alpha_composite(headshapeHead, eyes)
    eyesNose = Image.alpha_composite(headEyes, nose)
    noseMouth = Image.alpha_composite(eyesNose, mouth)
    mouthNeck = Image.alpha_composite(noseMouth, neck)

    #adjust your dimensions to your desired dimenions (I used 336 x 336 to match cryptopunks)
    finalImage = mouthNeck.resize((336, 336), Image.NEAREST)
    finalImage.save("myChar/charitableAlien-#{}.png".format(zero_filled_number), "PNG")

