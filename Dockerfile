FROM python:3.14-alpine3.23

RUN apk add nginx
COPY configs/nginx.conf /etc/nginx/nginx.conf

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .

EXPOSE 5050

CMD ["python", "src/main.py"]