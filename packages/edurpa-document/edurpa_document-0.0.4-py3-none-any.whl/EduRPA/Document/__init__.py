name = 'edurpa_document'
from .DocumentAutomation import *
from .transform import *

from robotlibcore import DynamicCore

class Document(DynamicCore):
    def __init__(
        self, lang, performance, *args, **kwargs
    ):
        # Register keyword libraries to LibCore
        libraries = [
            DocumentAutomation(self, lang, performance, *args, **kwargs)
        ]
        super().__init__(libraries)