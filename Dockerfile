FROM python:3.10

# setup python environment
ADD Pipfile Pipfile.lock ./
RUN pip install pipenv debugpy
RUN pipenv --python python3.10

# pull exact version from Pipfile.lock
RUN pipenv install --ignore-pipfile --system

COPY . .

# CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]

# uvicorn main:app --reload