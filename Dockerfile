FROM python:3.10-alpine
COPY . /
WORKDIR /
RUN pip install --upgrade pip && pip install fastapi uvicorn aiofiles
EXPOSE 8888
CMD uvicorn main:app --reload --host 0.0.0.0 --port 8888