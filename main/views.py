from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import Course, Instructor, Student
from .serializers import CourseSerializer, InstructorSerializer, StudentSerializer

# 🎯 Default HTML Views
def index(request):
    return render(request, 'index.html')

def home(request):
    return HttpResponse("🎓 Welcome to EduWeb API Home")

# 🎯 Instructor API View
class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

# 🎯 Course API View
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 🎯 Student API View
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# ✅ Student Register API
class StudentRegisterView(APIView):
    def post(self, request):
        user_data = request.data.get("user")
        enrolled_courses = request.data.get("enrolled_courses", [])
        password = user_data.get("password")

        if User.objects.filter(username=user_data["username"]).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # ✔️ Create user with hashed password
        user = User.objects.create_user(
            username=user_data["username"],
            email=user_data.get("email"),
            password=password
        )

        # ✔️ Create student and link to courses
        student = Student.objects.create(user=user)
        student.enrolled_courses.set(enrolled_courses)
        student.save()

        return Response({"message": "Student registered successfully!"}, status=status.HTTP_201_CREATED)

# ✅ Custom Login API
class CustomLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
