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
* [Important Links](#important-links)
* [Overview](#overview)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Settings](#settings)
  * [Reference](#reference)  
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)
  
  
## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## Important Links

Where you can find what you need:
* Releases: published to [PyPI](https://pypi.org/search/?q=pinax) or tagged in app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Global documentation: [Pinax documentation website](https://pinaxproject.com/pinax/)
* App specific documentation: app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Support information: [SUPPORT.md](https://github.com/pinax/.github/blob/master/SUPPORT.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Contributing information: [CONTRIBUTING.md](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Current and historical release docs: [Pinax Wiki](https://github.com/pinax/pinax/wiki/)


## pinax-waitinglist

### Overview

``pinax-waitinglist`` is an app for Django sites for collecting user emails on
a waiting list before a site has launched. It also provides basic survey
capabilities to gather information from your potential users.

For an out-of-the-box Django project already set up with ``pinax-waitinglist``
and Bootstrap templates, see the Pinax ``waitinglist`` starter project.

#### Supported Django and Python Versions

Django / Python | 3.6 | 3.7 | 3.8
--------------- | --- | --- | ---
2.2  |  *  |  *  |  *
3.0  |  *  |  *  |  *


## Documentation

### Installation

To install pinax-waitinglist:

```shell
$ pip install pinax-waitinglist
```

Add `pinax.waitinglist` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    # other apps
    "pinax.waitinglist",
]
```

Run migrations:

```shell
$ python manage.py migrate
```

Add `pinax.waitinglist.urls` to your project urlpatterns:

```python
urlpatterns = [
    # other urls
    url(r"^waitinglist/", include("pinax.waitinglist.urls", namespace="pinax_waitinglist")),
]
```

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

```django
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

```django
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

```django
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

```django
    {# templates/waitinglist/survey_invite_subject.txt #}

    Survey from {{ site.name }}
```

Add `survey_invite_body.txt` template:

```django
    {# templates/waitinglist/survey_invite_body.txt #}

    Please take a moment to complete a brief survey from Example.com:
    {{ protocol }}://www.{{ site.domain }}{% url 'waitinglist_survey' instance.code %}
```

Send survey emails:

```shell
$ python manage.py mail_out_survey_links
```

#### Campaigns and Referrals

Campaigns work by just taking the querystring parameter `wlc` if present in querystring and records
the value to the waitinglist entry.  This is useful if you want to track conversions of a particular
ad campaign.  You can set, for instance, https://mysite.com/?wlc=c1, as the url for the ad. when
people click on the ad, and signup, `c1` will be added to their entry and is viewable in the admin.

Referrals work the same as campaigns but work automatically.  If there a value in `request.META["HTTP_REFERER"]`
when landing on the signup page, the value will get required in the `referral` field of the waitinglist entry.

### Settings

#### WAITINGLIST_SURVEY_SECRET

Defaults to `SECRET_KEY`

This is used for generating the hash for `pinax.waitinglist.models.SurveyInstance.code`.

#### DEFAULT_HTTP_PROTOCOL

Defaults to `HTTP`

Provided as context in certain emails for URL building.

### Reference

#### Management Commands

##### waitinglist.management.commands.mail_out_survey_links

Email links to survey instances for those that never saw a survey. Retrieves the currently active `Survey`, and filters `WaitingListEntry` where `SurveyInstance` is null.

Uses templates `waitinglist/survey_invite_subject.txt` & `waitinglist/survey_invite_body.txt` for emails.

#### Templates

Default templates are provided by the `pinax-templates` app in the
[waitinglist](https://github.com/pinax/pinax-templates/tree/master/pinax/templates/templates/pinax/waitinglist)
section of that project.

Reference pinax-templates
[installation instructions](https://github.com/pinax/pinax-templates/blob/master/README.md#installation)
to include these templates in your project.

View live `pinax-templates` examples and source at [Pinax Templates](https://templates.pinaxproject.com/waitinglist/fragments/)!

##### Customizing Templates

Override the default `pinax-templates` templates by copying them into your project
subdirectory `pinax/waitinglist/` on the template path and modifying as needed.

For example if your project doesn't use Bootstrap, copy the desired templates
then remove Bootstrap and Font Awesome class names from your copies.
Remove class references like `class="btn btn-success"` and `class="icon icon-pencil"` as well as
`bootstrap` from the `{% load i18n bootstrap %}` statement.
Since `bootstrap` template tags and filters are no longer loaded, you'll also need to update
`{{ form|bootstrap }}` to `{{ form }}` since the "bootstrap" filter is no longer available.

##### `_list_signup.html`

Rendered by `ajax_list_signup` view when form is not valid and gets passed `form` (`WaitingListEntryForm`) in context.

##### `_success.html`

Rendered by `ajax_list_signup` view when form is valid.

#### User-Provided Templates

Create these templates in a `pinax/waitinglist/` subfolder in your template search path.

##### `list_signup.html`

Rendered by `list_signup` view and gets passed `form` (`WaitingListEntryForm`) in context.

##### `success.html`

Rendered by `django.views.generic.TemplateView`.

##### `survey.html`

Rendered by `survey` view when request method is `GET` and gets passed `form` (`SurveyForm`) in context.

##### `survey_invite_body.txt`

Rendered by `mail_out_survey_links` command and gets passed `instance` (`SurveyInstance` instance), `site` (`Site` instance) and `protocol` (`DEFAULT_HTTP_PROTOCOL` setting).

##### `survey_invite_subject.txt`

Rendered by `mail_out_survey_links` command and gets passed `instance` (`SurveyInstance` instance), `site` (`Site` instance) and `protocol` (`DEFAULT_HTTP_PROTOCOL` setting).

##### `thanks.html`

Rendered by `django.views.generic.TemplateView` after successfully adding user to waiting list.

#### Signals

##### waitinglist.signals.answered_survey

Triggedered when a user completes a survey through `SurveyForm` which is used with `survey` view.

Provides argument `form` (`SurveyForm` instance).

##### waitinglist.signals.signed_up

Triggered when a user signs up through `ajax_list_signup` or `list_signup` views.

Provides argument `entry` (`WaitingListEntry` instance).


## Change Log

### 3.0.1

* Add an admin action to export the waiting list as csv 

### 3.0.0

* Drop Django 1.11, 2.0, and 2.1, and Python 2,7, 3.4, and 3.5 support
* Add Django 2.2 and 3.0, and Python 3.6, 3.7, and 3.8 support
* Update packaging configs
* Direct users to community resources

### 2.0.3

* Fix render_to_string `context_instances` kwarg 
* Fix setup.py `package_data` reference for included templates
* Add pinax-templates support

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

[Contributing](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) information can be found in the [Pinax community health file repo](https://github.com/pinax/.github).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a [Code of Conduct](https://github.com/pinax/.github/blob/master/CODE_OF_CONDUCT.md). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject) and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-present James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
