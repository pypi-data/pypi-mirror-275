name = 'edurpa_document'
from .DocumentAutomation import *
from .transform import *

from robotlibcore import DynamicCore
from robot.libraries.BuiltIn import BuiltIn
class Document(DynamicCore):
    def __init__(
        self, lang, performance, **kwargs
    ):
        # Register keyword libraries to LibCore
        kwargs = {
            "dryrun": BuiltIn().dry_run_active
        }
        
        libraries = [
            DocumentAutomation(lang, performance, **kwargs)
        ]
        super().__init__(libraries)