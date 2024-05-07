from os import name, getcwd
from time import sleep
from python_imagesearch.imagesearch import imagesearch
dir_path = getcwd()
sep = "/"

if name == "nt":
    from winsound import Beep as bp
    sep = "\\"

    def Beep():
        bp(500, 500)

elif name == "posix":
    from AppKit import NSBeep as Beep
else:
    raise RuntimeError("Unsupported OS")


def main(image):
    Beep()
    while True:
        img_pth = dir_path+sep+"Image_Assets"+sep+image
        pos = imagesearch(img_pth)
        if pos[0] != -1:
            Beep()
        sleep(0.05)

if __name__ == "__main__":
    main("Loaded.PNG")
