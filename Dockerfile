FROM python:3.9.0

# Create a directory for the application
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a directory for the data
RUN mkdir data

# Copy the compressed_opinions.zip file into the container
COPY compressed_opinions.zip .

# Unzip the file into the data directory
RUN unzip compressed_opinions.zip -d data/

# Set the working directory to /app
WORKDIR /app

# Add your application code or configuration here

# Start your application or provide the necessary entry point command
