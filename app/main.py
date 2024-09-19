from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update, asc, delete
from .models import Links, PostLink, UpdateLink, DeleteLink
from .config import AsyncSessionLocal
# from time import sleep


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


@app.get('/links')
async def read_links(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Links).order_by(asc(Links.name)))
    links = result.scalars().all()
    # Test sleep to show loading
    # sleep(0.5)
    return JSONResponse(jsonable_encoder(links))


@app.post('/link')
async def post_link(link: PostLink, db: AsyncSession = Depends(get_db)):

    query = select(Links).filter(Links.name == link.name)
    result = await db.execute(query)
    existing_link = result.scalars().first()

    if existing_link:
        raise HTTPException(status_code=400, detail='Name exists')

    new_link = Links(
        name=link.name,
        url=link.url,
        description=link.description
    )

    db.add(new_link)

    try:
        await db.commit()
        await db.refresh(new_link)
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=f'Error: {e}')

    return new_link


@app.put('/link')
async def put_link(link: UpdateLink, db: AsyncSession = Depends(get_db)):

    query = select(Links).filter(Links.name == link.name)
    result = await db.execute(query)
    existing_link = result.scalars().first()

    if existing_link and (existing_link.id != link.id):
        raise HTTPException(status_code=400, detail='Name exists')

    stmt = (
        update(Links)
        .where(Links.id == link.id)
        .values(
            name=link.name,
            url=link.url,
            description=link.description,
            views=link.views
        )
        .execution_options(synchronize_session='fetch')
    )

    try:
        result = await db.execute(stmt)

        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail='Link not found')
        
        await db.commit()
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=f'Error: {e}')
    
    return {'message': f'{link.name} updated'}


@app.delete('/link')
async def delete_link(link: DeleteLink, db: AsyncSession = Depends(get_db)):
    try:
        stmt = delete(Links).where(Links.id == link.id)

        result = await db.execute(stmt)

        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail='Link not found')
        
        await db.commit()
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=400, details=f'Error: {e}')
