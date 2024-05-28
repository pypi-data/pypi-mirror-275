from enum import StrEnum, auto

class ImplMissing(StrEnum):
    @classmethod
    def _missing_(cls, value: str):
        value = value.lower()
        for member in cls:
            if member == value:
                return member
        return None

class ReceivePay(ImplMissing):
    """
    Representa el tipo de pata de la operación, el cual puede ser Activo (Receive) o Pasivo (Pay).
    """

    RECEIVE = auto()
    PAY = auto()

class Product(ImplMissing):
    """
    Representa los tipos de productos que procesa el sistema.

    Los tipos soportados son: ``ICP``=Swap Cámara, ``CCS``=Cross Currency UF/CLP, ``BASIS``=Basis USD/CLP.
    """

    ICP = auto()
    CCS = auto()
    BASIS = auto()

class Bank(ImplMissing):
    """
    Listado de bancos locales validos para el sistema.
    """

    BICE = auto()
    ESTADO = auto()
    SECURITY = auto()
    SANTANDER = auto()
    FALABELLA = auto()
    INTERNACIONAL = auto()