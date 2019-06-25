import os
from xml.dom import minidom

rootDir = './Dataset/Annotations'
classes = []


for dirName, subdirList, fileList in os.walk(rootDir):
    for f in fileList:
        xml = minidom.parse(dirName + "/" + f)
        _class = xml.getElementsByTagName("name")
        classname = _class[0].firstChild.data 
        if classname not in classes:
            print("Appending {} to classes.".format(classname))
            classes.append(classname)
