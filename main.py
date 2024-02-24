from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import FastAPI, File, UploadFile, HTTPException

import cv2
import numpy as np
from ultralytics import YOLO
from typing import List, Dict
import os
from fastapi.staticfiles import StaticFiles

save_directory = "detected_images"
os.makedirs(save_directory, exist_ok=True)

app = FastAPI()
app.mount("/static", StaticFiles(directory=save_directory), name="static")

# Load the YOLO model
model = YOLO("best.pt")

@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <html>
        <head>
            <title>Upload an Image for Detection</title>
        </head>
        <body>
            <h1>Upload an Image for Detection</h1>
            <form action="/detect/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit">
            </form>
        </body>
    </html>
    """
    return content

@app.post("/detect/", response_class=HTMLResponse)
async def detect_objects(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = np.frombuffer(image_bytes, dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        

        results=model.predict(image, save=False, imgsz=320, conf=0.001)
        for result in results:

            
            res_plotted = result[0].plot()
            save_path = os.path.join(save_directory, f"detected_image_1.jpg")
            if os.path.exists(save_path):
                os.remove(save_path)
            print(res_plotted)
            cv2.imwrite(save_path, res_plotted)
            
        image_url = "/static/detected_image_1.jpg"
        return HTMLResponse(content=f'<img src="{image_url}" />')
    
    except Exception as e:
        # Log the error for debugging
        print(f"Error processing the image: {str(e)}")
        # Return a generic server error response
        return JSONResponse(status_code=500, content={"message": "Internal server error while processing the image."})
