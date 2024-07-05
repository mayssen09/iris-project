import pandas as pd
from fastapi import HTTPException
from helpers.load_model import scaler, model




def predict_species(data):
    try:
        input_data = pd.DataFrame({
            'Id': [0],
            'SepalLengthCm': [data.SepalLengthCm],
            'SepalWidthCm': [data.SepalWidthCm],
            'PetalLengthCm': [data.PetalLengthCm],
            'PetalWidthCm': [data.PetalWidthCm],
        })

        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)

        return {"prediction": prediction[0]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
