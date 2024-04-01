from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students_list = Student.objects.all()
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('students')
    return render(request, 'students.html', {'students': students_list, 'form': form})

def courses(request):
    courses_list = Course.objects.all()
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('courses')
    return render(request, 'courses.html', {'courses': courses_list, 'form': form})


def details(request, student_id):
    student = Student.objects.get(id=student_id)
    available_courses = Course.objects.exclude(students=student)
    
    if request.method == 'POST':
        course_name = request.POST.get('course')
        if course_name:
            course = Course.objects.get(name=course_name)
            student.courses.add(course)
            student.save()
            return redirect('details', student_id=student_id)

    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})
