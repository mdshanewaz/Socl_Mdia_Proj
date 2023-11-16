from django.contrib import admin
from Posts_App.models import PostModel, LikeModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(LikeModel)