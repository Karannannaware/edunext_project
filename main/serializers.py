from rest_framework import serializers
from .models import Instructor, Course, Student
from django.contrib.auth.models import User

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all())

    class Meta:
        model = Course
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'user', 'enrolled_courses']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        enrolled_courses = validated_data.pop('enrolled_courses', [])
        student = Student.objects.create(user=user)
        student.enrolled_courses.set(enrolled_courses)
        return student
