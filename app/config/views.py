import mimetypes
import os

from django.conf import settings
from django.http import FileResponse, HttpResponse


def serve_media(request, path):
    media_path = os.path.join(settings.MEDIA_ROOT, path)
    content_type = mimetypes.guess_type(path)
    response = FileResponse(open(media_path, 'rb'), content_type=content_type)
    return response
