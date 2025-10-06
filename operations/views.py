from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def employee_form(request):
    if request.method == "POST":
        data=request.POST
        emp_name=data.get('emp_name')
        emp_id=data.get('emp_id')
        emp_dob=data.get('emp_dob')
        emp_pos=data.get('emp_pos')
        emp_address=data.get('emp_address')

        Employee.objects.create(emp_name=emp_name, emp_id=emp_id, emp_pos=emp_pos, emp_dob=emp_dob, emp_address=emp_address)
        return redirect('/')
    
    queryset=Employee.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(emp_name__icontains=request.GET.get('search'))
    context={'employee':queryset}

    return render(request,"index.html",context)

def update_emp(request,id):
    queryset=Employee.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        emp_name=data.get('emp_name')
        emp_id=data.get('emp_id')
        emp_dob=data.get('emp_dob')
        emp_pos=data.get('emp_pos')
        emp_address=data.get('emp_address')

        queryset.emp_name=emp_name
        queryset.emp_id=emp_id
        queryset.emp_dob=emp_dob
        queryset.emp_pos=emp_pos
        queryset.emp_address=emp_address

        queryset.save()
        return redirect('/')
    context={'employee':queryset}
    return render(request,'update_emp.html',context)

def delete_emp(request,id):
    queryset=Employee.objects.get(id=id)
    queryset.delete()
    return redirect('/')