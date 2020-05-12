from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def emp_view(request):
    empdata = Employee.objects.all()
    return render(request, "app/emp.html", context={"empdata": empdata})


def emp_add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            emp = request.POST['name']
            messages.info(request, f'employee {emp} added successfully.')
        return redirect("/emp/")
    form = EmployeeForm()
    return render(request, "app/empadd.html", context={"form": form})

def emp_update(request, id):
    data = Employee.objects.get(id=id)
    form = EmployeeForm(instance=data)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.info(request, f'employee {data.name} update successfully')
        return redirect("/emp/")
    return render(request, "app/update.html", context={"form": form})

def emp_delete(request, id):
    del_emp = Employee.objects.get(id=id)
    messages.info(request, f'employee {del_emp.name} deleted successfully')
    del_emp.delete()
    return redirect("/emp/")
