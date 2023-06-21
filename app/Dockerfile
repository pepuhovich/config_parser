FROM python:alpine
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "-u", "main.py"]