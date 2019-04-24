from PIL import Image
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# Generate character list
ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    """"""
    if alpha == 0:
        return ' '

    # Gray value conversion
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256 + 1.0) / len(ascii_char)
    x = int(gray / unit)
    return ascii_char[x]


if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ''

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))

        txt += '\n'
    print(txt)

    # save file
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)







