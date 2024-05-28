name = 'edurpa_document'
from .DocumentAutomation import *
from .transform import *

from robotlibcore import DynamicCore
from robot.libraries.BuiltIn import BuiltIn
class Document(DynamicCore):
    def __init__(
        self, lang, performance, **kwargs
    ):
        self.tolerate = kwargs.get('tolerate', 0.4) 
        
        # Register keyword libraries to LibCore
        kwargs = {
            "dryrun": BuiltIn().dry_run_active
        }
        
        libraries = [
            DocumentAutomation(lang, performance,self.tolerate,**kwargs)
        ]
        super().__init__(libraries)