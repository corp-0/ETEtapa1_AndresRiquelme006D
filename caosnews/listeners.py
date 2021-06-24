from django.core.cache import cache


def clear_model_cache(sender, *args, **kwargs):
    """
    Clears cached data of models on update or delete.
    :param sender: Model Class triggering this signal.
    :param args: extra arguments
    :param kwargs: extra keyword arguments
    :return: None
    """
    from .models import Publicacion

    if Publicacion.CACHE_KEY in cache:
        cache.delete(Publicacion.CACHE_KEY)