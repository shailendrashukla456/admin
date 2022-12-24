from django.shortcuts import render,redirect
from . forms import EmpForm
from . models import Employee

# Create your views here.

def Addemployee(request):
    empForm = EmpForm()
    return render(request,'Addemployee.html',{'empForm':empForm})

def insertemployee(request):
    if request.method=="POST":
        empForm=EmpForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            return render(request,'EmployeeDetails.html')
        else:
           return render(request,'Addemployee.html')
        
    return render(request,'Addemployee.html')

def EmployeeDetails(request):
    employee=Employee.objects.all()
    return render(request,'EmployeeDetails.html',{'employee':employee})

def update(request,Id):
    emp=Employee.objects.get(Id=Id)
    return render(request,'update.html',{'emp':emp})

def edit(request,Id):
    if request.method=="POST":
        emp=Employee.objects.get(Id=Id)
        form=EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return render(request,'EmployeeDetails.html')
        else:
            return render(request,'update.html')
    else:
        return render(request,'update.html')


def delete(request,Id):
    emp=Employee.objects.get(Id=Id)
    emp.delete()
    return redirect("EmployeeDetails")