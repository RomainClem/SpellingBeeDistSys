# Use an official Python runtime as a parent image - for a list of others see https://hub.docker.com/_/python/
FROM python:3-stretch

# Set the working directory to /app - this is a directory that gets created in the image
WORKDIR /app

# Copy the current host directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pika

# Make port 64001 available to the world outside this container
EXPOSE 64001

# Run greeter_server.py when the container launches
CMD ["python", "-u", "server.py"]