FROM python:3.11-slim-bullseye

LABEL org.opencontainers.image.source="https://github.com/stoyanK7/not-reddit"
LABEL org.opencontainers.image.description="Not-reddit subreddit service API"
LABEL org.opencontainers.image.licenses="GPL-3.0"

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src/main/*.py /app/src/main/

COPY ./src/main/subreddit/*.py /app/src/main/subreddit/

CMD ["uvicorn", "src.main.subreddit.main:app", "--host", "0.0.0.0", "--port", "8080"]
