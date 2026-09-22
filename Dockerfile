FROM python:3.11
COPY . /app
RUN pip install -r dependencies/requirements.txt
CMD ["python", "-m", "services.archive.archive"]
