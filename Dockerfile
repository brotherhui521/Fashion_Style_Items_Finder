# FROM python:3.11
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# EXPOSE 8000
# CMD ["uvicorn", "main:fastapp", "--host", "0.0.0.0","--port", "8000"]


FROM python:3.11-slim

WORKDIR /app

# Install deps first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# Copy app code last
COPY . .

EXPOSE 8000
CMD ["sh","-c","uvicorn main:fastapp --host 0.0.0.0 --port ${PORT:-8000}"]
