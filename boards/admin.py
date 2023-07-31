from django.contrib import admin

from . models import Board, Topic

from django.contrib.auth.models import Group

from import_export.admin import ImportExportModelAdmin

class ImportExport(ImportExportModelAdmin):
    pass

class InlineTopic(admin.StackedInline):
    model = Topic
    extra = 1

class BoardAdmin(admin.ModelAdmin):
    inlines = [InlineTopic]

# class TopicAdmin(admin.ModelAdmin):
#     fields = ('subject','board','created_by','views')
#     list_display = ('subject','board','created_by')
#     list_display_links = ['subject','board']
#     list_filter = ('board',)
    

admin.site.register(Board,BoardAdmin)
admin.site.register(Topic,ImportExport)

admin.site.site_header = "Boards Admin Panel"
admin.site.site_title = "Admin Panel"
