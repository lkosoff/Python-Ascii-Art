# Python-Ascii-Art
This project converts any image into ascii characters
# Overview
I was inspired to do some creative coding and creaeate a program that can generate ascii art from any image. The average grayscale value of an area of the image is calculated and then mapped to an ascii character. Each row of pixles is convereted to a row of ascii characters and the results are stored in a text file. Because there are so many characters per a row, the results are best seen when the font is smallest and the file is zommed out.

The main function takes three arguments, 
```
main(filename,outname, resolution)
```
The _filename_ is the path of the original image, the _outname_ is the name of the text file to be generated, and the _resolution_ is proportional to the area of the image that is averaged.  

# Screenshoots

Original image:
![alt text](https://github.com/lkosoff/Python-Ascii-Art/blob/main/readmeImages/cookie_monster.jpeg?raw=true)

Zoomed out generated text file:
![alt text](https://github.com/lkosoff/Python-Ascii-Art/blob/main/readmeImages/ascii_screenshot.png?raw=true)

Zoomed in section of generated text file:
![alt text](https://github.com/lkosoff/Python-Ascii-Art/blob/main/readmeImages/zoomed_in_screenshot.png?raw=true)
