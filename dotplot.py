# plots coordinates as dots
  
from PIL import Image
import numpy as np
# from scipy.ndimage import binary_dilation

lpath = "C:\\Users\\Til\\Desktop\\sp\\"
spath = "C:\\Users\\Til\\Desktop\\"
fn = "t_PiceaAbies_3f.csv"

res = (15360, 15360)

map = np.zeros(res)

for line in open(lpath + fn):
    params = line.split(" ")
    posX = min(max(round(float(params[1])),0),res[0]-1)
    posY = min(max(round(float(params[2])),0),res[1]-1)
    map[posX, posY] = 1

# map = binary_dilation(map, iterations=1).astype(int) # increases dot size

Image.fromarray(np.rot90(map).astype(bool)).save(spath + fn.split(".")[0] + ".png")
