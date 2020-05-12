from django.shortcuts import render, redirect
from secapp.models import State


# Create your views here.
def home(request):
    data = State.objects.all()
    return render(request, "secapp/home.html", context={"data": data})



def stateadd(requset):
    if requset.method == "POST":
        data = State(statename=requset.POST.get("var1"), statecode=requset.POST.get("var2")
                     , state_cm=requset.POST.get("var3"))
        data.save()
        return redirect("/state/")
    return render(requset, "secapp/state.html")


def update(request, id):
    data = State.objects.get(id=id)
    return render(request, "secapp/update.html", context={"data": data})

def updatestate(request, id):
    data = State.objects.get(id=id)
    data.statename = request.POST.get("var1")
    data.statecode = request.POST.get("var2")
    data.state_cm = request.POST.get("var3")
    data.save()
    return redirect("/home/")


def deletestate(request, id):
    data = State.objects.get(id=id)
    data.delete()
    return redirect("/home/")
