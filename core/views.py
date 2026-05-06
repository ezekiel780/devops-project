from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from my DevOps Project! 🚀 Running on Kubernetes!")
