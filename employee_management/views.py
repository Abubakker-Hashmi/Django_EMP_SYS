from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

def employee_lists(request):
    employees = Employee.objects.all()
    return render(request, 'employee_management/employee_list.html', {'employees': employees})

def create_employee(request):
    if request.method == 'POST':
        en = request.POST['employee_number']
        names = request.POST['name']
        department = request.POST['department']
        role = request.POST['role']
        salary = request.POST['salary']
        working_experience = request.POST['working_experience']

        employee = Employee(employee_number=en, name=names, department=department, role=role,
                            salary=salary, working_experience=working_experience)
        employee.save()

        return redirect('employee-lists')

    return render(request, 'employee_management/create_employee.html')

def filter_employees(request):
    if request.method == 'POST':
        department = request.POST['department']
        employees = Employee.objects.filter(department=department)


        return render(request, 'employee_management/employee_list.html', {'employees': employees})

    return render(request, 'employee_management/filter_employees.html')

def remove_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employee-lists')
