from uuid import uuid4

from django.http import HttpResponse, JsonResponse
from django.core.files.storage import default_storage

CURRENT_DOMAIN = 'http://127.0.0.1:8000'

def mainpage(request):
    return HttpResponse('This is the mainpage!')


def savetmceimage(request):
    file = request.FILES.get('file')
    filename = f"tinymce/{uuid4()}/{str(file)}"
    default_storage.save(filename, file)
    return JsonResponse({'location': f"{CURRENT_DOMAIN}/media/{filename}"})
