FROM python:3.12-alpine

WORKDIR /app

# Dependências mínimas
RUN apk add --no-cache gcc musl-dev linux-headers

COPY app/ /app/

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "app.py"]
