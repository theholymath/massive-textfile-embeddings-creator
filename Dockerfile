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

# Copy the Python file into the container
COPY create_embeddings_service.py .

# Execute the Python file
CMD ["python", "create_embeddings_service.py"]
