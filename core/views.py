from django.shortcuts import redirect, render

from core.forms import AffiliatePartnerForm, ContactForm, EnquireModelForm
from .models import FAQ, Category, Course, Service, Tags, Testimony
from django.utils.translation import activate

# Create your views here.
def home(request):
    services = Service.objects.all()
    faq_items = FAQ.objects.all()
    category = Category.objects.all()
    courses = Course.objects.all()
    testimony1 = Testimony.objects.all()[:6]
    testimony2 = Testimony.objects.all()[:10]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mail_succes)
    else:
        form = ContactForm()


    params = {
        'services':services,
        'faq_items':faq_items,
        'categories':category,
        'courses':courses,
        'testimony1':testimony1,
        'testimony2':testimony2,
        'form':form

    }
    return render(request,'main/index.html',params)

def details_course(request,slug):
    course = Course.objects.get(slug=slug)
    courses = Course.objects.filter(status = 'coming_soon')
    categories = Category.objects.all()[:15]
    tags = Tags.objects.all()
    if request.method == 'POST':
        form = EnquireModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(enroll_success)  # Replace 'success_page' with the name of your success URL pattern
    else:
        form = EnquireModelForm()
    params ={
        'form':form,
        'tags':tags,
        'course':course,
        'courses':courses,
        'categories':categories
    }
    return render(request,'main/details_course.html',params)

def mail_succes(request):
    return render(request,'main/mail_sent.html')

def enroll_success(request):
    return render(request,'main/enrol_success.html')

def courses(request):
    courses = Course.objects.all()
    params ={
        'courses':courses
    }
    return render(request,'main/courses.html',params)

def about(request):
    faq_items = FAQ.objects.all()
    category = Category.objects.all()
    courses = Course.objects.all()
    testimony1 = Testimony.objects.all()[:6]
    testimony2 = Testimony.objects.all()[:10]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mail_succes)
    else:
        form = ContactForm()


    params = {
        'faq_items':faq_items,
        'categories':category,
        'courses':courses,
        'testimony1':testimony1,
        'testimony2':testimony2,
        'form':form

    }
    return render(request,'main/about.html',params)

def affiliate(request):
    if request.method == 'POST':
        form = AffiliatePartnerForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect(affiliate_success)
    else:
        form = AffiliatePartnerForm()
    params ={
        'form':form
    }
    return render(request,'main/affiliate.html',params)

def affiliate_success(request):

    return render(request,'main/affiliate_success.html')

def CategoryCourse(request,category_id):
    categorie = Category.objects.get(id=category_id)
    courses = Course.objects.filter(category=categorie)

    params={
        'categorie':categorie,
        'courses':courses
    }
    return render(request,'main/coursebycategory.html',params)


def my_view(request):
    lang = request.LANGUAGE_CODE  # Retrieve user's preferred language
    activate(lang)  # Activate the user's preferred language


def enquire(request):
    if request.method == 'POST':
        form = EnquireModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(enroll_success)  # Replace 'success_page' with the name of your success URL pattern
    else:
        form = EnquireModelForm()
    params ={
        'form':form,
    }
    return render(request,'main/enquire.html',params)