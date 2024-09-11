FROM python:3.9-slim-buster
COPY requirements.txt requirements.txt
RUN python3 -m venv /my_env
ENV PATH="/my_env/bin:$PATH"
RUN pip install -r requirements.txt
WORKDIR /ingegneria_software_avanzata
COPY . .
CMD ["python", "main.py"]