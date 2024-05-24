# SPDX-FileCopyrightText: Christian Amsüss and the aiocoap contributors
#
# SPDX-License-Identifier: MIT

"""List of known values for the CoAP "Type" field.

As this field is only 2 bits, its valid values are comprehensively enumerated
in the `Type` object.
"""

from enum import IntEnum

class Type(IntEnum):
    CON = 0 # Confirmable
    NON = 1 # Non-confirmable
    ACK = 2 # Acknowledgement
    RST = 3 # Reset

    def _str_(self):
        return self.name

CON, NON, ACK, RST = Type.CON, Type.NON, Type.ACK, Type.RST

_all_ = ['Type', 'CON', 'NON', 'ACK', 'RST']

# Diccionario para cambiar los valores del tipo de mensaje
custom_type_mapping = {
    Type.CON: 3,  # CON -> 3
    Type.NON: 2,  # NON -> 2
    Type.ACK: 0,  # ACK -> 0
    Type.RST: 1   # RST -> 1
}

def translate_type(message_type):
    return custom_type_mapping.get(message_type, message_type)