from PIL import Image
import os, PIL

inputPath = "./withExif/"
outputPath = "./withoutExif/"
content = os.listdir(inputPath)


def get_exif(path):
    exif_table = {}
    image = Image.open(path)
    info = image.getexif()
    for tag, value in info.items():
        decoded = PIL.ExifTags.TAGS.get(tag, tag)
        exif_table[decoded] = value
    return exif_table


for part in content:
    inPath = inputPath + part
    outPath = outputPath + part
    
    if os.path.isfile(inPath):
        inputImg = Image.open(inPath)
        data = list(inputImg.getdata())
        exif = get_exif(inPath)
        rotation = exif['Orientation']

        outputImg = Image.new(inputImg.mode, inputImg.size)
        outputImg.putdata(data)

        if rotation == 2:
            outputImg = outputImg.transpose(Image.ROTATE_90)
        if rotation == 3:
            outputImg = outputImg.transpose(Image.ROTATE_180)
        if rotation == 4:
            outputImg = outputImg.transpose(Image.ROTATE_270)

        outputImg.save(outPath)
        
        inputImg.close()
        outputImg.close()

        print("Cleared {} to {}".format(inPath,outPath))
