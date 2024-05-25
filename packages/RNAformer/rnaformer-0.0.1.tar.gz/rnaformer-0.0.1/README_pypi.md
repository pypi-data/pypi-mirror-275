# RNAformer

RNAformer is a simple yet effective deep learning model for RNA secondary structure prediction. We describe RNAformer in the preprint [*RNAformer: A Simple Yet Effective Deep Learning Model for RNA Secondary Structure Prediction*](https://www.biorxiv.org/content/10.1101/2024.02.12.579881v1)  and the preceding workshop paper 
[*Scalable Deep Learning for RNA Secondary Structure Prediction*](https://arxiv.org/abs/2307.10073) 
presented at the 2023 ICML Workshop on Computational Biology.

### Abstract

Ribonucleic acid (RNA) is a major biopolymer with key roles as a regulatory molecule in cellular differentiation, gene expression, and various diseases. The prediction of the secondary structure of RNA is a challenging research problem crucial for understanding its functionality and developing RNA-based treatments. Despite the recent success of deep learning in structural biology, applying deep learning to RNA secondary structure prediction remains contentious. A primary concern is the control of homology between training and test data. Moreover, deep learning approaches often incorporate complex multi-model systems, ensemble strategies, or require external data. Here, we present the RNAformer, an attention-based deep learning model designed to predict the secondary structure from a single RNA sequence. Our deep learning model, in combination with a novel data curation pipeline, addresses previously reported caveats and can effectively learn a biophysical model across RNA families. The RNAformer achieves state-of-the-art performance on experimentally derived secondary structures while considering data homologies by training on a family-based split. 


## Reproduce results

You may install the RNAformer using `pip`

```
pip install RNAformer
```

or directly from the source below.

### Clone the repository

```
git clone https://github.com/automl/RNAformer.git
cd RNAformer
```

### Install virtual environment

The Flash Attention package currently requires a Ampere, Ada, or Hopper GPU (e.g., A100, RTX 3090, RTX 4090, H100). Support for Turing GPUs (T4, RTX 2080) is coming soon. 

```
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
pip install flash-attn==2.3.4
pip install -e .
```
Alternatively, you may install RNAformer for inference without Flash Attention or a GPU:
```
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
pip install -e .
```

### Download datasets

```
bash download_all_datasets.sh
``` 


### Download pretrained models

``` 
bash download_all_models.sh
```
    

### Reproduce results from the paper

``` 
bash run_evaluation.sh
```


## Infer RNAformer for RNA sequence:

An example of a inference, the script outputs position indexes in the adjacency matrix that are predicted to be paired. 

``` 
python infer_RNAformer.py -c 6 -s GCCCGCAUGGUGAAAUCGGUAAACACAUCGCACUAAUGCGCCGCCUCUGGCUUGCCGGUUCAAGUCCGGCUGCGGGCACCA --state_dict models/RNAformer_32M_state_dict_intra_family_finetuned.pth --config models/RNAformer_32M_config_intra_family_finetuned.yml
``` 

## Model Checkpoints

Please find here the state dictionaries and configs for the models used in the paper: 

RNAformer 32M from the biophysical model experiment:
```
https://ml.informatik.uni-freiburg.de/research-artifacts/RNAformer/models/RNAformer_32M_state_dict_biophysical.pth
https://ml.informatik.uni-freiburg.de/research-artifacts/RNAformer/models/RNAformer_32M_config_biophysical.yml
```

RNAformer 32M from the bprna model experiment:
```
https://ml.informatik.uni-freiburg.de/research-artifacts/RNAformer/models/RNAformer_32M_state_dict_bprna.pth
https://ml.informatik.uni-freiburg.de/research-artifacts/RNAformer/models/RNAformer_32M_config_bprna.yml
```

RNAformer 32M from the intra family finetuning experiment:
```
https://ml.informatik.uni-freiburg.de/research-artifacts/RNAformer/models/RNAformer_32M_state_dict_intra_family_finetuned.pth
https://ml.informatik.uni-freiburg.de/research-artifacts/RNAformer/models/RNAformer_32M_config_intra_family_finetuned.yml
```

RNAformer 32M from the inter family finetuning experiment:
```
https://ml.informatik.uni-freiburg.de/research-artifacts/RNAformer/models/RNAformer_32M_state_dict_inter_family_finetuned.pth
https://ml.informatik.uni-freiburg.de/research-artifacts/RNAformer/models/RNAformer_32M_config_inter_family_finetuned.yml
```
