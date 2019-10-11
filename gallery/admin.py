from django.contrib import admin
from .models import ibyiciro,Ahanu,Pics

# Register your models here.
# class PicseAdmin(admin.ModelAdmin):
#     filter_horizontal =('Ahanu',)

admin.site.register(ibyiciro)
admin.site.register(Ahanu)
admin.site.register(Pics)