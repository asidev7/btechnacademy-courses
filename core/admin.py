from django.contrib import admin

from core.models import FAQ, Category, Company, Contact, Course, EnquireModel, Service, Testimony

# Register your models here.
admin.site.register(Service)
admin.site.register(FAQ)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Testimony)
admin.site.register(Contact)
admin.site.register(Company)
admin.site.register(EnquireModel)