from django.contrib import admin
from .models import User, Urls


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'httpurl', 'pub_date', 'count')
    ordering = ('-pub_date',)


admin.site.register(Urls, UrlsAdmin)
admin.site.register(User)
