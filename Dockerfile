FROM python:3.11-slim

COPY ./app /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN alembic revision --autogenerate -m "First migration"
RUN alembic upgrade head

CMD python main.py
