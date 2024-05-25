

from controller.model.TotoConfig import TotoConfig
from controller.model.singleton import singleton

@singleton
class Config(TotoConfig): 
    
    def __init__(self):
        super().__init__()
        
        self.logger.log("INIT", "Configuration loaded!")
        
    def get_api_name(self) -> str:
        return "test-api"