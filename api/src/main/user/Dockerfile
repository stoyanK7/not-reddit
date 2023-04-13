FROM python:3.11-slim-bullseye

LABEL org.opencontainers.image.source="https://github.com/stoyanK7/not-reddit"
LABEL org.opencontainers.image.description="Not-reddit user service API"
LABEL org.opencontainers.image.licenses="GPL-3.0"

WORKDIR /app

COPY ./user/requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./*.py /app/src/main/

COPY ./user/ /app/src/main/user/

CMD ["uvicorn", "src.main.user.main:app", "--host", "0.0.0.0", "--port", "8080"]
