FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv pip compile pyproject.toml -o requirements.txt && \
    uv pip install --system -r requirements.txt && \
    rm requirements.txt

COPY kerminal ./kerminal

EXPOSE 8000

CMD ["python", "-m", "kerminal.api.main"]
