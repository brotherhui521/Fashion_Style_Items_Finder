from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import app
import gradio as gr


# Initialize the app with the dataset
myapp = app.StyleFinderApp("swift-style-embeddings.pkl")

# Create the Gradio interface
demo = app.create_gradio_interface(myapp)

# create fastapi app
fastapp = FastAPI()

fastapp=gr.mount_gradio_app(fastapp, demo, path="/gradio")



class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@fastapp.get("/")
def read_root():
    return {"status":"ok"}

@fastapp.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@fastapp.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
     return {"item_name": item.name, "item_id": item_id}


