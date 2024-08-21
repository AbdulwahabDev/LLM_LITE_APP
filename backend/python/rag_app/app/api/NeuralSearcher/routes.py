from commons.common_imports_and_config import *

from fastapi import APIRouter , Query
from app.api.NeuralSearcher.helper.neural_searcher import NeuralSearcher , VectorParams, Distance

# Create a neural searcher instance
NeuralSearcher_router_ = APIRouter(prefix="/api/v1/RAG/NeuralSearcher")

NeuralSearcher_obj = NeuralSearcher(collection_name=collection_name,
                                    NeuralSearcher_model_path=base_path+NeuralSearcher_model_path,
                                    QdrantClient_URL=QdrantClient_URL)

if True: #NeuralSearcher Search
    @NeuralSearcher_router_.get("/search",tags=['NeuralSearcher'])
    def search(q: str ,
                   limit:int=3,
                   return_payloads_only:bool=True):
    
        # You must change it later to retrieve it using body params...    
        query_filter_list_simple = [
            {
                    "SearchType":"must",    
                    "keyName":"city",           
                    "match_value":"Sydney"         
            }
        ]
        
        return {"result": NeuralSearcher_obj.search(text=q ,
                                                query_filter_list=query_filter_list_simple,
                                                limit=limit,
                                                return_payloads_only=return_payloads_only)}
        
if True: #NeuralSearcher Model 
    
    @NeuralSearcher_router_.get("/getModelValues",tags=['Model'])
    def GetModelValues():
        return NeuralSearcher_obj.GetModelValues()
    
    @NeuralSearcher_router_.get("/updateModel",tags=['Model'])
    def UpdateModel(
                    NeuralSearcher_model_path: str | None = None,
                    device: DeviceEnum = Query('cpu', description="Select the device")
                    # device: str = 'cpu'
                    ):
        return NeuralSearcher_obj.UpdateModel(NeuralSearcher_model_path=NeuralSearcher_model_path,
                                              device=device)
    
    @NeuralSearcher_router_.get("/encode",tags=['Model'])
    def create_if_not_exists():
        return NeuralSearcher_obj.encode_data()
                    
if True: #NeuralSearcher Collection 
    @NeuralSearcher_router_.get("/getClientValues",tags=['Collection'])
    def GetClientValues():
        return NeuralSearcher_obj.GetClientValues()
    
    @NeuralSearcher_router_.get("/cheack_if_exists",tags=['Collection'])
    def create_if_not_exists():
        return NeuralSearcher_obj.cheack_if_exists()

    @NeuralSearcher_router_.patch("/create_if_not_exists",tags=['Collection'])
    def create_if_not_exists():
        return NeuralSearcher_obj.create_if_not_exists()

    @NeuralSearcher_router_.patch("/upload_test_collection",tags=['Collection'])
    def upload_test_collection():
        return NeuralSearcher_obj.upload_test_collection()
