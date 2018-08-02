# rest-api-deploy

### Directory Structure

```
toy_project_v2/
├── build_image.sh
├── conda
│   └── requirements.txt
├── docker
│   ├── api_supervisor.conf
│   └── create_container.sh
├── Dockerfile
├── README.md
└── toy
    ├── bin
    │   ├── flask.sh
    │   ├── gunicorn.sh
    │   ├── kill.sh
    │   ├── restart.sh
    │   └── test.sh
    ├── conf
    │   ├── gunicorn.conf
    │   └── logging.conf
    ├── logs
    │   └── toy.log
    ├── requirements.txt
    ├── test
    │   └── module_a
    └── toy
        ├── __init__.py
        ├── module_a
        │   ├── __init__.py
        │   └── logic.py
        └── utils
            ├── exception.py
            ├── __init__.py
            ├── logger.py
            └── timer.py

```