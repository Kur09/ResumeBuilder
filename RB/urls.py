from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('user_reg/', views.reg, name="reg"),
    path('user_login/', views.user_login, name="login"),
    path('user_logout/', views.user_logout, name="logout"),
    path('user_resume/', views.user_resume, name="resume"),
    path('get_demo/<int:id>', views.get_demo, name="demo"),
    path('get_form/<int:id>', views.get_form, name="form"),
    path('get_cover_form/<int:id>', views.get_cover_form, name="coverform"),
    path('cover_data/<int:id>', views.cover_form, name="coverform1"),
    path('resume_data/<int:id>', views.resume_form, name="r_form"),
    path('get_blog/<int:id>', views.get_blog, name="g_form"),

    path('pdf/', views.dowpdf, name='pdf'),
    path('user_cv/', views.user_cv, name='cv'),
    path('get_savedResume/', views.saved_resume, name='saved_resume'),
    path('blog/', views.blog, name='blog'),

]
