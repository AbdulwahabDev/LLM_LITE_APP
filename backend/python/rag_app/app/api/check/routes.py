from fastapi import APIRouter
 

check_router_ = APIRouter(prefix="", tags=["check"])
 
@check_router_.get("/",include_in_schema=False)
def _():
    return "FastAPI Working ...  "
