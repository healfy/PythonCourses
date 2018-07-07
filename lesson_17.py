# from PIL import Image, ImageFont
# from PIL.ImageDraw import ImageDraw


# image1 = Image.open('background.jpg')
# width = 750
# ratio = (width / float(image1.size[0]))
# height = int((float(image1.size[1]) * float(ratio)))
# new = image1.resize((width, height))
# new.show()

# print(image1.format, image1.size, image1.mode)
# image1.thumbnail((750, 750))
# print(image1.size)
# #new_image = image1.resize((300, 300))
# region = image1.crop((0, 25, 200, 100)) #x1, y1, x2 , y2
# # region = region.transpose(Image.ROTATE_180)
# image2 = Image.open('kosmos_a86.jpg')
# image2.thumbnail((750, 750))
# image2.paste(region, (550, 50, 550 + region.size[0], 50 + region.size[1]))
# draw = ImageDraw(image2)
# font = ImageFont.truetype('arial.ttf', 40)
# draw.text((50, 50), 'privet, haahhmhahah', font=font)
# pixels = image2.load()
# print(pixels[0, 0])
# pixels[0, 0] = (255, 0, 0)
# image2.show()
