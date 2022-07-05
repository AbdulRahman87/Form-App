from django.contrib import admin
from .models import Categories, Question, user_details, question_reply, ContactUs
# Register your models here.

admin.site.register(Categories)
admin.site.register(Question)
admin.site.register(user_details)
admin.site.register(question_reply)
admin.site.register(ContactUs)