

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
        model_dict: dict = file_data.get("model", {})
        self.n_heads: int = model_dict.get("n_heads", 2)
        self.n_layers: int = model_dict.get("n_layers", 6)
        self.resblock: str = model_dict.get("resblock", "1")
        self.p_dropout: float = model_dict.get("p_dropout", 0.1)
        self.n_layers_q: int = model_dict.get("n_layers_q", 3)
        self.kernel_size: int = model_dict.get("kernel_size", 3)
        self.gin_channels: int = model_dict.get("gin_channels", 256)
        self.inter_channels: int = model_dict.get("inter_channels", 192)
        self.upsample_rates: list = model_dict.get("upsample_rates", [8, 8, 2, 2])
        self.filter_channels: int = model_dict.get("filter_channels", 768)
        
        
class WbcSegmentConfig:
    """
        WBC segmentation config
    """

    def __init__(self):
        self.threshold: int = 50
        self.kernel: int = 13
        self.boundary: int = 5000        