# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /sms_app

# Install dependencies
COPY requirements.txt /sms_app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /sms_app/

# Collect static files (if needed)
# RUN python manage.py collectstatic --noinput

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]