FROM python:3.8-slim
LABEL maintainer="student_v22_bsuir@bsuir.by"
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app.py /app/app.py
RUN pip install --no-cache-dir flask==2.3.3
EXPOSE 80
CMD ["python", "app.py"]
