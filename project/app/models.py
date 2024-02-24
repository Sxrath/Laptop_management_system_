from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Condition(models.Model):
    Condition=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Condition

class Laptop(models.Model):
    serial_number = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=50)
    condition = models.ForeignKey(Condition,on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.serial_number

class Transaction(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    check_out_time = models.DateTimeField()
    check_in_time = models.DateTimeField(null=True, blank=True)
    is_late = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        History.objects.create(student=self.student, laptop=self.laptop, time=self.check_out_time)



    
class feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE,default=None)
    feedback=models.TextField(max_length=300,default=None)
    Date= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student} feed back on {self.laptop }"
    
class Reservation(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, default=None)
    fromtime = models.DateTimeField(default=timezone.now)
    totime = models.DateTimeField()
    def __str__(self):
        return f"{self.student} reserved {self.fromtime}"

class Studentprofile(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    feedback=models.ForeignKey(feedback,on_delete=models.CASCADE)
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE)
    
class History(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    time=models.DateTimeField()
    def __str__(self):
     return f"{str(self.student)} - {str(self.laptop)}"
