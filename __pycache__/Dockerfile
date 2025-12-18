# 1. Use an official Python image as a base
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your local code into the container
COPY main.py .

# 4. Install the necessary libraries
RUN pip install fastapi uvicorn

# 5. The command to run your app inside the box
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]