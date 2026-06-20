FROM python:3.12-slim

WORKDIR /app

# 1. copy requirements first
COPY requirements.txt .

# 2. install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 3. copy full project
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]