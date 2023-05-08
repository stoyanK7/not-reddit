FROM python:3.11-slim-bullseye

LABEL org.opencontainers.image.source="https://github.com/stoyanK7/not-reddit"
LABEL org.opencontainers.image.description="Not-reddit authentication service API"
LABEL org.opencontainers.image.licenses="GPL-3.0"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

COPY ./auth/requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./shared/ /app/src/main/shared/

COPY ./auth/ /app/src/main/auth/

CMD ["uvicorn", "src.main.auth.main:app", "--host", "0.0.0.0", "--port", "8080"]
