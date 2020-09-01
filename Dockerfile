# Use an official Python runtime as a parent image
FROM python:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
  wait-for-it

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run scrapyrt when the container launches
ENTRYPOINT ["scrapyrt", "-i", "0.0.0.0"]

# Expose scrapyrt default port
EXPOSE 9080