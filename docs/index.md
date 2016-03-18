# pinax-waitinglist

A waiting list app for Django sites.

!!! note "Pinax Ecosystem"
    This app was developed as part of the Pinax ecosystem but is just a Django app
    and can be used independently of other Pinax apps.
    
    To learn more about Pinax, see <http://pinaxproject.com/>

## Quickstart

!!! note "Pinax Starter Projects"
    Utilizing Pinax Starter Projects would offer the quickest way to get started. Additional information on getting up and running with a starter project can be found in the [Pinax Documentation](http://pinaxproject.com/pinax/pinax_starter_projects/).

Install the development version:

    pip install pinax-waitinglist

Add `pinax-waitinglist` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        "pinax.waitinglist",
        # ...
    )

Run migrations:

    python manage.py migrate

Add entry to your `urls.py`:

    url(r"^waitinglist/", include("pinax.waitinglist.urls"))

## Finding Help

The primary place to find a helpful hand would be in our [Slack](http://slack.pinaxproject.com/)
instance. Ask around in `#general` or `#pinax-waitinglist` channels there if you
need anything at all.

If you think you encountered a bug, either in the code, or in the docs (after
all, if something is not clear in the docs, then it should be considered a
bug in the documentation, most of the time), then please [file an issue](https://github.com/pinax/pinax-waitinglist/issues) with the project.