import sys
import pathlib
from PIL import Image

#print(pathlib.Path.cwd())
sourceFolder=pathlib.Path('E:\\udemy\modules\\venv\\ImageConverter\\SampleImages');
targetFolder=pathlib.Path('E:\\udemy\modules\\venv\\ImageConverter\\ConvertedImages');
# if not targetFolder.is_dir():
#     pathlib.Path.mkdir(targetFolder)
# content=pathlib.Path('E:\\udemy\modules\\venv\\ImageConve')
# print(content.is_dir())
#pathlib.Path.mkdir(content)

def processImage(ImgFilePath,filename):
    #print(str(targetFolder)+"\\"+str(filename)+".png")
    img=Image.open(ImgFilePath)
    img.save(str(targetFolder)+"\\"+str(filename)+".png","png")

def startProcessing(sorceFolder,targetFolder):
    if not targetFolder.is_dir():
        pathlib.Path.mkdir(targetFolder)

    for files in sourceFolder.iterdir():

        if (files.suffix == ".jpg" or files.suffix == ".jpeg"):
            modifiedFileName = files.name[0:files.name.find(".")]
            print(files.name.split(".")[0])
            #print(modifiedFileName)
            processImage(files, modifiedFileName)




startProcessing(sourceFolder,targetFolder)

