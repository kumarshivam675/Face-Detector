'''
Created on 10-Nov-2013

@author: raghavan
'''

from PIL import Image

class PyImage(object):
    '''
    classdocs
    '''

    def __init__(self, filename):
        '''
        Constructor
        '''
        self.image = Image.open(filename)
        self.pixels = self.image.load()


    def get_rgba(self, pixelx, pixely):
        '''
        Get the rgb values of the pixel at (pixelx, pixely)
        '''
        # Your code
    

    def size(self):
        '''
        Get the size of the image as a tuple (width, height) in pixels
        '''
        return self.image.size


    def set(self, pixelx, pixely, rgb):
        '''
        Check that (x,y) is a valid pixel and set the color of that pixel to rgb
        rgb is a triple (R, G, B) where each component is in the range 0-255
        Setting the color value of a pixel is exactly like reading a pixel value - just that the assignment is reversed 
        '''
        # Your code
        


    def save(self, filename):
        '''
        Save the image (with the modified pixels to a new image with the given filename
        '''
        self.image.save(filename)
    
    