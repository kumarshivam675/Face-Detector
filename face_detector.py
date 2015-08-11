'''
Created on 10-Nov-2013

@author: raghavan
'''
import os

from color import Color
from pyimage import PyImage
from graph import Graph

class FaceDetector(object):
    '''
    classdocs
    '''

    def __init__(self, filename, block_size = 5, min_component_size = 10, majority = 0.5):
        '''
        Constructor - keeps input image filename, image read from the file as a PyImage object, block size (in pixels),
        threshold to decide how many skin color pixels are required to declare a block as a skin-block
        and min number of blocks required for a component. The majority argument says what fraction of
        the block pixels must be skin/hair colored for the block to be a skin/hair block - the default value is
        0.5 (half).
        '''
        # Your code

    def skin_green_limits(self, red):
        '''
        Return the limits of normalized green given the normalized red component as a tuple (min, max)
        '''
        return ((-0.776*red*red + 0.5601*red + 0.18), (-1.376*red*red + 1.0743*red + 0.2))


    def is_skin(self, pixel_color):
        '''
        Given the pixel color (as a Color object) return True if it represents the skin color
        Color is skin if hue in degrees is (> 240 or less than or equal to 20) and 
        green is in the green limits and it is not white
        '''
        # Your code


    def is_hair(self, pixel_color):
        '''
        Return True if the pixel color represents hair - it is if intensity < 80 and ((B-G)<15 or (B-R)<15 or
        hue is between 20 and 40)
        '''
        # Your code


    def is_skin_hair_block(self, block, block_type):
        '''
        Return true if the block (given by the argument 'block' which is the coordinate-tuple for the top-left corner)
        is a skin/hair-block - it is if a majority (as per the threshold attribute) of the pixels in the block are
        skin/hair colored. 'block_type' says whether we are testing for a skin block ('s') or a hair block ('h).
        '''
        # Your code


    def add_neighbour_blocks(self, block, graph):
        '''
        Given a block (given by the argument 'block' which is the coordinate-tuple for the top-left corner)
        and a graph (could be a hair or a skin graph), add edges from the current block to its neighbours
        on the image that are already nodes of the graph
        Check blocks to the left, top-left and top of the current block and if any of these blocks is in the
        graph (means the neighbour is also of the same type - skin or hair) add an edge from the current block
        to the neighbour.
        '''
        # Your code


    def make_block_graph(self):
        '''
        Return the skin and hair graphs - nodes are the skin/hair blocks respectively
        Initialize skin and hair graphs. For every block if it is a  skin(hair) block
        add edges to its neighbour skin(hair) blocks in the corresponding graph
        For this to work the blocks have to be traversed in the top->bottom, left->right order
        '''
        # Your code


    def find_bounding_box(self, component):
        '''
        Return the bounding box - a box is a pair of tuples - ((minx, miny), (maxx, maxy)) for the component
        Argument 'component' - is just the list of blocks in that component where each block is represented by the
        coordinates of its top-left pixel.
        '''
        # Your code
    
    
    def skin_hair_match(self, skin_box, hair_box):
        '''
        Return True if the skin-box and hair-box given are matching according to one of the pre-defined patterns
        '''
        # Your code


    def detect_faces(self):
        '''
        Main method - to detect faces in the image that this class was initialized with
        Return list of face boxes - a box is a pair of tuples - ((minx, miny), (maxx, maxy))
        Algo: (i) Make block graph (ii) get the connected components of the graph (iii) filter the connected components
        (iv) find bounding box for each component (v) Look for matches between face and hair bounding boxes
        Return the list of face boxes that have matching hair boxes
        '''
        # Your code
    
    
    def mark_box(self, box, color):
        '''
        Mark the box (same as in the above methods) with a given color (given as a raw triple)
        This is just a one-pixel wide line showing the box.
        '''
        # Your code


    def mark_faces(self, marked_file):
        '''
        Detect faces and mark each face detected -- mark the bounding box of each face in red
        and save the marked image in a new file
        '''
        # Your code

if __name__ == '__main__':
    detect_face_in = FaceDetector('images/faces-11.jpeg')
    detect_face_in.mark_faces('images/faces-11-marked.jpeg')
