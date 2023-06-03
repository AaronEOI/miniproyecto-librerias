from PIL import Image

img = Image.new("RGB", (256, 256))
img.save("256x256.png")
mapa = img.load()

width, height = 256, 256

for y in range(height):
    for x in range(width):
        r = int(x / width * 255)
        g = int(y / height * 255)
        b = int(x / width * 255)
        img.putpixel((x, y), (r, g, b))
img.save("gradient_image.png")
img.show()
