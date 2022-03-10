# main.py
# socket connections for API to run on.
import uvicorn

if(__name__ == "__main__"):
    uvicorn.run('endpoints:app', host="0.0.0.0", port=8000, reload=True)
