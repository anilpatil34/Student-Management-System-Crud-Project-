from django.shortcuts import render,redirect
from .models import Student


# Create your views here.

def home_view(request):
    return render(request, 'studentapp/home.html')

def insert_students(request):

    if request.method == 'POST':
        r = request.POST.get('rn')
        n = request.POST.get('nm')
        m = request.POST.get('mk')

        s1 = Student(roll=r, name=n, marks=m)
        s1.save() # using this method student data will be saved in database table we created above s1 object .save method to insert data into table above student class parnethesis available fields and values 
        
    # after above all logic completed data will stored in database table and thhen we will redirect to display all students page
        return redirect("/student/display-all/") # after inserting data we will redirect to display all students page
        #return redirect("https://thekiranacademy.com/") # we pass the website url to redirect to that website
    return render(request, 'studentapp/insert.html')

def display_students(request):
 # fetch all data from student table its below is django orm query
    student_db = Student.objects.all() # to fetch all data from student table we created above we used objects.all() method to fetch all data from table
    
    context = {'data': student_db} # context dictionary to send all fetched data to html page all data comes inside student_db variable we assigned to data key in context dictionary data key we cal in html data will get displayed on html page
    
    return render(request, 'studentapp/display.html', context) # we called context dictionary here to display all fetched data on display.html page

def update_student_view(request, roll):
    s1 = Student.objects.get(roll=roll)

    if request.method == "POST":
        updated_n = request.POST.get('nm')
        updated_m = request.POST.get('mk')

        s1.name = updated_n
        s1.marks = updated_m
        s1.save()
        return redirect("/display-all/")

    return render(request, 'studentapp/update.html', {'data': s1})

def delete_student_view(request, roll):

    s1 = Student.objects.get(roll=roll)

    if request.method == "POST": # when we click on confirm button in delete.html page request method will be post
     s1.delete() # to delete the record from database table we use .delete() method on object we fetched from database table
     return redirect("/display-all/") # after deleting the record we will redirect to display all students page


    return render(request, 'studentapp/delete.html', {'data': s1})  
    