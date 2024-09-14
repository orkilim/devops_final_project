FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

COPY Scores.txt /Scores.txt

EXPOSE 5000

ENV FLASK_APP=MainScores.py

CMD ["flask", "run", "--host=0.0.0.0"]
