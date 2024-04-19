from django.db import models
from django.utils.text import slugify

class Company(models.Model):
    description = models.TextField()
    logo = models.ImageField(upload_to="logo")
    logo_whitr = models.ImageField(upload_to="logo")
    phone_number = models.CharField(max_length=225)
    email1 = models.EmailField()
    email2 = models.EmailField()
    linkedin = models.URLField()
    youtube = models.URLField()
    facebook = models.URLField()


# Create your models here.
class Service(models.Model):
    nom = models.CharField(max_length=225)
    description = models.TextField()
    icon = models.CharField(max_length=225)
    def __str__(self) -> str:
        return self.nom
    
class FAQ(models.Model):
    question = models.TextField()
    reponse = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    STATUS_CHOICES = (
        ('on_demand', 'On Demand'),
        ('available', 'Available'),
        ('coming_soon', 'Coming Soon'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Price = models.PositiveIntegerField(default=0)
    Finance_options = models.CharField(max_length=255)
    image = models.ImageField(upload_to="courses")
    start_date = models.DateField(blank=True)
    programs_training = models.TextField(blank=True)
    Study_method = models.CharField(max_length=255)
    Duration = models.CharField(max_length=255)
    Overview =  models.TextField()
    Course_Outline = models.TextField()
    Advantages = models.TextField()
    Requirements = models.TextField()
    Certificates = models.TextField()
    tags = models.ManyToManyField(Tags,blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    slug = models.SlugField(max_length=100, blank=True, null=True)
    def __str__(self) -> str:
        return self.title

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class EnquireModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    Select_Course_Certification_Exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    preferred_date_time = models.DateTimeField()
    any_previous_experience_on_IT = models.TextField()
    Any_special_request_accommodations = models.TextField()
    comments_question = models.TextField()
    



class Testimony(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="test")
    content = models.TextField()
    title = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    def __str__(self) -> str:
        return self.name


class AffiliatePartner(models.Model):
    firstname = models.CharField(max_length=225)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    Referrer_name = models.CharField(max_length=255)
    Referrer_email = models.CharField(max_length=255)
    Referrer_phone_number = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)


