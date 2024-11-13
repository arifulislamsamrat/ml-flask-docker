FROM python:3.9-slim

RUN pip install mlflow psycopg2-binary boto3

EXPOSE 5000

CMD ["mlflow", "server", \
     "--host", "0.0.0.0", \
     "--port", "5000", \
     "--backend-store-uri", "${MLFLOW_TRACKING_URI}", \
     "--default-artifact-root", "s3://mlflow"]