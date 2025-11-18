# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory to the project root
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
# RUN pip install --upgrade pip && pip install -r requirements.txt 
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the image
COPY . . 

# Expose port 8000 for Django
EXPOSE 8000

# Run migrations automatically and start server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]