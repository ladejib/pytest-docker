FROM python:3.14-rc-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY tests/ tests/
COPY pytest.ini .

ENTRYPOINT ["pytest"]

