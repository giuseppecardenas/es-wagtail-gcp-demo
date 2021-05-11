Static File Generation PoC
=======================

PoC for building static files when publishing pages or on-demand as an option in the wagtail admin.

It uses:

- The [wagtail-bakery](https://github.com/wagtail/wagtail-bakery) library.
- The [django-storages](https://django-storages.readthedocs.io/en/latest/backends/gcloud.html) library. (For saving files to and from GCP buckets.)

### Running the PoC

This PoC uses docker. You can run

```bash
$ docker-compose -f infrastructure/docker/local/docker-compose.yml up
```

and this will start the application on port 8000. Note that you also have to run

```bash
$ docker-compose run app /venv/bin/python manage.py migrate
$ docker-compose run app /venv/bin/python manage.py load_initial_data
```

for populating the database beforehand.
