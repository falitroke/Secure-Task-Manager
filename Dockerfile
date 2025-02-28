# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

# Copy package.json and install Node.js dependencies
COPY package.json .
RUN npm install

# Copy source code
COPY src/ .

# Expose port
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]