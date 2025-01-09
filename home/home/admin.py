from django.contrib import admin
from .models import Setting, ContactMessage, Language
from ..models import SettingLang


# Register your models here.

class SettigsAdmin(admin.ModelAdmin):
    list_display = ["title"]
admin.site.register(Setting, SettigsAdmin)


admin.site.register(ContactMessage)
admin.site.register(Language,LanguagesAdmin)
admin.site.register(SettingLang)
