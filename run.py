import os
import sys
sys.path.append("..")
from controllers.swagger import app
import uvicorn


def run():
    run_app = uvicorn.run(app)
    return run_app

if __name__ == "__main__":
    run()