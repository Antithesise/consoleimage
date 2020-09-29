from os import get_terminal_size, listdir
from os.path import isfile, join
from time import sleep

from image import image # image.py is made all by me

def clear():
	from os import system
	from sys import platform
	system("cls" if platform == "win32" else "clear") # clears the console

images = {}

while True:
	for imagename in [f for f in listdir("tests/images/") if isfile(join("tests/images/", f))]:
		clear() # clear console

		images[imagename] = image("tests/images/" + imagename, get_terminal_size()[1] - 4) # create instance of image class

		print(images[imagename].name) # print the name of the image in that instance
		images[imagename].display() # print the image
		print(images[imagename].width, images[imagename].height, sep=" x ", end=" (" + str(images[imagename].aspect_ratio) + ")\n") # print the width, height and aspect ratio
		sleep(2) # wait 2 seconds
