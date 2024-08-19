#! /usr/bin/env sh
set -e
  
# Start Uvicorn 
exec uvicorn  --host 0.0.0.0 --port $APP_PORT --log-level info app.main:app
