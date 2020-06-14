from django.contrib import admin
from .models import Vote, Choice1, Choice2, Comment

# Register your models here.
class ChoiceInline1(admin.TabularInline):
    model = Choice1

class ChoiceInline2(admin.TabularInline):
    model = Choice2

class CommentInline(admin.TabularInline):
    model = Comment

class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    inlines = [ChoiceInline1, ChoiceInline2, CommentInline]

admin.site.register(Vote, VoteAdmin)
