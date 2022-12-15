

class RbcConfig:
    """
        RBC counting config
    """

    def __init__(self):
        self.threshold: int = 120
        self.boundary_low: int = 10
        self.boundary_up: int = 25
        

class WbcClassifyConfig:
    """
        WBC classify config
    """

    def __init__(self):
        self.threshold: int = 120
        self.low: int = 10
        self.up: int = 25
        
        
class WbcSegmentConfig:
    """
        WBC segmentation config
    """

    def __init__(self):
        self.threshold: int = 120
        self.low: int = 10
        self.up: int = 25        