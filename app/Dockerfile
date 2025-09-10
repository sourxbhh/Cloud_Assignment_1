# Start from a lightweight Python image [cite: 103]
FROM python:3.11-slim

# Install the PostgreSQL driver for Python 
RUN pip install --no-cache-dir "psycopg[binary]==3.1.18"

# Set the working directory inside the container 
WORKDIR /app

# Copy your application script into the container [cite: 105]
COPY main.py .

# Define the default command to run when the container starts [cite: 106]
CMD ["python", "main.py"]