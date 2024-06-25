from django.contrib import admin
from .models import *
from elin.models import *
from service.models import *
from other.models import *
from logist.models import *
from car.models import *
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList

class LogistAdmin(admin.ModelAdmin):
    list_display = ('name','price','phone','img1')

    def get_photo(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img1.url}" width="75">')
        else:
            return 'Surat goyulmadyk'
admin.site.register(Logist, LogistAdmin)


class ElinAdmin(admin.ModelAdmin):
    list_display = ('name','price','phone','img1')

    def get_photo(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img1.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

admin.site.register(Elin, ElinAdmin)

class OtherAdmin(admin.ModelAdmin):
    list_display = ('name','price','phone','img1')

    def get_photo(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img1.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

admin.site.register(Other, OtherAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('checked','name','price','phone','img1')

    def get_photo(self, obj):
        if obj.img1:
            return mark_safe(f'<img src="{obj.img1.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

admin.site.register(Car, CarAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name','img')

    def get_photo(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

admin.site.register(News, NewsAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','price','phone','img1')
    
    def get_photo(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img1.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

class TopProductsAdmin(admin.ModelAdmin):
    list_display = ('name','price','phone','img1')
    
    def get_photo(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img1.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

admin.site.register(TopProducts, TopProductsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(CarouselImage)
admin.site.register(Address)
admin.site.register(UserProd    )
admin.site.register(CarCategory)
admin.site.register(ElinCategory)
admin.site.register(LogistCategory)
admin.site.register(ServiceCategory)
admin.site.register(NewsCategory)
admin.site.register(OtherCategory)

admin.site.site_title = 'Seýir'
admin.site.site_header = 'Seýir'
