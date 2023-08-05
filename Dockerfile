FROM python:3.11-slim
RUN apt-get update && apt-get install -y curl
RUN pip --no-cache-dir install ctransformers

WORKDIR /action
ADD action.py /action
RUN curl -O -L https://huggingface.co/TheBloke/orca_mini_3B-GGML/resolve/main/orca-mini-3b.ggmlv3.q4_0.bin -o /action/orca-mini-3b.ggmlv3.q4_0.bin

ENV TRANSFORMERS_OFFLINE=1

ENTRYPOINT ["python", "-u", "/action/action.py"]
