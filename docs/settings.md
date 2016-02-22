# Settings & Configuration

## Settings

### WAITINGLIST_SURVEY_SECRET

Defaults to `SECRET_KEY`

This is used for generating the hash for `pinax.waitinglist.models.SurveyInstance.code`.

### DEFAULT_HTTP_PROTOCOL

Defaults to `HTTP`

Provided as context in certain emails for URL building.