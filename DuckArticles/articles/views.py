from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
import json
import tinymce


def mainpage(request):
    return HttpResponse('This is the mainpage!')


def savetmceimage(request):
    file = request.FILES.get('file')
    return HttpResponse('file', RequestContext(request))
    # return JsonResponse({'location': 'folder/sub-folder/new-location.png'})
