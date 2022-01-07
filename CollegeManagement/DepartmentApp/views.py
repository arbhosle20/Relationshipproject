from django.shortcuts import render,redirect
from .forms import DeptModelForm
from .models import Dept
from django .views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class AddDeptView(LoginRequiredMixin,View):
    def get(self,request):
        form = DeptModelForm()
        template_name = 'DepartmentApp/adddept.html'
        context = {'form':form}
        return render(request,template_name,context)
    def post(self,request):
        form = DeptModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_dept')
        template_name = 'DepartmentApp/adddept.html'
        context = {'form':form}
        return render(request,template_name,context)

class ShowDeptView(View):
    def get(self,request):
        depts_list = Dept.objects.all()
        template_name = 'DepartmentApp/showdept.html'
        context = {'depts_list':depts_list}
        return render(request,template_name,context)

    def post(self,request):
        department = Dept.objects.filter(name__icontains=request.POST['searchdata'])
        professor = department[0].department_pro.all()
        student = department[0].department_stu.all()
        template_name = "DepartmentApp/searchdept.html"
        context = {'department': department, 'professor': professor, 'student': student}
        return render(request, template_name, context)

class DeptUpdate(LoginRequiredMixin,View):
    def get(self,request,i):
        depts = Dept.objects.get(id=i)
        form = DeptModelForm(instance=depts)
        template_name = 'DepartmentApp/adddept.html'
        context ={'form':form}
        return render(request,template_name,context)
    def post(self ,request,i):
        depts = Dept.objects.get(id=i)
        form = DeptModelForm(request.POST,instance=depts)
        if form.is_valid():
            form.save()
            return redirect('show_dept')
        template_name = 'DepartmentApp/adddept.html'
        context = {'form':form}
        return render(request,template_name,context)

class DeptDelete(LoginRequiredMixin,View):
    def get(self,request,i):
        depts = Dept.objects.get(id=i)
        template_name = 'DepartmentApp/deledept.html'
        context = {'depts':depts}
        return render(request,template_name,context)

    def post(self,request,i):
        depts = Dept.objects.get(id=i)
        depts.delete()
        return redirect('show_dept')





# Create your views here.
