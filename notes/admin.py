from django.contrib import admin
from .models import Notes


#admin.site.register(Notes)

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    autocomplete_fields=["author"]
    list_display=["author","title","created_date"]

    

