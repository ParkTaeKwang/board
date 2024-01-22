from django.shortcuts import render_to_response, redirect
from guestbook.models import Guestbook
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def list(request):
    gbCount = Guestbook.objects.count()
    gbList = Guestbook.objects.order_by("-idx")
    return render_to_response(\
        "list.html", {"gbList":gbList,"gbCount":gbCount})

@csrf_exempt
def write(request):
    return render_to_response("write.html")

@csrf_exempt
def insert(request):
    dto=Guestbook(title=request.POST["title"],
                  name=request.POST["name"],
                  email=request.POST["email"],
                  passwd=request.POST["passwd"],
                  content=request.POST["content"])
    dto.save()
    return redirect("/")