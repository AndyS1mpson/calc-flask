FROM python:3.8

EXPOSE 5000

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . ./

RUN python -m pip install -r ./requirements.txt

#ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "app:app"]