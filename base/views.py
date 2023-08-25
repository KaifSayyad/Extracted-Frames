from django.shortcuts import render
from .models import Image
# Create your views here.
def home(request):
    model = Image.objects.all()
    context = {'model' : model}
    return render(request , 'base/home.html', context)