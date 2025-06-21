FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    espeak \
    libsndfile1 \
    build-essential \
    cmake \
    g++ \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install --use-pep517 --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
