FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

ARG USER_ID=0

RUN mkdir -p /home/appuser
RUN chown -R ${USER_ID}:${USER_ID} /home/appuser

RUN groupadd -r appuser
RUN useradd -r -u ${USER_ID} -g appuser appuser



COPY requirements.txt /code/
RUN pip install -r requirements.txt


COPY . /code/

USER appuser