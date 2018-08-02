# Image
FROM python:3.5

RUN apt-get update -y && \
	# apt-get install -y build-essential &&\ 
    apt-get clean &&\ 
    apt-get install -y supervisor &&\ 
    apt-get install -y vim &&\ 
    apt-get install -y git

# Copy | Add	
COPY toy/ toy/
WORKDIR toy/
RUN pip install --no-cache-dir -r requirements.txt

# Supervisor config (auto start)
ADD docker/toy_supervisor.conf  /etc/supervisor/conf.d/

# port
EXPOSE 5000

CMD ["supervisord", "-n"]

