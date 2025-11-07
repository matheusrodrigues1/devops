# Build stage
FROM python:3.11-alpine as builder

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev \
    libffi-dev

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-alpine

WORKDIR /app

# Install runtime dependencies
RUN apk add --no-cache postgresql-libs libffi

# Copy installed packages from builder stage
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Create non-root user
RUN adduser -D appuser && chown -R appuser:appuser /app
USER appuser

# Copy application code
COPY --chown=appuser:appuser app/ .

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Start application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]