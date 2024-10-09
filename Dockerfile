FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./api/requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./api/ /app/

EXPOSE 8000

CMD ["uvicorn", "app:app", "--reload"]
