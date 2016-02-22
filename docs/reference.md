# Reference

## Management Commands

#### waitinglist.management.commands.mail_out_survey_links

Email links to survey instances for those that never saw a survey. Retrieves the currently active `Survey`, and filters `WaitingListEntry` where `SurveyInstance` is null.

Uses templates `waitinglist/survey_invite_subject.txt` & `waitinglist/survey_invite_body.txt` for emails.

## Templates

All the templates for this app should be located in the subfolder `waitinglist/` in your template search path.

#### waitinglist/_list_signup.html

Rendered by `ajax_list_signup` view when form is not valid and gets passed `form` (`WaitingListEntryForm`) in context.

#### waitinglist/_success.html

Rendered by `ajax_list_signup` view when form is valid.

#### waitinglist/list_signup.html

Rendered by `list_signup` view and gets passed `form` (`WaitingListEntryForm`) in context.

#### waitinglist/success.html

Rendered by `django.views.generic.TemplateView`.

#### waitinglist/survey.html

Rendered by `survey` view when request method is `GET` and gets passed `form` (`SurveyForm`) in context.

#### waitinglist/survey_invite_body.txt

Rendered by `mail_out_survey_links` command and gets passed `instance` (`SurveyInstance` instance), `site` (`Site` instance) and `protocol` (`DEFAULT_HTTP_PROTOCOL` setting).

#### waitinglist/survey_invite_subject.txt

Rendered by `mail_out_survey_links` command and gets passed `instance` (`SurveyInstance` instance), `site` (`Site` instance) and `protocol` (`DEFAULT_HTTP_PROTOCOL` setting).

#### waitinglist/thanks.html

Rendered by `django.views.generic.TemplateView`.

## Signals

#### waitinglist.signals.answered_survey

Triggedered when a user completes a survey through `SurveyForm` which is used with `survey` view.

Provides argument `form` (`SurveyForm` instance).

#### waitinglist.signals.signed_up

Triggered when a user signs up through `ajax_list_signup` or `list_signup` views.

Provides argument `entry` (`WaitingListEntry` instance).
