FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create supervisor log directory
RUN mkdir -p /var/log/supervisor

# Expose both ports
EXPOSE 7860 8000

# Start both services using supervisord
CMD ["/usr/bin/supervisord", "-c", "/app/supervisord.conf"]