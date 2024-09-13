from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/readyz")
async def healthz():
    return {"msg": "ok"}


@app.get("/livez")
async def livez():
    return {"msg": "ok"}

# Mock initial data
data = [{'name': 'fb', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 'url': 'https://facebook.com'},
        {'name': 'yt', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 'url': 'https://youtube.com'},
        {'name': 'argocd', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 'url': 'https://argoproj.github.io/cd/'},
        {'name': 'twitch', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 'url': 'https://twitch.tv'}]


@app.get("/links")
async def links():
    return JSONResponse(jsonable_encoder(data))
