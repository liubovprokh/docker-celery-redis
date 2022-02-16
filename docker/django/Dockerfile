FROM python:3.10-alpine


ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PIPENV_SHELL_COMPAT=true \
  PIPENV_COLORBLIND=true \
  PIPENV_NOSPIN=true

# System deps:
RUN apk update \
    && apk add \
      bash \
      build-base \
      curl \
      gcc \
      gettext \
      git \
      libffi-dev \
      linux-headers \
      musl-dev \
      postgresql-dev \
      tini \
      jpeg-dev \
      zlib-dev \
      freetype-dev \
      lcms2-dev \
      openjpeg-dev \
      tiff-dev \
      tk-dev \
      tcl-dev \
      harfbuzz-dev \
      fribidi-dev && rm -vrf /var/cache/apk/*

RUN mkdir /app
WORKDIR /app

# Add requirements.txt before rest of repo for caching
ADD ./src/requirements.txt ./src/requirements.txt
RUN pip install -r ./src/requirements.txt
ADD ./src ./src
ADD ./docker/django/run.sh ./docker/django/run.sh
