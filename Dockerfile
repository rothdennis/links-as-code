FROM python:3.14-alpine3.23

RUN apk add nginx
COPY configs/nginx.conf /etc/nginx/nginx.conf

WORKDIR /app
RUN mkdir -p /app/data

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .

ENV DEBUG=0
ENV DATA_DIR=/app/data

EXPOSE 9010

CMD ["sh", "-c", "nginx && python main.py"]