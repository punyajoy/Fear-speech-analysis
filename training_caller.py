from models.tokenization import *
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from models.model_architecture import *
from models.train_eval import *
from models.model_utils import *
from models.tokenization import *
from tqdm import tqdm, tqdm_notebook
parent_path='../Data/New_Data_15-06-2020/'


#bert-base-multilingual-cased
#xlm-roberta-base
#lstm_transformer
params={'model_path':'xlm-roberta-base',
        'preprocess_doc':False,
        'max_length':256,
        'batch_size':16,
        'hidden_size':128,
        'weights':[3.0,1.0],
        'load_saved':False,
        'seq_model':'lstm',
        'data_path':parent_path+'Fearspeech_data_final.pkl',
        'max_sentences_per_doc':5,
        'transformer_type':'normal_transformer',
        'take_tokens_from':'both',
        'device':'cuda',
        'learning_rate':2e-5,
        'epsilon':1e-8,
        'random_seed':2020,
        'epochs':20,
        'max_memory':0.6,
        'freeze_bert':False
       }



if __name__=='__main__': 
    train_phase_held_out(params)