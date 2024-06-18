import os
import sys
import implicit
from bson import ObjectId

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from models.recommendation_system.base_algorithm import BaseAlgorithm
from models.recommendation_system.preprocess import Preprocess

class ImplicitModel(BaseAlgorithm):
    def __init__(self, **kwargs):
        self.model = implicit.als.AlternatingLeastSquares(**kwargs)
        self.dataset = None
        
    def fit(self, dataset: Preprocess):
        self.dataset = dataset
        sparse_matrix = self.dataset.build_sparse_matrix()
        self.model.fit(sparse_matrix)
        
    def fit_partial(self, new_data):
        pass
    
    def recommend(self, user_id, n):
        if isinstance(user_id, str):
            player_ixs = self.dataset.get_player_ix(ObjectId(user_id))
        elif isinstance(user_id, list):
            player_ixs = [self.dataset.get_player_ix(
                ObjectId(player_id)) for player_id in user_id]
        else:
            raise ValueError(
                'user_id must be an str or a list of str')
        ids, _ = self.model.recommend(
            player_ixs, self.dataset.get_sparse_matrix()[player_ixs], N=10, filter_already_liked_items=True)
        if ids.ndim == 1:
            return [str(self.dataset.get_question_id(ix)) for ix in ids]
        result_dict = {}
        for i, player_id in enumerate(user_id):
            result_dict[str(player_id)] = [str(self.dataset.get_question_id(ix))
                                        for ix in ids[i]]
            
    def save(self, path):
        pass
    
    def load(self, path):
        pass