from django.contrib import admin
from main.models import SharedFiles


class SharedFilesAdmin(admin.ModelAdmin):
    list_display = ('filename', 'slug', 'fileid', 'upload_time', 'expiration_time', 'is_expired')
    list_filter = ('upload_time', 'expiration_time')
    search_fields = ('filename', 'slug', 'fileid')
    ordering = ('upload_time', 'expiration_time')


admin.site.register(SharedFiles, SharedFilesAdmin)

# Register your models here.
