### Layered Art Compiler

Simple code to randomly generate attributes, create CSV/JSON files and compile .PNG layers to create images such as NFTs

## Objective

   - find a way to programmatically generate random attributes and compile images based on those attributes
   - explore csv/json file creation/writing within python


## Download Python

- Download [Python](https://www.python.org/downloads/)
- Install Python and add path
- Install all requirements
- If you dont have pip get pip first
[get-pip.py](https://bootstrap.pypa.io/get-pip.py)
CTRL+S(same folder)
- python3 get-pip.py
- pip install pillow
- pip install -r requirements.txt
- python main.py

## IMAGES

All images use the same dimensions and are saved into the 'source' folder at the individual layer level.

Output files are transformed to 336x336 - these dimensions can be easily adjusted within the code (3-generate-PNG.py)

Naming convention for files should be consisent per type(i.e. mouth1.png, mouth2.png) so that when randomly generated, you can take the # and locate the correct file 

## Steps to use

   1. create your artwork, determine the number of layers and categories

   2. go to 1-generate-attributes-csv.py and use the comments to replicate your set up
        - set up your header columns (one for each layer + # if that's an important element for your project)
        - create variables for each layer (one for the number of options and one of the weight of each option described in the comments)
        - modify the range to match the total number of row you'd like to generate
        - update the ______Value variables with the corresponding layer/layerWeight variables (add/delete the ones you need)
        - update the "writer.writerow()" line with your variables -- include zero_filled_number if applicable
        - highlight all text and run the script, confirm that a csv file is generated
            *note that if you open the csv file in excel, the leading 0's will be erased. To get them back use the formulate "=TEXT(A2, "00000")" where A2 is the cell with your zero-filled number and "00000" represents the number of digits (if you used 4, only use 4 0's here)

   3. move over to 2-csv-to-json.py and update the file names and key (currently '#')
        - the json file name will be whatever you want the file to be called
        - if your first column/key is not '#' then change it in line 19
        - highlight all text and run the script, confirm that a json file is generated
            *you can open this file without issues with leading zeros

   4. open 3-generate-PNG.py
        - update range to match the set of images to generate -- range(1000) would create the first 1000 images from the json file
        - update the json file name to match your json file name
        - adjust your zero_filled_number if required
        - replace the second bracket (per comment in file) with your attribute name
           *add/remove attributes in the same format as necessary
        - replace/update the source path to match your attributes, ensure that the appropriate path is tied to each attribute
        - in the section with the code "Image.alpha_composite..." start from the furthest back layer and build up one layer at a time
            -Example:
                background is furthest back; then glow; then headshape
                Therefore:
                backgroundGlow = Image.alpha_composite(background, glow)
                glowHeadshape = Image.alpha_composite(backgroundGlow, headshape)
                backgroundGlow represents background & glow
                glowHeadshape represents backgroundGlow & headshape (therefore background, glow & headshape)
        
        - in the "finalImage" variable, adjust your dimensions if necessary
        - review the save path, in our example, the zero_filled_number is used in the name of the saved file (and therefore unique)
        - highlight all text and run the script - I recommend starting with only a couple to start (reduce range to a smaller number) to ensure the images are compiling in the way you expect them to. 




## Inspiration 

https://github.com/emirongrr/pixelArt_Generator - Donations - ETH WALLET:0x6Ea3f85086fd11eb81dAbd6D60232230ceAaf830

## Donate

mark et cap: 
ETH wallet - 0xc076a6A9D8486dc4C305E62bbF86252A5c6242B0
BTC wallet - 3EwGQFwWreNH1EnW4uQckGU1526f49WscQ
DOGE wallet - DAmCvhfzmfmgqHvj3oAzSFR2GAK4fpvkbq

Support our charity NFT project - www.mark-et-cap.com/charitable-alien-nft 
    - 50% of all proceeds will go to charity
    - new charity selected by the community each month
    - 1000 new aliens released per month (using this tool!)
