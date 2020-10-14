#!/bin/bash

pip install -r requirements.txt
gunicorn --bind=0.0.0.0 srv.main:app -w 4 -k uvicorn.workers.UvicornWorker