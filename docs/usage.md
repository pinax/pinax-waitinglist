# Usage

## List Signup

The most basic usage would be to direct users to a page where they can provide their email address to be notified of updates:

Add a TemplateView for a landing page to your `urls.py`:

    # project/urls.py
    from django.views.generic import TemplateView

    urlpatterns = [
        [...]
        url(r"^$", TemplateView.as_view(template_name="waitinglist/list_signup.html"), name="home"),
    ]

Update your template directories in `settings.py`:

    # project/settings.py
    TEMPLATES = [
        {
            [...]
            'DIRS': [os.path.join(BASE_DIR, "templates"),],
            [...]
        },
    ]

Add `list_signup.html` template:

    <!-- templates/waitinglist/list_signup.html -->

    [...]
    <div class="site-wrapper-inner">
        <div class="cover-container">
            <div class="inner cover">
                <h1 class="cover-heading">Sign up on our waiting list!</h1>
                <p class="lead">
                    Once this site is ready to launch, you will be emailed.
                </p>
                {% if form.email.errors %}
                    <b>{{ form.email.errors.0 }}</b>
                {% endif %}
                {% url "waitinglist_list_signup" as url %}
                <form method="POST" action="{{ url }}" class="form-inline">
                    {% csrf_token %}
                    <div class="form-group">
                        <label class="sr-only" for="id_email">Email address</label>
                        <input type="email" name="email" class="form-control input-lg" id="id_email" placeholder="your@email.com">
                    </div>
                    <button class="btn btn-default btn-lg">Submit</button>
                </form>
            </div>
            <div class="mastfoot">
                <div class="inner">
                    <p>{% include "_footer.html" %}</p>
                </div>
            </div>
        </div>
    </div>
    [...]

Add a success template `success.html`:

    <!-- templates/waitinglist/success.html -->

    [...]
    <div class="site-wrapper-inner">
        <div class="cover-container">
            <div class="inner cover">
                <h1 class="cover-heading">Thank you!</h1>
                <p class="lead">You are on the list. We will notify you know when this site launches.</p>
                <p>
                    If you have any questions, feel free to email <a href="mailto:info@example.com"><b>info@example.com</b></a>.
                </p>
            </div>
            <div class="mastfoot">
                <div class="inner">
                    <p>{% include "_footer.html" %}</p>
                </div>
            </div>
        </div>
    </div>
    [...]

## Survey

If you would like to offer a survey after users enter their email:

A survey will need to be created with one or more questions. Surveys and their questions are accessed through the admin interface.

    # Add a survey
    /admin/waitinglist/survey/

    # Add questions to an existing survey
    /admin/waitinglist/surveyquestion/


Add `survey.html` template:

    <!-- templates/waitinglist/survey.html -->

    [...]
    <div class="site-wrapper-inner">
        <div class="cover-container">
            <div class="inner cover">
                <h1 class="cover-heading">Survey</h1>
                <p class="lead">Do you have a moment to answer a few qustions?</p>
                <form>
                    {% csrf_token %}
                    {{ form }}
                    <button type="submit" class="btn btn-default btn-lg">Submit</button>
                </form>
            </div>
            <div class="mastfoot">
                <div class="inner">
                    <p>{% include "_footer.html" %}</p>
                </div>
            </div>
        </div>
    </div>
    [...]

## Email Survey to existing emails

Existing emails can be emailed surveys through a django command, `mail_out_survey_links`
.

A `SITE` object is passed to both of the following templates, if you haven't enabled the sites framework yet, you will need to do so before proceeding. Additional information on enabling can be found at [The “sites” framework](https://docs.djangoproject.com/en/dev/ref/contrib/sites/).

Add `survey_invite_subject.txt` template:

    # templates/waitinglist/survey_invite_subject.txt

    Survey from {{ site.name }}

Add `survey_invite_body.txt` template:

    # templates/waitinglist/survey_invite_body.txt

    Please take a moment to complete a brief survey from Example.com:
    {{ protocol }}://www.{{ site.domain }}{% url 'waitinglist_survey' instance.code %}

Send survey emails:

    python manage.py mail_out_survey_links


## Campaigns and Referrals

Campaigns work by just taking the querystring parameter `wlc` if present in querystring and records
the value to the waitinglist entry.  This is useful if you want to track conversions of a particular
ad campaign.  You can set, for instance, https://mysite.com/?wlc=c1, as the url for the ad. when
people click on the ad, and signup, `c1` will be added to their entry and is viewable in the admin.

Referrals work the same as campaigns but work automatically.  If there a value in `request.META["HTTP_REFERER"]`
when landing on the signup page, the value will get required in the `referral` field of the waitinglist entry.
