# Generate the Slug Function and check that it will match the old slug or not. 

from django.utils.text import slugify
import string,random

def random_string_generator(N):
    res = ''.join(random.choices(string.ascii_uppercase, k = N))
    return res


def random_string_generator_all(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = N))
    return res

def slug_generator(text):
    from main.models import SharedFiles
    slug=slugify(text)
    if SharedFiles.objects.filter(slug=slug).exists():
        text=text+random_string_generator(1)
        return slug_generator(text)
    return slug


def fileid():
    from main.models import SharedFiles
    fileid=random_string_generator_all(1)
    if SharedFiles.objects.filter(fileid=fileid).exists():
        fileid+=random_string_generator_all(1)
    return fileid