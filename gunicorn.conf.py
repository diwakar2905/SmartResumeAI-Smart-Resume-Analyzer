# Gunicorn configuration for Smart Resume Analyzer
bind = "0.0.0.0:5001"
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
preload_app = True
reload = False
accesslog = "-"
errorlog = "-"
loglevel = "info"
capture_output = True
