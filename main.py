from fastapi import FastAPI
from helpers.models import InputData
from helpers.predict import predict_species



app = FastAPI()


@app.post("/predict/")
async def predict_endpoint(data: InputData):
    return predict_species(data)
    
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1", port=8000)
