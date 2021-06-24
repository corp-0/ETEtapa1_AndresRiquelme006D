import random

contenidos = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
    "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
    "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure "
    "dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
    "mollit anim id est laborum. ",
    "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque "
    "laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi "
    "architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas "
    "sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione "
    "voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit "
    "amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut "
    "labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, "
    "quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea "
    "commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit "
    "esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas "
    "nulla pariatur? ",
    "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium "
    "voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint "
    "occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt "
    "mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et "
    "expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque "
    "nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas "
    "assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis "
    "debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et "
    "molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, "
    "ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus "
    "asperiores repellat. ",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor "
    "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
    "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure "
    "dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
    "mollit anim id est laborum. "

]
animales = [
    "Capibara",
    "Fénec",
    "Ajolote",
    "Petauro del azúcar",
    "Gineta",
    "Erizo",
    "Langosta azul de Florida",
    "Kinkajú",
    "Zorro",
    "Mofeta",
    "Perro",
    "Gallo",
    "Gato",
    "Vaca",
    "Toro cebú",
    "Cabra",
    "Cerdo",
    "Oveja",
    "Cuy",
    "Burro",
    "Pato",
    "Caballo",
    "Dromedario",
    "Gusano de seda",
    "Paloma",
    "Camello",
    "Llama",
    "Alpaca",
    "Gallina de Guinea",
    "Turón",
    "Ratón casero",
    "Tórtola rosigris",
    "Pavo",
    "Pez carpa",
    "Rata doméstica",
    "Canario",
    "Pez guppy o pez millón",
    "Abeja doméstica",
    "Pato criollo",
    "Pavo real",
    "Cacatúa",
    "Guacamaya",
    "Tortuga de tierra",
    "Cisne",
    "Periquito australiano",
    "Mosca de la fruta",
    "Capibara, chigüire o carpincho",
    "Hámster",
    "Tortuga de orejas rojas",
    "Loro"
]
adjetivos = [
    "complicado",
    "sencillo",
    "inesperado",
    "dulce",
    "agrio",
    "inimaginable",
    "rústico",
    "frágil",
    "preferible",
    "dicho",
    "ameno",
    "crítico",
    "trágico",
    "cierto",
    "falso",
    "premiado",
    "facturado",
    "dirigido",
    "seguro",
    "bonito",
    "seco",
    "derecho",
    "justo",
    "plausible",
    "cálido",
    "fino",
    "elegante",
    "usado",
    "nuevo",
    "perdido",
    "egoísta",
    "enorme",
    "alto",
    "típico",
    "alternativo",
    "maduro",
    "feliz",
    "diestro",
    "apasionado",
    "estirado",
    "cocido",
    "hablado",
    "ambicioso",
    "amable",
    "ágil",
    "celoso",
    "distintivo",
    "duradero",
    "cautivador",
    "complicado",
    "salado",
    "ordenado",
    "alterado",
    "consistente",
    "pasado",
    "futuro",
    "problemático",
    "sugerente",
    "agridulce",
    "líquido",
    "espeso",
    "ruidoso",
    "silencioso",
    "animado",
    "concreto",
    "subjetivo",
    "árido",
    "convincente",
    "vanidoso",
    "rugoso",
    "sospechoso",
    "declarado",
    "pronosticado",
    "presionado",
    "oculto",
    "supervisado",
    "encontrado",
    "incierto",
    "ordenado",
    "cambiado",
    "prensado",
    "procedente",
    "envuelto",
    "olfateado",
    "terminado",
    "empezado",
    "creado",
    "preferido",
    "cítrico",
    "examinado",
    "tupido",
    "cortado",
    "mejorado",
    "concentrado",
    "azucarado",
    "rígido",
    "estudiado",
    "convenido",
    "cotidiano",
    "interceptado",
]

from django.core.management.base import BaseCommand
from caosnews.models import Colaborador, Publicacion


class Command(BaseCommand):
    help = "Genera una cantidad de noticias que pueden o no estar publicadas"
    autores = Colaborador.objects.all()

    def add_arguments(self, parser):
        parser.add_argument('cantidad', type=int)

    def handle(self, *args, **options):
        print("generando noticias...")
        for i in range(0, options.get('cantidad', 100)):
            self.generar()

    def generar(self):
        titulo = f"{random.choice(animales)} {random.choice(adjetivos)}"
        contenido = random.choice(contenidos)
        autor = random.choice(self.autores)
        publicada = random.random() < 0.8

        noticia = Publicacion(titulo=titulo, contenido=contenido, autor=autor, publicada=publicada)
        noticia.save()

