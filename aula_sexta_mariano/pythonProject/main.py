import uvicorn

from app.settings.fastapi_app import create_app

app = create_app()


if__name__ == 'main':
    uvicorn.run("main:app", host= "127.0.0.1", port=8000, reload=True)