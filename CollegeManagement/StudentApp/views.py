from django.shortcuts import render,redirect
from .forms import StudentModelForm
from .models import Student
from django .views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class AddStudentView(LoginRequiredMixin,View):
    def get(self,request):
        form = StudentModelForm()
        template_name = 'StudentApp/addstudent.html'
        context = {'form':form}
        return render(request,template_name,context)
    def post(self,request):
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_student')
        template_name = 'StudentApp/addstudent.html'
        context = {'form':form}
        return render(request,template_name,context)

class ShowStudentView(View):
    def get(self,request):
        student_list = Student.objects.all()
        template_name = 'StudentApp/showstudent.html'
        context = {'student_list':student_list}
        return render(request,template_name,context)

class StudentUpdate(LoginRequiredMixin,View):
    def get(self,request,i):
        student = Student.objects.get(id=i)
        form = StudentModelForm(instance=student)
        template_name = 'StudentApp/addstudent.html'
        context ={'form':form}
        return render(request,template_name,context)
    def post(self ,request,i):
        student = Student.objects.get(id=i)
        form = StudentModelForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_student')
        template_name = 'StudentApp/addstudent.html'
        context = {'form':form}
        return render(request,template_name,context)

class StudentDelete(LoginRequiredMixin,View):
    def get(self,request,i):
        student = Student.objects.get(id=i)
        template_name = 'StudentApp/deletestudent.html'
        context = {'student':student}
        return render(request,template_name,context)

    def post(self,request,i):
        student = Student.objects.get(id=i)
        student.delete()
        return redirect('show_student')





# Create your views here.
