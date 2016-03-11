from PIL import Image

def compute_average_image_color(img):
    width, height = img.size

    r_ave = 0
    g_ave = 0
    b_ave = 0

    for x in range(1, width):
        for y in range(1, height):
            r, g, b = img.getpixel((x,y))
            r_ave = (r + r_ave) / 2
            g_ave = (g + g_ave) / 2
            b_ave = (b + b_ave) / 2

    return (r_ave, g_ave, b_ave)

img = Image.open('eikona.jpg')   #https://upload.wikimedia.org/wikipedia/commons/b/b4/JPEG_example_JPG_RIP_100.jpg to exw dokimasei me auth thn eikona.
average_color = compute_average_image_color(img)
print(average_color)
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

print "To pio dimofiles xrwma einai to: "
print rgb_to_hex(average_color)