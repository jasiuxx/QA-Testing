FROM python:3.10

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


RUN playwright install --with-deps chromium chrome

COPY . /app/
CMD ["pytest"]
