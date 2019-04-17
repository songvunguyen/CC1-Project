import numpy as np
import os
import json
import sys
# import json
# from datasets_path import *
# from lda_demo import parameter_estimation as lda_pe
# from dxtp_demo import parameter_estimation as dxtp_pe

from text_utils import *

PATH = os.path.abspath(os.path.dirname(__file__))
NUM_PRINT_TERMS = 6
MODELS_FOLDER = os.path.join(PATH, "python/DXTP02122043/DXTP02122043/")
NEURO_VOCAB_PATH = os.path.join(PATH, "files/neuro_vocab.txt")
NEURO_DATASETS_PATH = os.path.join(PATH, "files/neuro_datasets.txt")
NEURO_TOOLS_PATH = os.path.join(PATH, "files/neuro_tools.txt")


def dxtp_parameter_estimation(kw, kt, ks, ztot, alpha, beta):
    num_topics = kw.shape[0]
    num_vocabs = kw.shape[1]
    num_tools = kt.shape[1]
    num_datasets = ks.shape[1]

    est_kw = np.zeros((num_topics, num_vocabs))
    est_kt = np.zeros((num_topics, num_tools))
    est_ks = np.zeros((num_topics, num_datasets))

    for k in range(num_topics):
        est_kw[k, :] = (1.0 * (kw[k, :] + beta)) / (ztot[k] + num_vocabs * beta)
        est_kt[k, :] = (1.0 * (kt[k, :] + alpha)) / (np.sum(kt[k, :]) + num_tools * alpha)
        est_ks[k, :] = (1.0 * (ks[k, :] + alpha)) / (np.sum(ks[k, :]) + num_datasets * alpha)

    return est_kw, est_kt, est_ks


def load_model():
    with open(NEURO_VOCAB_PATH, 'r') as fp:
        vocabs = fp.readlines()
    vocabs = [x.strip() for x in vocabs]
    fp.close()

    with open(NEURO_TOOLS_PATH, 'r') as fp:
        tools = fp.readlines()
    tools = [x.strip() for x in tools]
    fp.close()

    with open(NEURO_DATASETS_PATH, 'r') as fp:
        datasets = fp.readlines()
    datasets = [x.strip() for x in datasets]
    fp.close()

    # load model file
    folder_name = MODELS_FOLDER + '/'
    kw = np.loadtxt(folder_name + 'kw.dat')
    kt = np.loadtxt(folder_name + 'kt.dat')
    ks = np.loadtxt(folder_name + 'ks.dat')
    ztot = np.loadtxt(folder_name + 'ztot.dat')

    with open(folder_name + 'settings.txt', 'r') as fp:
        settings = fp.readlines()
    settings = [x.strip() for x in settings]

    for s in settings:
        if 'alpha' in s:
            alpha = float(s.split('=')[1])

        if 'beta' in s:
            beta = float(s.split('=')[1])

    est_kw, est_kt, est_ks = dxtp_parameter_estimation(kw, kt, ks, ztot, alpha, beta)

    return est_kw, est_kt, est_ks, vocabs, tools, datasets


def query(s="neuron simulation"):
    output = []
    est_kw, est_kt, est_ks, vocabs, tools, datasets = load_model()
    words = s.split()
    ids = []
    for w in words:
        if w in vocabs:
            ids.append(vocabs.index(w))

    if len(ids) == 0:
        output.append({'id': 0, 'summary': '', 'tools': '', 'datasets': ''})
        print("no match topics")
        return output

    num_topics = est_kw.shape[0]
    probs = []
    for k in range(num_topics):
        p = np.sum(np.log(est_kw[k, ids]))
        probs.append(p)

    topics = np.argsort(probs)[::-1][:2]
    print("Highly matched topics is")
    for i in range(len(topics)):
        topic_summary = ''
        tool_summary = ''
        dataset_summary = ''

        kw_idx = np.argsort(est_kw[topics[i], :])[::-1][:NUM_PRINT_TERMS]
        kt_idx = np.argsort(est_kt[topics[i], :])[::-1]
        kt_idx = kt_idx[kt_idx < len(tools)][:NUM_PRINT_TERMS]

        ks_idx = np.argsort(est_ks[topics[i], :])[::-1]
        ks_idx = ks_idx[ks_idx < len(datasets)][:NUM_PRINT_TERMS]

        for j in range(NUM_PRINT_TERMS):
            topic_summary += vocabs[kw_idx[j]]
            if j != NUM_PRINT_TERMS - 1:
                topic_summary += ' '

        for j in range(3):
            tool_summary += tools[kt_idx[j]]
            if j != NUM_PRINT_TERMS - 1:
                tool_summary += ', '

        for j in range(3):
            dataset_summary += datasets[ks_idx[j]]
            if j != NUM_PRINT_TERMS - 1:
                dataset_summary += ', '
        #load the query result into dictionary struct
        output.append({"id": int(topics[i]), "summary": str(topic_summary), "tools": str(tool_summary), "datasets": str(dataset_summary)})
        print('\t topic %s : %s\n' % (topics[i], topic_summary))
        print('\t\t Suggested tools:  %s \n' % tool_summary)
        print('\t\t Suggested datasets: %s \n' % dataset_summary)
        print()
    
    return output


def main():
    print("What can I help you with?")
    s = input()
    # s = str(sys.argv[1])
    query(s)
    while s != 'quit':
        print('What can I help you with?')
        s = input()
        query(s)


if __name__ == '__main__':
    main()
