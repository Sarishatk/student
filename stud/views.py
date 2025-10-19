from django.shortcuts import render
from django.views.generic import View
from stud.models import StudentModel

# Create your views here.

class studentCreateView(View):

    def get(self,request):

        return render(request,"create_stud.html")
    
    def post(self,request):

        print(request.POST)

        # add browser html inputs to model (database)

        StudentModel.objects.create(name = request.POST.get("name"),
                                     roll_no =request.POST.get("rollno"),
                                      department=request.POST.get("dept"),
                                       email =request.POST.get("email"),
                                       marks =request.POST.get("mark")
                                         )

        return render(request,"create_stud.html")
    

# update student form using get method

class UpdateStudView(View):

    def get(self,request):

        stud_data = StudentModel.objects.get(id = 1)

        return render(request,"update_stud.html",{"stud_data":stud_data})




