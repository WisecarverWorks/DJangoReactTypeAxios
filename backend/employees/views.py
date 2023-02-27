from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Employee
from .serializers import EmployeeSerializer
from .forms import EmployeeUploadForm

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<
def index(request):
    data = Employee.objects.all()
    context = {
        'data': data
    }
    return render(request, 'display.html', context)

# new


def uploadView(request):
    if request.method == 'POST':
        form = EmployeeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeUploadForm()
    return render(request, 'upload.html', {'form': form})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_employees(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        employees = Employee.objects.filter(user_id=request.user.id)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
