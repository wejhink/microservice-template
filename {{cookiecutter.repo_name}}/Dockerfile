# install lims microservice

FROM google/python-runtime
MAINTAINER {{cookiecutter.full_name}}

ENTRYPOINT ["/env/bin/gunicorn", "-b :8080", "wsgi_gunicorn:app"]
