from django.utils.text import slugify


def unique_slug_generator(instance, title):
    slug = slugify(instance.title)
    model_class = instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1

        slug = f'{slug}-{object_pk}'

    return slug
