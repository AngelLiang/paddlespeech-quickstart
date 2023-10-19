from fastapi import FastAPI
import uvicorn

from web.schemas import TTSIn,TTSOut
from web.services import TTSService

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/paddlespeech/tts")
async def tts(param_in: TTSIn):
    params = param_in.dict()
    result = TTSService().tts(**params)
    return {
        'success': True,
        'code': 0,
        # 'message': {},
        'result': {
            'lang': 'zh',
            'audio': result
        }
    }


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")
