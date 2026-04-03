# builder stage
FROM python:3.14-alpine3.23 as builder
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# final stage
FROM python:3.14-alpine3.23

ARG VERSION="0.0.1"
ARG VCS_REF
ARG BUILD_DATE

LABEL org.opencontainers.image.title="Links as Code" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.authors="Dennis Roth" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.source="https://github.com/rothdennis/links-as-code" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.created="${BUILD_DATE}"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBUG=0
ENV DATA_DIR=/app/data

RUN addgroup -S appgroup \
    && adduser  -S appuser -G appgroup

COPY --from=builder /install /usr/local

WORKDIR /app
RUN mkdir -p /app/data && chown -R appuser:appgroup /app/data

COPY src/ .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER appuser

EXPOSE 9000

ENTRYPOINT ["/entrypoint.sh"]