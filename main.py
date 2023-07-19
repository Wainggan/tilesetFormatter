from PIL import Image
import os
import math

dir = input("Tileset file location: ")
fileName = False
fileDirectory = False
if os.path.isfile(dir):
    fileName, fileExtention = os.path.splitext(dir)

    fileDirectory = os.path.split(fileName)[0]
    fileName = os.path.basename(fileName)
    print("File found")

    if fileExtention in (".jpg", ".jpeg"):
        print("WARNING: you are using a " + fileExtention + ", which look ugly, use a png instead")
else:
    print("That file doesn't exist!")
    input()
    exit()


originalPic = Image.open(dir)
originalPixels = originalPic.load()

print("Image loaded")

ogImageWidth, ogImageHeight = originalPic.size


tileWidth = math.floor(ogImageWidth / 11)
tileHeight = math.floor(ogImageHeight / 5)
#print(tileWidth, tileHeight)

newImageWidth = tileWidth * (46 + 1)
newImageHeight = tileHeight
#print(newImageWidth, newImageHeight)

def copyFrom(ogImage, targetImage, ogCoord = (0, 0), targetCoord = (0, 0), tileSize=(16, 16)):
    imageBuffer = ogImage.copy()
    ogImageLocation = (ogCoord[0] * tileSize[0], ogCoord[1] * tileSize[1])
    imageBuffer = imageBuffer.crop( ogImageLocation + (ogImageLocation[0]+tileSize[0], ogImageLocation[1]+tileSize[1]) )
    targetImage.paste(imageBuffer, (targetCoord[0] * tileSize[0], targetCoord[1] * tileSize[1]))


openOrder = [
    (3,3), (3,2), (0,3), (4,3), (0,2), (3,0), (3,1), (4,0),
    (0,0), (4,4), (4,1), (4,2), (0,1), (2,3), (7,3), (2,2),
    (1,3), (8,3), (5,3), (6,3), (1,2), (7,0), (2,0), (7,4),
    (7,1), (7,2), (2,1), (8,0), (6,0), (5,0), (1,0), (8,4),
    (10,3), (9,3), (8,1), (9,2), (9,0), (6,4), (6,1), (10,2),
    (5,4), (9,1), (5,1), (8,2), (5,2), (6,2), (1,1)

]



newPic = Image.new(mode="RGBA", size=(newImageWidth, newImageHeight), color=(0,0,0,127))

print("Pasting tiles....")

i = 0
while i < len(openOrder):
    copyFrom(originalPic, newPic, ogCoord=openOrder[i], targetCoord=(i,0), tileSize=(tileWidth,tileHeight))
    #print("Tile " + str(i) + " pasted")
    i += 1


#copyFrom(originalPic, newPic, ogCoord=(0,0), targetCoord=(0,0), tileSize=(tileWidth,tileHeight))
#copyFrom(originalPic, newPic, ogCoord=(1,0), targetCoord=(0,0), tileSize=(tileWidth,tileHeight))

#newPic.show()

newPic.save(fileDirectory + "/" + fileName + "_formatted.png")

print("Finished! Look for '" + fileName + "_formatted.png'")
print("Press Enter to quit")
input()