class image():
	from sys import stdout

	def __init__(self, path, newheight=None):
		'''
		Create an instance of this class passing the path of a image as an argument.
		Instance arguments:
			- width (of astext string)
			- height (of astext string)
			- aspect_ratio (width/height)
			- astext (string that gets printed to the console)
			- name (the name of the image file)
			- display() (pass a file to write to, otherwise sys.stdout)
		'''
		from PIL import Image
		from fractions import Fraction

		__img = Image.open(path)
		__width, __height = __img.size
		__aspect_ratio = __width/__height
		__new_height = int(newheight if newheight else __height)
		__new_width = int(__aspect_ratio * __new_height)
		__img = __img.resize((__new_width, __new_height, ))

		__pixellist = __img.getdata()
		__colourtext = (["\u001b[48;2;" + ";".join(str(__rgb) for __rgb in self.__getRGB(__img, (index % __new_width), ((index - (index % __new_width)) / __new_width))) + "m  \u001b[0m" for index, pixel in enumerate(__pixellist)])
		self.width = __new_width
		self.height = __new_height
		self.aspect_ratio = str(Fraction(self.width, self.height)).replace("/", ":")
		self.astext = "\n".join(["".join(__colourtext[index:index + __new_width]) for index in range(0, self.width * self.height, __new_width)])
		self.name = path.split("/")[-1]

	def display(self, file=stdout):
		print(self.astext, flush=False, file=file)
	
	def __getRGB(self, image, x, y):
		return image.convert('RGB').getpixel((x, y))