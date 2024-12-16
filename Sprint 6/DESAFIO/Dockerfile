FROM python:3.8

WORKDIR /app

COPY envia.py .
COPY movies.csv .
COPY series.csv .

RUN pip install boto3

CMD ["python", "envia.py"]
