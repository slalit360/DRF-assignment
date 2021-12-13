from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *


class AnswerAdmin(SimpleHistoryAdmin):
    list_display = (
        'id',
        'query',
        'answer',
        'answered_by',
    )
    search_fields = (
        'query',
        'answer',
    )


class QueryAdmin(SimpleHistoryAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'user',
    )
    search_fields = (
        'title',
        'description',
    )


# Register your models here.
admin.site.register(Query, QueryAdmin)
admin.site.register(Answer, AnswerAdmin)
