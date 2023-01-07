# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.schema import Attachment


class UserProfile:
    """
      This is our application state. Just a regular serializable Python class.
    """

    def __init__(self, name: str = None, pregunta1: str = None,pregunta2: str = None,pregunta3: str = None,pregunta4: str = None,pregunta5: str = None,pregunta6: str = None,pregunta7: str = None,pregunta8: str = None,pregunta9: str = None,email: str = None):
        self.name = name
        self.email = email
        self.pregunta1 = pregunta1
        self.pregunta2 = pregunta2
        self.pregunta3 = pregunta3
        self.pregunta4 = pregunta4
        self.pregunta5 = pregunta5
        self.pregunta6 = pregunta6
        self.pregunta7 = pregunta7
        self.pregunta8 = pregunta8
        self.pregunta9 = pregunta9
        
        