FROM python:3-slim

RUN pip install anonfile
COPY upload.py /app/upload.py

ENTRYPOINT ["python", "/app/upload.py"]
