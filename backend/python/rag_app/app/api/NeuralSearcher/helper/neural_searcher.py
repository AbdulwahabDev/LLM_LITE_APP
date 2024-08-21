from commons.common_imports_and_config import *

from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient 
from qdrant_client.models import Filter    
from qdrant_client.models import VectorParams, Distance


current_file_path = Path(__file__)
helper_path = str(current_file_path.parent)



class NeuralSearcher:
    def __init__(self,
                 collection_name ,
                 NeuralSearcher_model_path:str ,
                 QdrantClient_URL:str,
                 device:str='cpu'):
        self.collection_name = collection_name
        self.NeuralSearcher_model_path = NeuralSearcher_model_path
        self.QdrantClient_URL = QdrantClient_URL
        self.device = device
        # Initialize encoder model
        self.model = SentenceTransformer(model_name_or_path=NeuralSearcher_model_path , device=device)
        # initialize Qdrant client
        self.qdrant_client = QdrantClient(QdrantClient_URL)

    if True:# model services
        
        def GetModelValues(self):
            return {
                "model_name":self.NeuralSearcher_model_path.split('/')[-1],
                "device":self.model.device.type,
                "model_path":self.NeuralSearcher_model_path,
            }  
            
        def UpdateModel(self ,NeuralSearcher_model_path:str|None=None,device:str='cpu' ):
            if(NeuralSearcher_model_path):
                self.NeuralSearcher_model_path = NeuralSearcher_model_path
                self.model = SentenceTransformer(model_name_or_path=NeuralSearcher_model_path , device=device)
            if(device):
                self.model.to(device)
        
        def encode_data(self):
            # read data
            df = pd.read_json(helper_path+"/startups_demo.json", lines=True)
            # select what we need to encode
            alt_with_description = [row.alt + ". " + row.description for row in df.itertuples()]
            # vectore selected data
                 
            vectors = [self.model.encode(item) for item in tqdm(alt_with_description, file=sys.stdout, ascii=True)]

            vectors = self.model.encode( alt_with_description,
                                        show_progress_bar=True)
            
            # save encoded vectors
            np.save(helper_path+"/startup_vectors.npy", vectors, allow_pickle=False)
            
            return {"status":"vectors encoded successfully","vectors_shape":vectors.shape}
            
    if True:# Collection services
        
        def GetClientValues(self):
            return {
                "collection_name":self.collection_name,
                "QdrantClient_URL":self.QdrantClient_URL
            }  
                  
        def cheack_if_exists(self):
            return self.qdrant_client.collection_exists(self.collection_name)
            
        def create_if_not_exists(self):
            if not self.qdrant_client.collection_exists(self.collection_name):
                self.qdrant_client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(
                                                size=self.model.get_sentence_embedding_dimension(),
                                                distance=Distance.COSINE
                                            ),
            )
                return(f"collection {self.collection_name} Created !!")
            else:
                return(f"collection {self.collection_name} exists !!") 
            
        def upload_test_collection(self) -> bool: 
            fd = open(helper_path + '/startups_demo.json')
            payload = list(map(json.loads, fd))
            vectors = np.load(helper_path+ "/startup_vectors.npy")
            
        
            print("upload_collection Start ...")
        
            self.qdrant_client.upload_collection(
                collection_name=self.collection_name,
                vectors=vectors,
                payload=payload,
                ids=tqdm(range(len(payload)),file=sys.stdout, ascii=True),
                batch_size=256,  # How many vectors will be uploaded in a single request?
            )
            
            return "upload_collection Done ..."
           
    if True:# search services
        
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
        
        