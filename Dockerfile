FROM python:3.12.6-slim-bookworm

EXPOSE 8080

WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./app /src

CMD ["fastapi", "run", "main.py", "--port", "8080"]
