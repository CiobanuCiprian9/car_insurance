import uvicorn
from fastapi import FastAPI,Request
from controllers.routers import list_of_cars_router,history_router,insurance_router,claim_router,policie_router
from fastapi.responses import JSONResponse
from app.exceptions import ServiceError

app = FastAPI()

app.include_router(list_of_cars_router.router,prefix="/api/cars")
app.include_router(history_router.router,prefix="/api/cars")
app.include_router(insurance_router.router,prefix="/api/cars")
app.include_router(claim_router.router,prefix="/api/cars")
app.include_router(policie_router.router,prefix="/api/cars")

@app.exception_handler(ServiceError)
async def service_error_handler(_: Request, exc: ServiceError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "status": exc.status_code,
                "type": exc.error,
                "message": str(exc),
            }
        },
    )

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
