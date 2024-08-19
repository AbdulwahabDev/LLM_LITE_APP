from fastapi import APIRouter

from app.api.NeuralSearcher.helper.neural_searcher import NeuralSearcher

# Create a neural searcher instance
NeuralSearcher_router_ = APIRouter(prefix="/api/v1/RAG/NeuralSearcher", tags=["NeuralSearcher"])

NeuralSearcher_obj = NeuralSearcher(collection_name='startups',
                                    model_name_or_path='all-MiniLM-L6-v2',
                                    QdrantClient_URL="http://localhost:6333")
 

@NeuralSearcher_router_.get("/search")
def search_startup(q: str ,
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