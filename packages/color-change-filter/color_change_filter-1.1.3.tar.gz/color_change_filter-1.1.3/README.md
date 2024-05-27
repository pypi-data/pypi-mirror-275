## ABOUT
This code can apply a filter to change the selected color to any color.

color_change_CUI(self, image_path,output_path,x,y,rgb)
- image_path: str
- output_path:str
- x:int
- y:int
- rgb:list

color_change_CUI changes the color of the specified pixel to an rgb color

color_change_GUI(self, image_path,output_path)
- image_path:str
- output_path:str

color_change_GUI selects a specified pixel by clicking on it. Also, rgb is selected from the color picker.

## METHOD
color_change_GUI method

```
from color_change_filter import *
C = color_change_filter()
C.color_change_GUI("IMG_3430.jpeg","output.jpg")

```

1. input image
![input image](https://drive.google.com/uc?export=view&id=1_nwdDS7z2xN5Pv4276920SV-g-nFSiHd)

2. select color from input image
![Choice color](https://drive.google.com/uc?export=view&id=1m5X2APSrvFFYXmA_c-vhM_IishERVuyR)

3. select color from color picker
![color picker](https://drive.google.com/uc?export=view&id=12mXDkKKTg0R-gP-eC_zIKIdwZOjJbZ8u)

4. output image
![output image](https://drive.google.com/uc?export=view&id=1dbJIIte8C4Hjbzau6bGbh359qXX7ZiSu)
