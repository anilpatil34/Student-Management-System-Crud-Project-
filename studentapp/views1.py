from django.shortcuts import render,redirect
from django.views import View 
from .models import Student


# class based view for home page
class StudentHomeView(View):
    def get(self, request):
        return render(request, 'studentapp/home.html')

class StudentDisplayAllView(View):
    def get(self, request):
        student_db = Student.objects.all() 
        context = {'data': student_db} 
        return render(request, 'studentapp/display.html', context)
    
class StudentInsertView(View):
    def get(self, request):
        return render(request, 'studentapp/insert.html')
    
    def post(self, request):
        r = request.POST.get('rn')
        n = request.POST.get('nm')
        m = request.POST.get('mk')

        s1 = Student(roll=r, name=n, marks=m)
        s1.save() 
        
        return redirect("/display-all/")
    
class StudentUpdateView(View):
    def get(self, request, roll):
        s1 = Student.objects.get(roll=roll)
        return render(request, 'studentapp/update.html', {'data': s1})
    
    def post(self, request, roll):
        s1 = Student.objects.get(roll=roll)
        updated_n = request.POST.get('nm')
        updated_m = request.POST.get('mk')

        s1.name = updated_n
        s1.marks = updated_m
        s1.save()
        return redirect("/display-all/")