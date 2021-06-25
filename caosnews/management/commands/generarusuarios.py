import random

nombres = [
    "Liam", "Olivia", "Noah",
    "Emma", "Oliver", "Ava", "Elijah",
    "Charlotte", "William", "Sophia",
    "James", "Amelia", "Benjamin",
    "Isabella", "Lucas", "Mia",
    "Henry", "Evelyn", "Alexander", "Harper"
]

apellidos = [
    "Smith", "Johnson", "Williams", "Brown",
    "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
    "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson",
    "Anderson", "Thomas", "Taylor", "Moore", "Jackson",
    "Martin", "Lee", "Perez", "Thompson", "White",
    "Harris", "Sanchez", "Clark", "Ramirez", "Lewis",
    "Robinson", "Walker", "Young", "Allen", "King",
    "Wright", "Scott", "Torres", "Nguyen", "Hill",
    "Flores", "Green", "Adams", "Nelson",
    "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"
]

from django.core.management.base import BaseCommand
from caosnews.models import Usuario, Colaborador
from caosnews.tipo_usuario import Tipo


class UsuarioFalso:
    incremental: int
    nombre: str
    apellido: str
    nombre_completo: str
    username: str
    email: str
    tipo: Tipo
    es_colaborador: bool
    foto: str
    rut: str
    fono: str
    direccion: str
    pais: str

    def __init__(self, incremental, es_colab):
        self.incremental = incremental
        self.es_colaborador = es_colab
        self.generar()

    def generar(self):
        self.nombre = random.choice(nombres)
        self.apellido = random.choice(apellidos)
        self.nombre_completo = f"{self.nombre} {self.apellido}"
        self.username = f"{self.nombre}{self.incremental}"
        self.email = f"{self.nombre}{self.apellido}@correo.cl"
        self.tipo = Tipo.COLABORADOR.value if self.es_colaborador else Tipo.EDITOR.value
        self.foto = "foto.jpg"
        self.rut = "99.999.999-9"
        self.fono = "+56990099999"
        self.direccion = "Avenida mi casa 1234"
        self.pais = "Chile"

        return self


class Command(BaseCommand):
    help = "Crea una cantidad de usuarios de prueba"

    def add_arguments(self, parser):
        parser.add_argument('cantidad', type=int)

    def handle(self, *args, **options):
        print("generando usuarios...")
        fakes = []
        usuarios = []
        colabs = []
        for i in range(0, options.get('cantidad', 100)):
            fakes.append(UsuarioFalso(i, random.random() < 0.8))

        for f in fakes:
            u = Usuario(username=f.username, email=f.email, tipo_usuario=f.tipo)
            u.set_unusable_password()
            usuarios.append(u)

        Usuario.objects.bulk_create(usuarios)
        usuarios = Usuario.objects.all()

        for index, f in enumerate(fakes):
            if f.es_colaborador:
                c = Colaborador(
                    user=usuarios[index],
                    rut=f.rut,
                    foto=f.foto,
                    nombre=f.nombre_completo,
                    fono=f.fono,
                    direccion=f.direccion,
                    pais=f.pais
                )

                colabs.append(c)

        Colaborador.objects.bulk_create(colabs)
