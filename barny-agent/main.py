from fastapi import FastAPI
from classes.system.Cpu import Cpu
from classes.system.Ram import Ram
from classes.system.Swap import Swap
from classes.system.Disk import Disk
from classes.Metrics import Metrics

app = FastAPI()

@app.get("/metrics")
def read_metrics():
    return Metrics(
        [
            Cpu(),
            Ram(),
            Swap(),
            Disk(),
        ],
    ).metrics()
