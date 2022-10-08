from django.contrib import admin
from api.models import User, FeedBack, Marketing, ResearchLab, BookRide

# Register your models here.
# admin.site.register(User)

from django.contrib import admin
from django.contrib.auth import get_user_model

user = get_user_model()

admin.site.register(user)

admin.site.register(FeedBack)
admin.site.register(Marketing)
admin.site.register(ResearchLab)
admin.site.register(BookRide)
