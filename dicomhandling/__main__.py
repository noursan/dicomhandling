import sys
import os

from cv2 import imwrite, subtract, convertScaleAbs
from .dicomhandling import DcmFilter, check_ipp
from .exceptions import IncorrectNumberOfImages, SameImagePositionPatient

if __name__ == '__main__':
    
    # Count files in dir while avoiding subdirectories in file count
    dir = sys.argv[1]
    img_files = next(os.walk(dir))[2] 
    num_files = len(img_files)

    # Raise error if number of image files is different from two
    if num_files != 2:
        raise IncorrectNumberOfImages

    # Filter the images with a Gaussian blur
    imgs = [DcmFilter(os.path.join(dir, img_file), sigma = 3) for img_file in img_files]
    
    # Check if images share the same IPP
    if check_ipp(imgs[0], imgs[1]):
        raise SameImagePositionPatient
    
    # Use OpenCV to avoid overflows arithmetic in subtraction
    unfiltered_residue = subtract(imgs[0].original, imgs[1].original)
    filtered_residue = subtract(imgs[0].filtered, imgs[1].filtered)

    # Scale result to have 255 as max
    scaled_unfiltered_residue = convertScaleAbs(unfiltered_residue, alpha=255/unfiltered_residue.max())
    scaled_filtered_residue = convertScaleAbs(filtered_residue, alpha=255/filtered_residue.max())

    # Write the scaled filtered and unfiltered residues in the residues folder
    dir_residues = os.path.join(dir, 'residues')
    if not os.path.exists(dir_residues):
        os.mkdir(dir_residues)
    imwrite(os.path.join(dir_residues, 'unfiltered_residue.jpg'), scaled_unfiltered_residue)
    imwrite(os.path.join(dir_residues, 'filtered_residue.jpg'), scaled_filtered_residue)
