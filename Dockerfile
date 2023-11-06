FROM python:3.10.12-slim-buster

RUN apt update

RUN python3 -m pip install --no-cache-dir --disable-pip-version-check pipenv

# Environment variables
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PIPENV_VENV_IN_PROJECT=1 \
    TZ=Asia/Tokyo

# Port
EXPOSE 8000

# Container variables
ARG project_name="community-place-for-cats-extension-api"
ARG application_name="src"
ARG build_arg="prod"

# Create work directory
ENV build_arg=${build_arg}
RUN mkdir -p /code/$project_name/$application_name
WORKDIR /code/$project_name

# Move Artifact to work directory
COPY ./Pipfile /code/$project_name
WORKDIR /code/$project_name/$application_name
COPY ./$application_name /code/$project_name/$application_name
WORKDIR /code/$project_name

# Install module
RUN pipenv sync
WORKDIR /code/$project_name/$application_name

# Execute server
COPY ./startup.sh /code/
RUN chmod 777 /code/$project_name/$application_name
RUN chmod 777 /code/startup.sh

CMD ["/code/startup.sh"]
