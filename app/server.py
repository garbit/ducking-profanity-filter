from fastapi import FastAPI
from pydantic import BaseModel
from detoxify import Detoxify

app = FastAPI()

model = Detoxify('multilingual', device='cpu')

class ToxicityReponse(BaseModel):
    toxicity: float
    severe_toxicity: float
    obscene: float
    identity_attack: float
    insult: float
    threat: float
    sexual_explicit: float

@app.get("/toxicity")
def predict(q: str) -> ToxicityReponse:
    result = model.predict([q])
    
    print(result)

    return ToxicityReponse(
        toxicity=result["toxicity"][0],
        severe_toxicity=result["severe_toxicity"][0],
        obscene=result["obscene"][0],
        identity_attack=result["identity_attack"][0],
        insult=result["insult"][0],
        threat=result["threat"][0],
        sexual_explicit=result["sexual_explicit"][0],
    )