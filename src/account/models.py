from django.db import models

# Create your models here.
class Discipline(models.Model):
    discipline= models.CharField(blank=True, max_length=20)
    def __str__(self):
        return self.discipline

class Account(models.Model):
    username=models.CharField(max_length=10)
    password= models.CharField( max_length=20)
    firstname= models.CharField(blank=True, max_length=20)
    lastname= models.CharField(blank=True, max_length=20)
    image= models.ImageField(upload_to="accounts/images/")
    user_title=models.CharField(blank=True, max_length=50)
    user_pgesco_Id=models.CharField(blank=True, max_length=20)
    Discipline= models.ForeignKey(Discipline,on_delete=models.CASCADE)
    email = models.EmailField()
    mobile= models.CharField(blank=True, max_length=20)
    VoIP= models.CharField(blank=True, max_length=20)
    site= models.CharField(blank=True, max_length=20)
    status=models.BooleanField(default=True)
    responsability=models.CharField( max_length=10,default=1)

    def __str__(self):
        return self.firstname + " " + self.lastname

        class Meta:
            ordering = -['firstname']
    def get_absolute_url(self):
            return reverse(account-detail, kwargs={"pk": self.pk})