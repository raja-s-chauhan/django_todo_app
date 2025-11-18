from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Employee
# Create your views here.
def employee_detail(request, employee_id):
        employee = get_object_or_404(Employee, id=employee_id)
        context = {'employee': employee}
        return render(request, 'employee_details.html', context)
        # return HttpResponse(f"Employee: {employee.first_name} {employee.last_name}, Designation: {employee.designation}")
   