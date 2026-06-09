FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Debug — test karo dono files chalti hain ya nahi
RUN cd /app && python -c "import sys; sys.path.insert(0, 'api'); import api" || true
RUN cd /app && python -c "import sys; sys.path.insert(0, 'app'); import streamlit" || true

RUN mkdir -p /var/log/supervisor

EXPOSE 7860 8000

CMD ["/usr/bin/supervisord", "-c", "/app/supervisord.conf"]