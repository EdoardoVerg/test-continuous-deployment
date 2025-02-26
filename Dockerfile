# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Start the Flask application on 0.0.0.0:8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
