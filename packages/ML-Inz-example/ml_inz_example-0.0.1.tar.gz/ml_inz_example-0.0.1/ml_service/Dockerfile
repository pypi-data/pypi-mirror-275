FROM python:3.11-slim-bullseye

RUN rm -rf /usr/local/cuda/lib64/stubs

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git

COPY ./app /app/app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu121

RUN useradd -m huggingface

USER huggingface

WORKDIR /app/huggingface

ENV USE_TORCH=1
ENV PYTHONPATH=/app

RUN mkdir -p /app/huggingface/.cache/huggingface \
  && mkdir -p /app/huggingface/input \
  && mkdir -p /app/huggingface/output

CMD ["python", "/app/app/main.py"]
