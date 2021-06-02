FROM python:3-slim

RUN pip install requests
COPY upload.py /app/upload.py

ENTRYPOINT ["python", "/app/upload.py"]
