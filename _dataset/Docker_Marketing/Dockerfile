# 1) Base ligera de Python
FROM python:3.9-slim

# 2) Instalo libs del SO para compilar extensiones Python (p.ej. xgboost)
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      gcc \
      python3-dev \
      libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# 3) Defino el directorio de trabajo
WORKDIR /app

# 4) Copio sólo requirements y actualizo pip
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 5) Copio el resto de la app
COPY . .

# 6) Exposición del puerto Flask
EXPOSE 4000

# 7) Uso Gunicorn en vez de flask run (más estable en producción)
CMD ["gunicorn","-w","4","-b","0.0.0.0:4000","app:app"]
