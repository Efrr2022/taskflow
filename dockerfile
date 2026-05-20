###############################
# Stage 1 — Builder
###############################
FROM python:3.11-slim-bookworm AS builder

WORKDIR /build

COPY app/requirements.txt .

RUN pip install --no-cache-dir --target=/python -r requirements.txt

COPY app/ .

###############################
# Stage 2 — Runtime
###############################
FROM gcr.io/distroless/python3-debian12

WORKDIR /app

COPY --from=builder /python /python

COPY --from=builder /build /app

ENV PYTHONPATH=/python

USER nonroot

EXPOSE 8000

CMD ["-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]