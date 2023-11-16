from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.db.models import Q
from datetime import datetime




# Create your views here.
def loginview(request):
    
    if request.user.is_authenticated:
        return redirect('employees')

    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            context ={'user': user}
            return redirect(reverse('employees'),context)
        
        messages.error(request,"Invalid credentials")
        return render(request,"login.html")

    return render(request,"login.html")

@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def EmployeeView(request):
    search_query = request.GET.get('search_query', '')

    employees = Employee.objects.all()

    if search_query:
        # Split the search query into individual words
        keywords = search_query.split()

        # Create an empty Q object to build the query dynamically
        search_q = Q()

        for keyword in keywords:
            try:
                # Try to parse the keyword as a date in various formats
                date_obj = datetime.strptime(keyword, '%Y-%m-%d')
            except ValueError:
                date_obj = None

            if date_obj:
                # If the keyword is a valid date, filter employees by date
                search_q |= Q(contract_start_date=date_obj) | Q(contract_end_date=date_obj)
            else:
                # If the keyword is not a date, search by other fields
                search_q |= (
                    Q(Emp_name__icontains=keyword) |
                    Q(contract_no__icontains=keyword) |
                    Q(state__icontains=keyword) |
                    Q(duty_station__icontains=keyword)
                )

        employees = employees.filter(search_q)

    context = {
        'employees': employees,
        'search_query': search_query,
    }

    return render(request, 'employees.html', context)



@login_required(login_url='login')
def EmployeeProfileView(request, pk):
    try:
        employee = Employee.objects.get(uuid=pk)
        flight_budget, _ = FlightBudget.objects.get_or_create(employee=employee)
        travel_budget, _ = TravelBudget.objects.get_or_create(employee=employee)
        ope_budget, _ = OPEBudget.objects.get_or_create(employee=employee)
        remaining_budget_flight = float(flight_budget.allocated_budget) * 0.2
        remaining_budget_travel = float(travel_budget.allocated_budget) * 0.2
        remaining_budget_ope = float(ope_budget.allocated_budget) * 0.2
    except Employee.DoesNotExist:
        employee = None
        remaining_budget_flight = 0
        remaining_budget_travel = 0
        remaining_budget_ope = 0

    context = {
        'employee': employee,
        'flight_budget': flight_budget,
        'travel_budget': travel_budget,
        'ope_budget': ope_budget,
        'remaining_budget_flight': remaining_budget_flight,
        'remaining_budget_travel': remaining_budget_travel,
        'remaining_budget_ope': remaining_budget_ope,
    }
    return render(request, "profile.html", context)



@login_required(login_url='login')
def AdvancedTravelPlanView(request,pk):
    try:
        emp = Employee.objects.get(uuid=pk)
        search_query = request.GET.get('search_query', '')
        atp = AdvancedTravelPlan.objects.filter(employee=emp)
        if search_query:
        # Split the search query into individual words
            keywords = search_query.split()

            # Create an empty Q object to build the query dynamically
            search_q = Q()

            for keyword in keywords:
                try:
                    # Try to parse the keyword as a date in various formats
                    date_obj = datetime.strptime(keyword, '%Y-%m-%d')
                except ValueError:
                    date_obj = None

                if date_obj:
                    # If the keyword is a valid date, filter employees by date
                    search_q |= Q(from_date=date_obj) | Q(to_date=date_obj)
                else:
                    # If the keyword is not a date, search by other fields
                   search_q |= Q(month__icontains=keyword) | Q(year__icontains=keyword)

            atp = atp.filter(search_q)
        
    except:
        atp = None

    context = {
        'atp' : atp,
        'emp' : emp
    }
    
    return render(request,"advancedtravelplan.html",context)





@login_required(login_url='login')
def ActualTravelPlan(request,pk):
    try:
        search_query = request.GET.get('search_query', '')
        emp = Employee.objects.get(uuid=pk)
        tp = Expense.objects.filter(employee=emp)

        if search_query:
        # Split the search query into individual words
            keywords = search_query.split()

            # Create an empty Q object to build the query dynamically
            search_q = Q()

            for keyword in keywords:
                try:
                    # Try to parse the keyword as a date in various formats
                    date_obj = datetime.strptime(keyword, '%Y-%m-%d')
                except ValueError:
                    date_obj = None

                if date_obj:
                    # If the keyword is a valid date, filter employees by date
                    search_q |= Q(from_date=date_obj) | Q(to_date=date_obj)
                else:
                    # If the keyword is not a date, search by other fields
                    pass

            tp = tp.filter(search_q)
        
    except:
        tp = None

    context = {
        'tp' : tp,
        'emp' : emp,
        'search_query': search_query,
    }
    
    return render(request,"actualtravelplan.html",context)

@login_required(login_url='login')
def ViewAtp(request,pk1,pk2):
    try:
        emp = Employee.objects.get(uuid=pk1)
        
        tp = Expense.objects.get(uuid=pk2)
        

    except:
        tp = None
    context = {
        'tp':tp,
        'emp':emp
    }
    return render(request,'viewatp.html',context)



def error404(request,exception):
    return render(request,'error404.html')
        

