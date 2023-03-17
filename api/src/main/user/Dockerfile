FROM python:3.10-slim-bullseye

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src/main/*.py /app/src/main/

COPY ./src/main/user/.env /app/src/main

COPY ./src/main/user/*.py /app/src/main/user/

CMD ["uvicorn", "src.main.user.main:app", "--host", "0.0.0.0", "--port", "8082"]