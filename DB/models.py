from django.db import models

class Userreg(models.Model):
    
    FNAME = models.CharField(max_length=100) 
    LNAME = models.CharField(max_length=100)
    EMAIL = models.CharField(max_length=50)
    MOBILE_NO = models.CharField(max_length=12)
    PSWD = models.CharField(max_length=15)
    

    def __str__(self):
       return self.EMAIL

    class Meta:
        db_table="userreg"


class Studentreg(models.Model):
    F_name=models.CharField(max_length=100)
    L_name=models.CharField(max_length=100)
    email = models.CharField(max_length=100) 
    mobile_no = models.IntegerField(max_length=12)
    student_id= models.IntegerField(max_length=15 )
    room_id= models.IntegerField(max_length=15)
    status_id=models.CharField(max_length=50)
    score=models.IntegerField(max_length=20)
    PSWD = models.CharField(max_length=20)
    def __str__(self):
       return self.email
    
    class Meta:
        db_table="studentreg"
