from django.contrib import admin
from .models import (
                     Customer,
                     SubjectCategory,
                     Subject,
                     Progress,
                     ProgressItem
                    )

admin.site.register(Customer)
admin.site.register(SubjectCategory)
admin.site.register(Subject)
admin.site.register(Progress)
admin.site.register(ProgressItem)
