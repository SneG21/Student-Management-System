# Use Python base image
FROM python:3.9

# Set the working directory
WORKDIR /sms_app

# Copy dependencies
COPY requirements.txt /sms_app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /sms_app/

# Expose the port
EXPOSE 8000

# Run Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]