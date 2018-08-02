docker rm -f project_toy_api
docker run -itd -p 5000:5000 -v /etc/localtime:/etc/localtime:ro --name project_toy_api toy_api
