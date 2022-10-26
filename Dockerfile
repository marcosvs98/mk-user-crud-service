FROM python:3.9

USER root

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    ca-certificates \
    locales locales-all \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN locale-gen pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt_br
ENV LC_ALL pt_BR.UTF-8

COPY --chown=userapp:userapp . .

RUN pip install --no-cache -U pip poetry && poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi -vvv


CMD ["python", "src/main.py"]
