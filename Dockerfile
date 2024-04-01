FROM python:3.9-slim

COPY ESRGAN/models/RRDB_ESRGAN_x4.pth /home/models/RRDB_ESRGAN_x4.pth

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx && rm -rf /var/lib/apt/lists/* 

COPY . .

EXPOSE 5100

CMD ["python", "app.py"]