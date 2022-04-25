from ctypes import resize
from PIL import Image

#讀取圖片
img=Image.open('images/COCO.png')

#調整圖片大小
h = 300
w = 200
img.resize((w,h),Image.NEAREST)

charCode = list("$@B%8&WM#*oahkbdpqwmZO0QLCJ7788000666661123UYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")
def getRGBtoGray(r,g,b,c):
    length= len(charCode)

    Gray= int(r*0.299 + g*0.587 + b*0.114)
    u = 256/length
    return charCode[int(Gray/u)]

char=''
for i in range(h):
    for j in range(w):
        char+=getRGBtoGray(*img.getpixel((j,i)))
    char +='\n'
print(char)