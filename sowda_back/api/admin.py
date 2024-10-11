from django.contrib import admin
from .models import *
from elin.models import *
from service.models import *
from other.models import *
from logist.models import *
from car.models import *
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList
from django.urls import reverse
from django.contrib.admin.utils import quote
from django.utils.translation import gettext_lazy as _

class LogistImageInline(admin.StackedInline):
    model = ImageLogist
    fields = ["img"]

class LogistAdmin(admin.ModelAdmin):
    list_display = ('author','name','price','phone','img','surat','checked')
    inlines=[LogistImageInline]

    def surat(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return 'Surat goyulmadyk'
admin.site.register(Logist, LogistAdmin)

class ElinImageInline(admin.StackedInline):
    model = ImageElin
    fields = ["img"]

class ElinAdmin(admin.ModelAdmin):
    list_display = ('author','name','price','phone','img','surat','checked')
    inlines = [ElinImageInline]

    def surat(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

admin.site.register(Elin, ElinAdmin)

class OtherImageInline(admin.StackedInline):
    model = ImageOther
    fields = ["img"]

class OtherAdmin(admin.ModelAdmin):
    list_display = ('author','name','price','phone','img','surat','checked')
    inlines = [OtherImageInline]

    def surat(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

admin.site.register(Other, OtherAdmin)

class CarImageInline(admin.StackedInline):
    model = ImageCar
    fields = ["img"]

class CarAdmin(admin.ModelAdmin):
    list_display = ('author','created','name','price','phone','img','surat','checked')
    inlines = [CarImageInline]

    def surat(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

admin.site.register(Car, CarAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name','img','surat','checked')

    def surat(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

admin.site.register(News, NewsAdmin)

class ServiceImageInline(admin.StackedInline):
    model = ImageService
    fields = ["img"]

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('author','name','price','phone','img','surat','checked')
    inlines = [ServiceImageInline]
    
    def surat(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

class TopImageInline(admin.StackedInline):
    model = ImageTop
    fields = ["img"]

class TopProductsAdmin(admin.ModelAdmin):
    list_display = ('name','author','price','phone','img','surat','checked')
    inlines = [TopImageInline]
    
    def surat(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return 'Surat goyulmadyk'

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('name','pk','surat')
    
    def surat(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="75">')
        else:
            return 'Surat goyulmadyk'



admin.site.register(TopProducts, TopProductsAdmin)
admin.site.register(ImageTop)
admin.site.register(Service, ServiceAdmin)
admin.site.register(CarouselImage,CarouselAdmin)
admin.site.register(Address)
admin.site.register(CarCategory)
admin.site.register(ElinCategory)
admin.site.register(LogistCategory)
admin.site.register(ServiceCategory)
admin.site.register(NewsCategory)
admin.site.register(OtherCategory)
admin.site.register(UserProd)

admin.site.site_title = 'Seýir'
admin.site.site_header = 'Seýir'
