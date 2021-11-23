from django.contrib import admin
from .models import FeedRecord


class FeedRecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'symbol_type', )
    search_fields = ['title']


admin.site.register(FeedRecord, FeedRecordAdmin)
