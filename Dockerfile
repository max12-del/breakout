# Base Image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy all project files
COPY . .

# Expose port
EXPOSE 5000

# Command to run app
CMD ["python", "app.py"]
