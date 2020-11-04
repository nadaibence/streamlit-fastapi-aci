from fastapi import FastAPI
from azure.storage.blob import BlockBlobService
import random
from io import BytesIO
import os
import joblib


app = FastAPI()
block_blob_service = BlockBlobService(account_name=os.environ.get('BLOB_ACC_NAME'),
                                      account_key=os.environ.get('BLOB_ACC_KEY'))

container = os.environ.get('CONTAINER_NAME')
model_name = os.environ.get('MODEL_NAME')
model = block_blob_service.get_blob_to_bytes(container, model_name)
model = joblib.load(BytesIO(model.content))


@app.get("/")
def read_root():
    l = [1,2,3,4,5,6,7,8,9,10]
    return {'Pred': random.choice(l)}


@app.get("/pred")
def prediction(rooms: float, area: float, balcony: float):
    pred = model.predict([[rooms, area, balcony]])
    return {'Pred': float(pred)}