from django.shortcuts import render,HttpResponse
from .models import productcls
# Create your views here.
def home(request):
    pr=productcls.objects.all()
    return render(request,"product\index.html",context={"kala":pr})

def showproduct(request,adad):
   pr=productcls.objects.get(id=adad)
   return render(request,"product\shop.html",context={"kala":pr}) 