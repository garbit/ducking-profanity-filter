FROM python:3.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

ENV PATH /home/${USERNAME}/.local/bin:${PATH}

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "3006"]