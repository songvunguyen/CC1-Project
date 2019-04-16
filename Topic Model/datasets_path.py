import os
from os.path import dirname

# Neuroscience dataset path
# papers from Front. Comput. Neurosci
FNCOM_PAPERS_ORI_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/fncom_papers_original.json')
FNCOM_PAPERS_INFO_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/fncom_papers_info.json')

# papers from Journal of Computational Neurosci
JOCN_PAPERS_INFO_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/jocn_papers_info.json')
JOCN_PAPERS_ORI_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/jocn_papers_original.json')

# papers from Journal of Neuroscience
JONEURO_PAPERS_INFO_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/joneuro_papers_info.json')
JONEURO_PAPERS_ORI_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/joneuro_papers_original.json')

# All papers from neuroscience community in bag of words
NEURO_PAPERS_BOW_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/neuro_papers_bow.json')
NEURO_PAPERS_IDX = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/neuro_papers_idx.json')
NEURO_PAPER_TOOL = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/neuro_paper_tool.json')
NEURO_PAPER_DATASET = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/neuro_paper_dataset.json')

#NEURO_VOCAB_PATH = "C:\\Users\\sivar\\Downloads\\files\\neuro_vocab.txt"
#NEURO_VOCAB_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/neuro_vocab.txt')
#NEURO_DATASETS_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/neuro_datasets.txt')
#NEURO_TOOLS_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/neuro_tools.txt')
NEURO_LESS_FREQUENT_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/neuro_less.txt')
NEURO_INVALID_WORDS_PAH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/invalid_words.txt')


# Paper from bmc bioinformatics
BMC_BIOINFORMACTS_INFO_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bmc_papers_info.json')
BIO_PAPER_ORI_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bmc_papers_original.json')

# Paper from bmc genomics
BMC_GENOMICIS_INFO_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bmc_genomics_papers_info.json')
BMC_GENOMICS_ORI_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bmc_genomics_original.json')

# Paper from plos
PLOS_INFO_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/plos_info.json')
PLOS_ORI_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/plos_original.json')

# Bioinformatcis tools and datasets
BIO_TOOLS_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bio_tools.txt')
BIO_DATASETS_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bio_datasets.txt')
BIO_LESS_FREQUENT_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bio_less.txt')
BIO_VOCAB_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bio_vocab.txt')
BIO_PAPERS_BOW_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bio_papers_bow.json')
BIO_PAPERS_IDX = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bio_papers_idx.json')
BIO_PAPER_TOOL = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bio_paper_tool.json')
BIO_PAPER_DATASET = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/bio_paper_dataset.json')

# CNT papers
CNT_PAPERS_Folder = os.path.join(dirname(os.path.realpath(__file__)), 'papers_cnt')
CNT_PAPERS_ORI_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/cnt_papers_original.json')
CNT_PAPERS_CROP_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/cnt_papers_crop.json')
CNT_PAPERS_IDX_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/cnt_papers_idx.json')
CNT_PAPERS_INFO_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/cnt_papers_info.json')
CNT_PAPERS_BOW_PATH = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/cnt_papers_bow.json')
CNT_PAPERS_VOCAB = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/cnt_papers_vocab.txt')
CNT_PAPERS_LESS = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/cnt_papers_less.txt')


# Models folder path
#MODELS_FOLDER = os.path.join(dirname(os.path.realpath(__file__)), 'models/')
STOP_WORDS = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/stop_words.txt')
INVALID_WORDS = os.path.join(dirname(os.path.realpath(__file__)), 'dataset/invalid_words.txt')