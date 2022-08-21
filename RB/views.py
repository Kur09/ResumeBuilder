from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# from weasyprint import HTML
from .connection import Mongopy
from .forms import TemplateForm, CoverForm
from .models import ResumeData
from .utils import render_to_pdf


# Create your views here.

def home(request):
    form = UserCreationForm()

    data = {'form': form}
    return render(request, 'resumeHome/home.html', data)


def blog(request):
    return render(request, 'resumeHome/blogHome.html')


def reg(request):
    fm = UserCreationForm()
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        user = User.objects.create_user(username=username, password=pass1)
        if pass1 == pass2:
            user.save()
            messages.success(request, 'Register Successfully')
            return render(request, 'resumeHome/navbar.html', {'form': fm})
        else:
            print("Not Valid......")
            messages.success(request, 'Error....')
    else:

        return render(request, 'resumeHome/navbar.html', {'form': fm})
    return redirect("/")


def user_login(request):
    global m, col
    if request.method == 'POST':
        email = request.POST['login_email']
        password = request.POST['login_pass']
        print("USER NAM<E IS   ", email, password)
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print(email, password)
            messages.success(request, (f"Welcome! {email}"))
            m = Mongopy()
            col = m.connect('Shiv')

            return redirect("/")
        else:
            messages.success(request, ("Invalid Credentials"))
            print("........No.........")
            return redirect("/")

    return redirect("/")


def user_logout(request):
    logout(request)
    return redirect("/")


def user_resume(request):
    return render(request, 'resumeHome/resumehome.html')


def user_cv(request):
    return render(request, 'resumeHome/cvhome.html')


def get_demo(request, id):
    return render(request, 'resumeTemplates/template' + str(id) + '.html')


def get_blog(request, id):
    return render(request, 'blog/blog' + str(id) + '.html')


def get_form(request, id):
    print("user is ", request.user.email)
    return render(request, 'formTemplate/form1.html', {'id': id})


def get_cover_form(request, id):
    print("user is ", request.user.email)
    return render(request, 'formTemplate/form2.html', {'id': id})


def resume_form(request, id):
    fm = TemplateForm(request.POST)
    print("name is ", fm['name'].value())
    # usr = ResumeData(request.POST)
    # m = Mongopy()
    # col = m.connect(request.POST['name'])
    data1 = {
        "cv_id": id,
        "name": fm['name'].value(),
        "email": fm['email'].value(),
        "objective": fm['objective'].value(),
        "prof": fm['prof'].value(),
        "college": fm['college'].value(),
        # "college_location":fm['college_location'],
        "college_join": fm['college_join'].value(),
        "college_leave": fm['college_leave'].value(),
        "college_field": fm['college_field'].value(),
        "college_per": fm['college_per'].value(),
        "school_12": fm['school_12'].value(),
        # "school_12_location":fm['school_12_location'],
        "school_12_join": fm['school_12_join'].value(),
        "school_12_leave": fm['school_12_leave'].value(),
        "school_12_field": fm['school_12_field'].value(),
        "school_12_per": fm['school_12_per'].value(),
        "school_10": fm['school_10'].value(),
        # "school_10_location":fm['school_10_location'],
        "school_10_join": fm['school_10_join'].value(),
        "school_10_leave": fm['school_10_leave'].value(),
        "school_10_per": fm['school_10_per'].value(),
        "skill_name_1": fm['skill_name_1'].value(),
        "skill_1": fm['skill_1'].value(),
        "skill_name_2": fm['skill_name_2'].value(),
        "skill_2": fm['skill_2'].value(),
        "skill_name_3": fm['skill_name_3'].value(),
        "skill_3": fm['skill_3'].value(),
        "project": fm['project'].value(),
        "project_obj": fm['project_obj'].value(),
        "project_tech": fm['project_tech'].value()
    }
    # # col.insert_one(data1)

    data = {'form': fm}
    print("................")

    return render(request, 'getResumeTemplate/form' + str(id) + '.html', data)
    # pdf = render_to_pdf('getResumeTemplate/form'+str(id)+'.html',data)
    # return HttpResponse(pdf, content_type='application/pdf')


def cover_form(request, id):
    fm = CoverForm(request.POST)
    print("name is ", fm['name'].value())
    # usr = ResumeData(request.POST)
    # m = Mongopy()
    # col = m.connect(request.POST['name'])
    # data1 = {
    #         "cv_id":id,
    #         "name":fm['name'].value(),
    #         "email":fm['email'].value(),
    #         "objective":fm['objective'].value(),
    #         "prof":fm['prof'].value(),
    #         "college":fm['college'].value(),
    #         # "college_location":fm['college_location'],
    #         "college_join":fm['college_join'].value(),
    #         "college_leave":fm['college_leave'].value(),
    #         "college_field":fm['college_field'].value(),
    #         "college_per":fm['college_per'].value(),
    #         "school_12":fm['school_12'].value(),
    #         # "school_12_location":fm['school_12_location'],
    #         "school_12_join":fm['school_12_join'].value(),
    #         "school_12_leave":fm['school_12_leave'].value(),
    #         "school_12_field":fm['school_12_field'].value(),
    #         "school_12_per":fm['school_12_per'].value(),
    #         "school_10":fm['school_10'].value(),
    #         # "school_10_location":fm['school_10_location'],
    #         "school_10_join":fm['school_10_join'].value(),
    #         "school_10_leave":fm['school_10_leave'].value(),
    #         "school_10_per":fm['school_10_per'].value(),
    #         "skill_name_1":fm['skill_name_1'].value(),
    #         "skill_1":fm['skill_1'].value(),
    #         "skill_name_2":fm['skill_name_2'].value(),
    #         "skill_2":fm['skill_2'].value(),
    #         "skill_name_3":fm['skill_name_3'].value(),
    #         "skill_3":fm['skill_3'].value(),                                        
    #         "project":fm['project'].value(),
    #         "project_obj":fm['project_obj'].value(),
    #         "project_tech":fm['project_tech'].value()
    #     }
    # # col.insert_one(data1)

    data = {'form': fm}
    print("................")

    return render(request, 'getResumeTemplate/form' + str(id) + '.html', data)


def dowpdf(request):
    user = ResumeData(name='sam')
    print("..........................")

    data = {
        'form': user
    }
    pdf = render_to_pdf('resumeTemplates/template5.html')
    return HttpResponse(pdf, content_type='application/pdf')


def saved_resume(request):
    # alldocs = col.find()
    data = {"alldocs": col.find()}
    return render(request, 'getSavedTemplate/savedResume.html', data)

# def generate_pdf(request,id):
#     """Generate pdf."""
#     # Model data


#     # Rendered
#     html_string = render_to_string('getResumeTemplate/form'+str(id)+'.html')
#     html = HTML(string=html_string)
#     result = html.write_pdf()

#     # Creating http response
#     response = HttpResponse(content_type='application/pdf;')
#     response['Content-Disposition'] = 'inline; filename=list_people.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'
#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output = open(output.name, 'r')
#         response.write(output.read())

#     return response
