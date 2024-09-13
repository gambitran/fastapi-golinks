from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from pprint import pprint

app = FastAPI()


class Link(BaseModel):
    name: str
    url: str
    description: str
    views: int | None = 0


@app.get('/readyz')
async def healthz():
    return {'msg': 'ok'}


@app.get('/livez')
async def livez():
    return {'msg': 'ok'}

# Mock initial data
data = [{'name': 'fb', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 'url': 'https://facebook.com', 'views': 5000},
        {'name': 'yt', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 'url': 'https://youtube.com', 'views': 100},
        {'name': 'argocd', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 'url': 'https://argoproj.github.io/cd/', 'views': 250},
        {'name': 'twitch', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam suscipit varius lacus, ut pulvinar leo vehicula vel. Curabitur iaculis malesuada est, et tempus justo sollicitudin id. Suspendisse dapibus justo ut sem malesuada, et tempus ipsum condimentum. Integer dictum risus arcu, efficitur elementum ipsum posuere ac.', 'url': 'https://twitch.tv', 'views': 300}]


@app.get('/links')
async def links():
    return JSONResponse(jsonable_encoder(data))


@app.post('/link')
async def post_link(link: Link):
    link_dict = link.model_dump()
    data.append(link_dict)
    pprint(data)
