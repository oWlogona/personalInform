from django.contrib import admin
from itemListBar.models import UserCardsModel


class UserCardsModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserCardsModel._meta.fields]


admin.site.register(UserCardsModel, UserCardsModelAdmin)
