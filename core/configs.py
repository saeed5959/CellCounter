

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
        self.kernel_size:int = 3
        self.in_channels:int = 3
        self.filtes:list = [16,32,64]
        self.linear_dim:int = 512
        self.n_category:int = 5
        self.epochs:int = 500
        self.batch_size:int = 8
        self.lr:int = 1e-10
        
class WbcSegmentConfig:
    """
        WBC segmentation config
    """

    def __init__(self):
        self.threshold: int = 50
        self.kernel: int = 13
        self.boundary: int = 5000        