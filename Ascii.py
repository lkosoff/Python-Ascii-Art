import numpy as np
from PIL import Image, ImageOps
from numpy.lib.function_base import average

#CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1()[]?-_+~<>i!lI;:,\"^`'. "
CHARS = ["@","#","S","%","?","*","+",":",":",",","."]
class Img:
    def __init__(self, fname, boxWidth):
        # open image and get info
        img = Image.open(fname).convert('L')
        img = ImageOps.exif_transpose(img)

        self.img = img

        # half width of box in grid
        self.width, self.height = img.size
        print("SIZE", img.size)

        scale = self.width/self.height
        self.boxHeight = int(boxWidth/scale)
        print("SIZE", boxWidth/scale)


        self.boxWidth = boxWidth
        self.numCols = int(self.width/(self.boxWidth))
        self.numRows = int(self.height/(self.boxHeight))
        print("Height", self.height, "Width", self.width)
        print("Box Height", self.boxHeight, "Box Width", self.boxWidth)       
        
        self.pixels = np.reshape(list(img.getdata()), (self.height,self.width))

        #corner points of grids
        self.gridXY = [[(j*self.boxWidth, i*self.boxHeight) for j in range(self.numCols)] for i in range(self.numRows)]
        self.stringGrid = [["" for _ in range(self.numCols)] for _ in range(self.numRows)]
        

    def averageColorGrid(self,x,y):
        colorSum = 0
        for i in range(self.boxHeight):
            for j in range(self.boxWidth): 
                if (i+y < self.height):
                    if (j+x < self.width):
                        
                        colorSum += self.pixels[i+y][j+x]
        
        average =  colorSum/(self.boxHeight * self.boxWidth)
        return average
    
    def colorToString(self):
        for i in range(self.numRows):
            for j in range(self.numCols):
                x,y  = self.gridXY[i][j]
                aveColor = self.averageColorGrid(x,y)
                self.stringGrid[i][j] = CHARS[int((len(CHARS) - 1)*aveColor/255)]
               

        return list(map(lambda i:  "".join(i), self.stringGrid))



def main(filename,outname, resolution):
    img = Img(filename, resolution)
    newLines = img.colorToString()
    with open(outname+".txt", "w",) as f:
        for line in newLines:
            f.write("%s\n" % line)

#Driver code
if __name__ == "__main__":
    filename = "cookie_monster.jpeg"
    outname = 'ascii_pic'
    resolution = 2
    main(filename,outname, resolution)
