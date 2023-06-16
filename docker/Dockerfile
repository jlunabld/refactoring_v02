# Base image for the container (Bullseye is the codename for Debian 11)
FROM python:3.9-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy the entire app directory and requirements.txt to the working directory
COPY app/ .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary port
EXPOSE 8000

# Start the Gunicorn server with the Dash app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:server"]