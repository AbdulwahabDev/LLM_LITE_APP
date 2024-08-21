import sys , os 
sys.path.append(os.path.abspath('../'))   

# to run using vscode ... 
sys.path.append(os.path.abspath('backend/python/'))                  # to see from commons .....
sys.path.append(os.path.abspath('backend/python/rag_app'))           # to see from app. .....


from fastapi import FastAPI
from app.api.check.routes import check_router_
from app.api.NeuralSearcher.routes import NeuralSearcher_router_

app = FastAPI( title=f"RAG APP APIs",  )

# Include router modules passed to the function
routers_modules=[ check_router_,
                 NeuralSearcher_router_, 
                 ]

for router_module in routers_modules:
    app.include_router(router_module)

