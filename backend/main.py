
from fastapi import FastAPI
from apis.nrb_api import app as nrb_app
from apis.crs_api import app as crs_app
from apis.immigration_api import app as immigration_app
from apis.iprs_api import app as iprs_app
from apis.refugees_api import app as refugees_app

app = FastAPI(title="MDA Data Integration POC")

app.mount("/nrb", nrb_app)
app.mount("/crs", crs_app)
app.mount("/immigration", immigration_app)
app.mount("/iprs", iprs_app)
app.mount("/refugees", refugees_app)
