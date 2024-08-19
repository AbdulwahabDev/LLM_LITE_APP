import sys , os 
sys.path.append(os.path.abspath('../'))   

# to run using vscode ... 
sys.path.append(os.path.abspath('backend/python/'))                  # to see from commons .....
sys.path.append(os.path.abspath('backend/python/rag_app'))           # to see from app. .....


from fastapi import FastAPI
from app.api.NeuralSearcher_test.routes import NeuralSearcher_test_router_

app = FastAPI( title=f"RAG APP APIs",  )

# Include router modules passed to the function
routers_modules=[ NeuralSearcher_test_router_, ]
for router_module in routers_modules:
    app.include_router(router_module)

