from django.shortcuts import render , redirect
from . models import Image

# Create your views here.
def home(request):
    if request.method =='POST':
        image = request.FILES['image']
        Image.objects.create(
           img=image
        )
        return redirect('post')
    return render(request , 'app/home.html')

def post(request):
    pics = Image.objects.all()
    return render(request, 'app/post.html' , {'pics':pics})