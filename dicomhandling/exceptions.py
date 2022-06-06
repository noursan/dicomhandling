class IncorrectNumberOfImages(ValueError):
    def __init__(self, message = None):
        if not self.message:
            self.message = 'Incorrect number of images. Aborting.'
        super().__init__(message)


class SameImagePositionPatient(ValueError):
    def __init__(self, message = None):
        if not self.message:
            self.message = 'The DICOM files appear to be the same. Aborting.'
        super().__init__(message)


class InvalidRotationAngle(ValueError):
    def __init__(self, message = None):
        if not self.message:
            self.message = 'Angle must be a multiple of 90°. Aborting.'
        super().__init__(message)