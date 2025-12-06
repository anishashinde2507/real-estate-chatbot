FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn whitenoise

# Copy backend code
COPY backend/ .

# Collect static files
RUN python manage.py collectstatic --noinput --clear 2>/dev/null || true

# Create non-root user
RUN useradd -m -u 1000 django && chown -R django:django /app
USER django

# Expose port
EXPOSE 8000

# Run start script
CMD ["gunicorn", "realestate_api.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "60"]
