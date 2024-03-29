from django.db import models
import datetime as dt

# Create your models here.

class ibyiciro(models.Model):
    name = models.CharField(max_length =30)

    
    def __str__(self):
        return self.name

    def save_ciro(self):
        self.save()

    def delete_ciro(self):
        self.save()

class Ahanu(models.Model):
    here = models.CharField(max_length =30)

    def __str__(self):
        return self.here

class Pics(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField()
    ciro = models.ForeignKey(ibyiciro)
    hanu = models.ManyToManyField(Ahanu)
    pub_date = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to = 'pictures/',null=True)

    @classmethod
    def save_pic(self):
        self.save()

    @classmethod
    def todays_pic(cls):
        today = dt.date.today()
        image = cls.objects.filter(pub_date__date = today)
        return image

    @classmethod
    def day_pic(cls,date):
        image = cls.objects.filter(pub_date__date = date)
        return image

    @classmethod
    def search_by_ciro(cls,search_term):
        image = cls.objects.filter(ciro__name__icontains=search_term)
        return image



    