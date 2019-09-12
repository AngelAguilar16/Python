import os

EXT_AUDIO = ['.wav', '.mp3', '.raw', '.wma', '.m4a']
EXT_VIDEO = ['.mp4', '.m4v', '.f4v', '.m4b', '.m4r', '.f4b', '.mov', '.avi', '.wmv', '.flv']
EXT_IMAGES = ['.jpeg', '.png', '.svg', '.gif', '.bmp']
EXT_DOCUMENTS = ['.txt', '.pdf', '.doc', '.docx', '.odt', '.html']

os.chdir("Downloads");

print("Automatizacion de limpieza de descargas")
print("Current directory {}".format(os.getcwd())
print()

files = os.listdir()

DIRS = ["Audio", "Video", "Images", "Documents", "Folders", "Other"]

if not os.path.isdir("./Audio"):
    for d in DIRS:
        os.mkdir("./{}".format(d))

    print("Directorios creados")


for f in files:
    name, extension = os.path.splitext(f)

    if extension in EXT_IMAGES:
        print("Image: {}{}".format(name, extension))
    elif extension in EXT_AUDIO:     
        print("Image: {}{}".format(name, extension))
    elif extension in EXT_VIDEO: 
        print("Video: {}{}".format(name, extension))
    elif extension in EXT_DOCUMENTS:
        print("Document: {}{}".format(name, extension))
    else:
        if os.path.isdir(name):
            if name not in DIRS:
                print("Folder (other): {}".format(name))
            else:
                print("Folder (script): {}".format(name))
        else:
            print("Some other file {}{}".format(name, extension))
        

