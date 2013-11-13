from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# Register your models here.
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question']
    fieldsets = [
            (None, {'fields' : ['question']}),
            ('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
            ]
    inlines = [ChoiceInline]

#admin.site.register(Poll)
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
