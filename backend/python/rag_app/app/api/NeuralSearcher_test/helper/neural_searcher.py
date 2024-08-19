from sentence_transformers import SentenceTransformer
from tqdm import tqdm , trange

from qdrant_client import QdrantClient 
from qdrant_client.models import Filter    

class NeuralSearcher:
    def __init__(self,
                 collection_name ,
                 model_name_or_path:str ,
                 QdrantClient_URL:str,
                device:str='cpu'):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer(model_name_or_path=model_name_or_path)
        # initialize Qdrant client
        self.qdrant_client = QdrantClient(QdrantClient_URL)

    
    def search(self,
               text: str,
               query_filter_list:list[dict]|None = None,
               limit:int=5,
               return_payloads_only:bool=True):
        """
        Example of query_filter:
        
        test_filter = {
            "SearchType":"must",    :str should | min_should | must | must_not
            "SearchType_details",   :list[dict]
            "keyName":"",           :str Faild Name
            "match_value":""        :str match value
        }
        """

        
        if query_filter_list:
            query_filter_dict = {query_filter_temp['SearchType']: [{
                                            "key": query_filter_temp['keyName'], 
                                            "match": {"value": query_filter_temp['match_value']}
                                        }] for query_filter_temp in query_filter_list }
            query_filter_list = Filter(**query_filter_dict) 
        
        # Convert text query into vector
        vector = self.model.encode(text).tolist()
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            query_filter=query_filter_list,
            limit=limit, 
        )
        
        if return_payloads_only:
            # In this function you are interested in payload only
            payloads = [hit.payload for hit in search_result]
            return payloads
        else:
            return search_result
    
        