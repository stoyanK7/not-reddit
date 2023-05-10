FROM python:3.11-slim-bullseye

LABEL org.opencontainers.image.source="https://github.com/stoyanK7/not-reddit"
LABEL org.opencontainers.image.description="Not-reddit post service API"
LABEL org.opencontainers.image.licenses="GPL-3.0"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

COPY ./src/__init__.py /app/src/__init__.py

COPY ./src/main/__init__.py /app/src/main/__init__.py

COPY ./src/main/post/requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src/main/shared/ /app/src/main/shared/

COPY ./src/main/post/ /app/src/main/post/

CMD ["uvicorn", "src.main.post.main:app", "--host", "0.0.0.0", "--port", "80"]
