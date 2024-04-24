FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Update pip
RUN pip install --upgrade pip

# Install HDF5 using apt
RUN apt-get update && apt-get install -y libhdf5-dev

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app