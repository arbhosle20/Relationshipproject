from django.shortcuts import render,redirect
from .forms import ProfModelForm
from .models import Prof
from django .views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class AddProfView(LoginRequiredMixin,View):
    def get(self,request):
        form = ProfModelForm()
        template_name = 'ProfessorApp/addprof.html'
        context = {'form':form}
        return render(request,template_name,context)
    def post(self,request):
        form = ProfModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_prof')
        template_name = 'ProfessorApp/addprof.html'
        context = {'form':form}
        return render(request,template_name,context)

class ShowProfView(View):
    def get(self,request):
        profs_list = Prof.objects.all()
        template_name = 'ProfessorApp/showprof.html'
        context = {'profs_list':profs_list}
        return render(request,template_name,context)

class ProfUpdate(LoginRequiredMixin,View):
    def get(self,request,i):
        profs = Prof.objects.get(id=i)
        form = ProfModelForm(instance=profs)
        template_name = 'ProfessorApp/addprof.html'
        context ={'form':form}
        return render(request,template_name,context)
    def post(self ,request,i):
        profs = Prof.objects.get(id=i)
        form = ProfModelForm(request.POST,instance=profs)
        if form.is_valid():
            form.save()
            return redirect('show_prof')
        template_name = 'ProfessorApp/addprof.html'
        context = {'form':form}
        return render(request,template_name,context)

class ProfDelete(LoginRequiredMixin,View):
    def get(self,request,i):
        profs = Prof.objects.get(id=i)
        template_name = 'ProfessorApp/deleteprof.html'
        context = {'profs':profs}
        return render(request,template_name,context)

    def post(self,request,i):
        profs = Prof.objects.get(id=i)
        profs.delete()
        return redirect('show_prof')





# Create your views here.
