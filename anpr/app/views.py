from django.shortcuts import render
from app.forms import Anprform
from app.lpr import detect
from django.conf import settings
from app.models import Anpr
import os


# Create your views here.

def index(request):
    form = Anprform()

    if request.method == 'POST':
        form = Anprform(request.POST or None, request.FILES or None)
        if form.is_valid():
            save = form.save(commit=True)

            primary_key = save.pk
            imgobj = Anpr.objects.get(pk=primary_key)
            fileroot = str(imgobj.image)
            filepath = os.path.join(settings.MEDIA_ROOT, fileroot)
            results = detect(filepath)
            print(results)
            return render(request, "index.html",{'form':form, 'upload':True,'results':results})

    return render(request, "index.html",{'form':form, 'upload':False})
