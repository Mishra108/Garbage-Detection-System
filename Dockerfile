FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# ── DEBUG: exact structure aur import errors dikhao ──
RUN echo "=== FOLDER STRUCTURE ===" && find /app -type f -name "*.py" | head -20
RUN echo "=== TESTING FASTAPI IMPORT ===" && cd /app/api && python -c "from api import app; print('FastAPI OK')"
RUN echo "=== TESTING STREAMLIT FILE ===" && cd /app/app && python -c "import ast; ast.parse(open('app.py').read()); print('Streamlit OK')"

RUN mkdir -p /var/log/supervisor

EXPOSE 7860 8000

CMD ["/usr/bin/supervisord", "-c", "/app/supervisord.conf"]