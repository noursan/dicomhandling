from pydicom import dcmread
from .exceptions import InvalidRotationAngle
from scipy.ndimage import gaussian_filter, rotate

class DcmBase():
    '''
    Base class for dcm file handling using pydicom's reader
    Attributes:
        original: NumPy array with the original image
        ipp: list containing the ImagePositionPatient
    '''
    def __init__(self, path: str) -> None:
        dicom_ds = dcmread(path)
        self.original = dicom_ds.pixel_array
        self.ipp = dicom_ds.ImagePositionPatient

class DcmFilter(DcmBase):
    '''
    Extends DcmBase adding a Gaussian filter operation
    Attributes:
        filtered: NumPy array with the filtered image
    '''
    def __init__(self, path: str, sigma: float = 3) -> None:
        super().__init__(path)
        self.filtered = gaussian_filter(self.original, sigma)

class DcmRotate(DcmBase):
    '''
    Extends DcmRotate adding a rotation operation
    Attributes:
        rotated: NumPy array with the rotated image
    '''
    def __init__(self, path: str, angle: int = 180) -> None:
        if self._is_valid_angle(angle):
            super().__init__(path)
            self.rotated = rotate(self.original, angle)
        else:
            raise InvalidRotationAngle
        
    def _is_valid_angle(angle: int) -> bool:
        return angle%90 == 0

def check_ipp(dcm_1: DcmFilter | DcmRotate, dcm_2: DcmFilter | DcmRotate) -> bool:
    """
    Compare the ImagePositionPatient of two processed dcm images
    """
    return dcm_1.ipp == dcm_2.ipp
