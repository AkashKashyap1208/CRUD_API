from django.contrib import admin
from . models import Dropdown

# Register your models here.
# class MemberAdmin(admin.ModelAdmin):
# 	list_display = ("designation_name",)
# 	prepopulated_fields={"slug" : ["designation_name",]}


admin.site.register(Dropdown)