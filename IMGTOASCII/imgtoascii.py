import numpy as np
import json
from PIL import Image
img = Image.open('download.jfif')
iarr = np.array(img)
HUE = "Ñ@#W$9876543210!abc;:+=-,._        "
l = len(HUE)
brightness = 0
char_hue = ""
s = ""
for row in iarr:
    for col in row:
        brightness = ((col[0] + col[1] + col[2])/3)/255 # in percentage
        char_hue = round(brightness*l)
        if HUE[::-1][char_hue] == " ":
            s+= "&nbsp"
        else:s += HUE[::-1][char_hue]
    s += "<br>"
json_img = {"img": s}
jsonfile = open("data.json","w")
jsonfile.write(json.dumps(json_img))
jsonfile.close()

