FROM python:3.12-slim-bookworm AS builder

# Variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Install build dependencies for mysqlclient
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    default-libmysqlclient-dev \
    pkg-config \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim-bookworm

# Install runtime dependencies for mysqlclient
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar librerías y binarios desde el builder
COPY --from=builder /usr/local /usr/local

COPY . /app

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

WORKDIR /app/todo_list

ENTRYPOINT ["/app/entrypoint.sh"]


