# Use an official Python base image with GUI support
FROM python:3.10-slim

# Install system dependencies for GUI (Tkinter, X11)
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    libx11-6 \
    libxrender1 \
    libxext6 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxkbcommon-x11-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your Python script and requirements
COPY . /app

# Install Python dependencies
#RUN pip install --no-cache-dir Pillow

# Set display variable for X11 (will use host display)
ENV DISPLAY=host.docker.internal:0

# Run the script
CMD ["python3", "gui.py"]
