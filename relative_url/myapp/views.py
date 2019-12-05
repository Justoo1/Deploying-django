from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"myapp/index.html",context={'yeap':'WELCOM'})

def other(request):
    return render(request, 'myapp/other.html')

def relative(request):
    return render(request, 'myapp/relative_template_tag.html')
