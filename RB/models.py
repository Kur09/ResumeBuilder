from django.db import models


# About User Module

# class User(models.Model):
#     email = models.CharField(max_length=50,default="")
#     password = models.CharField(max_length=20,default="")

class ResumeData(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, primary_key=True)
    phone = models.IntegerField(default=0)
    objective = models.CharField(max_length=500)
    prof = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200)

    college = models.CharField(max_length=100, null=True)
    college_join = models.CharField(max_length=50, null=True)
    college_leave = models.CharField(max_length=50, null=True)
    college_field = models.CharField(max_length=50, null=True)
    college_per = models.IntegerField(null=True)

    school_12 = models.CharField(max_length=100, null=True)
    school_12_join = models.CharField(max_length=50, null=True)
    school_12_leave = models.CharField(max_length=50, null=True)
    school_12_field = models.CharField(max_length=50, null=True)
    school_12_per = models.IntegerField(null=True)

    school_10 = models.CharField(max_length=100, null=True)
    school_10_join = models.CharField(max_length=50, null=True)
    school_10_leave = models.CharField(max_length=50, null=True)
    school_10_field = models.CharField(max_length=50, null=True)
    school_10_per = models.IntegerField(null=True)

    skill_name_1 = models.CharField(max_length=50, null=True)
    skill_1 = models.CharField(max_length=100, null=True)
    skill_name_2 = models.CharField(max_length=50, null=True)
    skill_2 = models.CharField(max_length=100, null=True)
    skill_name_3 = models.CharField(max_length=50, null=True)
    skill_3 = models.CharField(max_length=100, null=True)

    project = models.CharField(max_length=50, null=True)
    project_obj = models.CharField(max_length=100, null=True)
    project_tech = models.CharField(max_length=100, null=True)

    img = models.ImageField(upload_to='RB/images', default=0)

    def str(self):
        return self.name


# # Education Model
# class ResumeEdu(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     name1 = models.CharField(max_length=100)
#     join_date1 = models.CharField(max_length=50)
#     leave_date1 = models.CharField(max_length=50)
#     cat1 = models.CharField(max_length=50)

#     name2 = models.CharField(max_length=100)
#     join_date2 = models.CharField(max_length=50)
#     leave_date2 = models.CharField(max_length=50)
#     cat2 = models.CharField(max_length=50)

#     name3 = models.CharField(max_length=100)
#     join_date3 = models.CharField(max_length=50)
#     leave_date3 = models.CharField(max_length=50)
#     cat3 = models.CharField(max_length=50)


# # # Experience and skill Model
# class ResumeExp(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     project_name = models.CharField(max_length=50)
#     obj = models.CharField(max_length=100)
#     tech = models.CharField(max_length=100)

# class Skills(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     skill1 = models.CharField(max_length=50)
#     skill2 = models.CharField(max_length=50)
#     skill3 = models.CharField(max_length=50)


class CoverLetter(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, primary_key=True)
    phone = models.IntegerField(default=0)
    job = models.CharField(max_length=200)
    study = models.CharField(max_length=100)
    strength = models.CharField(max_length=200)
    exp = models.CharField(max_length=200)
