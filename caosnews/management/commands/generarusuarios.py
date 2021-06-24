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
from caosnews.usuario import Tipo


class Command(BaseCommand):
    help = "Crea una cantidad de usuarios de prueba"
    incremental: int = 0

    def add_arguments(self, parser):
        parser.add_argument('cantidad', type=int)

    def handle(self, *args, **options):
        print("generando usuarios...")
        for i in range(0, options.get('cantidad', 100)):
            self.generar()

    def generar(self):
        self.incremental += 1
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        username = f"{nombre}{self.incremental}"
        email = f"{nombre}{apellido}@correo.cl"
        tipo = Tipo.EDITOR.value
        es_colaborador = random.random() < 0.8
        if es_colaborador:
            tipo = Tipo.COLABORADOR.value

        usuario = Usuario(username=username, email=email, tipo_usuario=tipo)
        usuario.set_password(f"{nombre + apellido[-2:]}{self.incremental * 10}")
        usuario.save()

        if es_colaborador:
            colab = Colaborador(
                user=usuario,
                rut="99.999.999-9",
                nombre=f"{nombre} {apellido}",
                foto="foto",
                fono="569999999",
                direccion="Avenida mi casa 1234",
                pais="Chile"
                )
            colab.save()





