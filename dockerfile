# Use official Python image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY=django-insecure-mysecurekey123

# Set working directory to the project root
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the image
COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Run migrations automatically (optional, can skip if handled externally)
# RUN python manage.py migrate

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]