from django.contrib import admin

from .models import INGMutationType


class INGMutationTypeAdmin(admin.ModelAdmin):
    list_display = ('description', 'mutation_type')

admin.site.register(INGMutationType, INGMutationTypeAdmin)
