from fastapi import APIRouter
 

check_router_ = APIRouter(prefix="", tags=["check"])
 
@check_router_.get("/")
def _():
    return "FastAPI Working ...  "
