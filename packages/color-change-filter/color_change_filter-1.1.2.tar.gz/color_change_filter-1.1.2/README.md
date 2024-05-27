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

"""
from color_change_filter import *
"""

1. input image
![Alt text](https://drive.google.com/file/d/1_nwdDS7z2xN5Pv4276920SV-g-nFSiHd/view?usp=sharing)
2. select color from input image
![Choice color](https://drive.google.com/file/d/1m5X2APSrvFFYXmA_c-vhM_IishERVuyR/view?usp=sharing)
3. select color from color picker
![Alt text](https://drive.google.com/file/d/12mXDkKKTg0R-gP-eC_zIKIdwZOjJbZ8u/view?usp=sharing)
4. output image
![Alt text](https://drive.google.com/file/d/1dbJIIte8C4Hjbzau6bGbh359qXX7ZiSu/view?usp=sharing)
