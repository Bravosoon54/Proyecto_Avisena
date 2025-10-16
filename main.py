from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import lands, users, auth, sensors, sensor_types

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/access", tags=["login"])
app.include_router(lands.router, prefix="/lands", tags=["lands"])
app.include_router(sensor_types.router, prefix="/sensor-types", tags=["sensor-types"])
app.include_router(sensors.router, prefix="/sensors", tags=["sensors"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"], 
    allow_headers=["*"], 
)

@app.get("/")
def read_root():
    return {
                "message": "ok",
                "autor": "ADSO 2925889"
            }