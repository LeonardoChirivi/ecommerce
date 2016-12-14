from django.shortcuts import (render,
                              get_object_or_404,
                              render_to_response)

def index(request, template_name='catalog/index.html'):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render_to_response()

