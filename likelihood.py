import os
import librosa # for audio file analysis
import librosa.display #to explicitly set the location of each object
from glob import glob # to list out all files in directory
import matplotlib.pyplot as plt #for plotting
import numpy as np  # to work with vector arrays
import speaker_verification_toolkit.tools as svt
from sklearn.mixture import GaussianMixture as GMM
import pickle as cPickle

def func():
    aud_file = glob('upload\\*') # to list out all files in directory
    features = np.asarray(())
    for i in range (0,1):#len(aud_file)):
        data , sr = librosa.load(aud_file[0],sr=44100, mono='true')
        data = svt.extract_mfcc(data)
        if features.size == 0:
            features = data
        else:
            features = np.vstack((features, data))
    modelpath = "GMM"
    gmm_files = [os.path.join(modelpath,fname) for fname in
                os.listdir(modelpath) if fname.endswith('.gmm')]
    #print(gmm_files)
    dict = {}
    c=0
    for i in gmm_files:
        dict.update({c:i})
        c+=1
                
    models    = [cPickle.load(open(fname,'rb')) for fname in gmm_files]

    scores     = None
    log_likelihood = np.zeros(len(models))
    for i in range(len(models)):
        gmm   = models[i]         #checking with each model one by one
        scores = np.array(gmm.score(features))
        log_likelihood[i] = scores.sum()
    winner = np.argmax(log_likelihood)
    return dict[winner]


if __name__=="__main__":
    x=func()
    print(x)



