from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import (
    Survey,
    SurveyAnswer,
    SurveyInstance,
    SurveyQuestion,
    SurveyQuestionChoice,
    WaitingListEntry,
)


class WaitingListEntryAdmin(admin.ModelAdmin):

    list_display = ["email", "created", "referrer", "campaign"]
    list_filter = ["referrer", "campaign", "created"]
    search_fields = ["email"]
    actions = ["export_waitinglist_entries"]

    def export_waitinglist_entries(self, request, queryset):

        fieldnames = ["email", "created"]

        csv_response = self.make_csv(queryset, fieldnames)

        return csv_response

    export_waitinglist_entries.short_description = "Export waiting list entries to csv"

    def make_csv(self, queryset, fieldnames):

        csv_response = HttpResponse(content_type="text/csv")
        csv_response["Content-Disposition"] = "attachment; filename=waitinglist_entries.csv"

        writer = csv.writer(csv_response)
        writer.writerow(fieldnames)
        for entry in queryset.order_by("created"):
            row = writer.writerow([getattr(entry, field) for field in fieldnames])

        return csv_response


class SurveyInstanceAdmin(admin.ModelAdmin):

    model = SurveyInstance
    list_display = ["survey", "email", "created"]

    def survey(self, obj):
        return obj.survey.label

    def email(self, obj):
        return obj.entry.email

    def created(self, obj):
        return obj.entry.created


class SurveyAnswerAdmin(admin.ModelAdmin):

    model = SurveyAnswer
    list_display = ["survey", "email", "question_label", "value", "value_boolean", "created"]

    def survey(self, obj):
        return obj.instance.survey.label

    def email(self, obj):
        return obj.instance.entry.email

    def question_label(self, obj):
        return obj.question.question


class SurveyQuestionChoiceInline(admin.TabularInline):

    model = SurveyQuestionChoice


class SurveyQuestionAdmin(admin.ModelAdmin):

    model = SurveyQuestion
    list_display = ["survey", "question", "kind", "required"]
    inlines = [SurveyQuestionChoiceInline]

    def survey(self, obj):
        return obj.survey.label


admin.site.register(WaitingListEntry, WaitingListEntryAdmin)

admin.site.register(
    Survey,
    list_display=["label", "active"]
)
admin.site.register(SurveyAnswer, SurveyAnswerAdmin)
admin.site.register(SurveyInstance, SurveyInstanceAdmin)
admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
