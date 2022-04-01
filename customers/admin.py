from django.contrib import admin
from .models import (
                     Customer,
                     SubjectCategory,
                     Subject,
                     Progress,
                     ProgressItem
                    )


class ProgressItemsAdminInline(admin.TabularInline):
    model = ProgressItem
    list_display = (
        'subject',
        'score',
        'comments',
        'practice_next_lesson',
    )


class ProgressAdmin(admin.ModelAdmin):
    inlines = (ProgressItemsAdminInline,)


class SubjectAdminInline(admin.TabularInline):
    model = Subject


class SubjectCategoryAdmin(admin.ModelAdmin):
    inlines = (SubjectAdminInline,)


admin.site.register(Customer)
admin.site.register(SubjectCategory, SubjectCategoryAdmin)
admin.site.register(Progress, ProgressAdmin)
