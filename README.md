![](http://pinaxproject.com/pinax-design/patches/pinax-waitinglist.svg)


# Pinax Waiting List

[![](https://img.shields.io/pypi/v/pinax-waitinglist.svg)](https://pypi.python.org/pypi/pinax-waitinglist/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-waitinglist.svg)](https://circleci.com/gh/pinax/pinax-waitinglist)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-waitinglist.svg)](https://codecov.io/gh/pinax/pinax-waitinglist)
[![](https://img.shields.io/github/contributors/pinax/pinax-waitinglist.svg)](https://github.com/pinax/pinax-waitinglist/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-waitinglist.svg)](https://github.com/pinax/pinax-waitinglist/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-waitinglist.svg)](https://github.com/pinax/pinax-waitinglist/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

* [About Pinax](#about-pinax)
* [Overview](#overview)
  * [Supported Django and Python versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Settings](#settings)
  * [Usage](#usage)
  * [Reference](#reference)  
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)
  
## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## pinax-waitinglist

``pinax-waitinglist`` is an app for Django sites for collecting user emails on
a waiting list before a site has launched. It also provides basic survey
capabilities to gather information from your potential users.

For an out-of-the-box Django project already set up with ``pinax-waitinglist``
and Bootstrap templates, see the Pinax ``waitinglist`` starter project.

### Overview

#### Supported Django and Python versions

Django \ Python | 2.7 | 3.4 | 3.5 | 3.6
--------------- | --- | --- | --- | ---
1.11 |  *  |  *  |  *  |  *  
2.0  |     |  *  |  *  |  *


## Documentation

### Installation

Install the development version:

```commandline
$ pip install pinax-waitinglist
```

Add `pinax-waitinglist` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = (
    # other apps
    "pinax.waitinglist",
)
```

Run migrations:

```commandline
$ python manage.py migrate
```

Add `pinax.waitinglist.urls` to your project urlpatterns:

```python
urlpatterns = [
    # other urls
    url(r"^waitinglist/", include("pinax.waitinglist.urls", namespace="pinax_waitinglist")),
]
```

### Settings

#### WAITINGLIST_SURVEY_SECRET

Defaults to `SECRET_KEY`

This is used for generating the hash for `pinax.waitinglist.models.SurveyInstance.code`.

#### DEFAULT_HTTP_PROTOCOL

Defaults to `HTTP`

Provided as context in certain emails for URL building.

### Usage

#### List Signup

The most basic usage would be to direct users to a page where they can provide their email address to be notified of updates:

Add a TemplateView for a landing page to your `urls.py`:

```python
# project/urls.py

from django.views.generic import TemplateView

urlpatterns = [
    # other urls
    url(r"^$", TemplateView.as_view(template_name="waitinglist/list_signup.html"), name="home"),
]
```

Update your template directories in `settings.py`:

```python
# project/settings.py
TEMPLATES = [
    {
        'DIRS': [
            # other dirs
            os.path.join(BASE_DIR, "templates"),
        ],
    },
]
```

Add `list_signup.html` template:

```djangotemplate
<!-- templates/waitinglist/list_signup.html -->

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
```

Add a success template `success.html`:

```djangotemplate
<!-- templates/waitinglist/success.html -->

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
```

#### Survey

If you would like to offer a survey after users enter their email:

A survey will need to be created with one or more questions. Surveys and their questions are accessed through the admin interface.

    # Add a survey
    /admin/waitinglist/survey/

    # Add questions to an existing survey
    /admin/waitinglist/surveyquestion/


Add `survey.html` template:

```djangotemplate
<!-- templates/waitinglist/survey.html -->

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
```

#### Email Survey to existing emails

Existing emails can be emailed surveys through a django command, `mail_out_survey_links`
.

A `SITE` object is passed to both of the following templates, if you haven't enabled the sites framework yet, you will need to do so before proceeding. Additional information on enabling can be found at [The “sites” framework](https://docs.djangoproject.com/en/dev/ref/contrib/sites/).

Add `survey_invite_subject.txt` template:

```djangotemplate
    {# templates/waitinglist/survey_invite_subject.txt #}

    Survey from {{ site.name }}
```

Add `survey_invite_body.txt` template:

```djangotemplate
    {# templates/waitinglist/survey_invite_body.txt #}

    Please take a moment to complete a brief survey from Example.com:
    {{ protocol }}://www.{{ site.domain }}{% url 'waitinglist_survey' instance.code %}
```

Send survey emails:

```commandline
$ python manage.py mail_out_survey_links
```


#### Campaigns and Referrals

Campaigns work by just taking the querystring parameter `wlc` if present in querystring and records
the value to the waitinglist entry.  This is useful if you want to track conversions of a particular
ad campaign.  You can set, for instance, https://mysite.com/?wlc=c1, as the url for the ad. when
people click on the ad, and signup, `c1` will be added to their entry and is viewable in the admin.

Referrals work the same as campaigns but work automatically.  If there a value in `request.META["HTTP_REFERER"]`
when landing on the signup page, the value will get required in the `referral` field of the waitinglist entry.


### Reference

#### Management Commands

##### waitinglist.management.commands.mail_out_survey_links

Email links to survey instances for those that never saw a survey. Retrieves the currently active `Survey`, and filters `WaitingListEntry` where `SurveyInstance` is null.

Uses templates `waitinglist/survey_invite_subject.txt` & `waitinglist/survey_invite_body.txt` for emails.

#### Templates

All the templates for this app should be located in the subfolder `waitinglist/` in your template search path.

##### waitinglist/_list_signup.html

Rendered by `ajax_list_signup` view when form is not valid and gets passed `form` (`WaitingListEntryForm`) in context.

##### waitinglist/_success.html

Rendered by `ajax_list_signup` view when form is valid.

##### waitinglist/list_signup.html

Rendered by `list_signup` view and gets passed `form` (`WaitingListEntryForm`) in context.

##### waitinglist/success.html

Rendered by `django.views.generic.TemplateView`.

##### waitinglist/survey.html

Rendered by `survey` view when request method is `GET` and gets passed `form` (`SurveyForm`) in context.

##### waitinglist/survey_invite_body.txt

Rendered by `mail_out_survey_links` command and gets passed `instance` (`SurveyInstance` instance), `site` (`Site` instance) and `protocol` (`DEFAULT_HTTP_PROTOCOL` setting).

##### waitinglist/survey_invite_subject.txt

Rendered by `mail_out_survey_links` command and gets passed `instance` (`SurveyInstance` instance), `site` (`Site` instance) and `protocol` (`DEFAULT_HTTP_PROTOCOL` setting).

##### waitinglist/thanks.html

Rendered by `django.views.generic.TemplateView`.

#### Signals

##### waitinglist.signals.answered_survey

Triggedered when a user completes a survey through `SurveyForm` which is used with `survey` view.

Provides argument `form` (`SurveyForm` instance).

##### waitinglist.signals.signed_up

Triggered when a user signs up through `ajax_list_signup` or `list_signup` views.

Provides argument `entry` (`WaitingListEntry` instance).


## Change Log

### 2.0.2

* Update CI configuration
* Remove docs build support
* Improve documentation markup

### 2.0.1

* Fix setup.py LONG_DESCRIPTION for PyPi

### 2.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.8, 1.9, 1.10 and Python 3.3 support
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description
* Move documentation to README.md

### 1.3.1

- fixed problem with survey choices in Python 3

### 1.3.0

- added campaign tracking
- added referral tracking

### 1.2.0

- added a simple management command to export waitinglist entries

### 1.1.1

- fixed paths in mail out email management command

### 1.1.0

- don't show empty label in radio choice survey questions


## Contribute

For an overview on how contributing to Pinax works read this [blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/)
and watch the included video, or read our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section.
For concrete contribution ideas, please see our
[Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our [Pinax Slack team](http://slack.pinaxproject.com)
and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course
also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our blog post on [Open Source and Self-Care](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).

## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project
has a [code of conduct](http://pinaxproject.com/pinax/code_of_conduct/).
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject)
and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-2018 James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
