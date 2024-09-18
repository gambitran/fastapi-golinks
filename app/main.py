from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Links
from .config import AsyncSessionLocal
from pprint import pprint

app = FastAPI()


async def get_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()


@app.get('/readyz')
async def healthz():
    return {'msg': 'ok'}


@app.get('/livez')
async def livez():
    return {'msg': 'ok'}


@app.get("/links")
async def read_links(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Links))
    links = result.scalars().all()
    pprint(links)
    return JSONResponse(jsonable_encoder(links))


# @app.post('/link')
# async def post_link(link: Link):
#     link_dict = link.model_dump()
#     data.append(link_dict)
#     pprint(data)
