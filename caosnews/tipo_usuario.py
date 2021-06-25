from enum import Enum


class Tipo(Enum):
    ADMINISTRADOR = 1
    EDITOR = 2
    COLABORADOR = 3


TIPO_CHOICES = [[tipo.value, tipo.name.capitalize()] for tipo in Tipo]



