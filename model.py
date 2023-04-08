import librosa # for audio file analysis
import librosa.display #to explicitly set the location of each object
from glob import glob # to list out all files in directory
import matplotlib.pyplot as plt #for plotting
import numpy as np  # to work with vector arrays
import speaker_verification_toolkit.tools as svt
from sklearn.mixture import GaussianMixture as GMM
import pickle as cPickle 

def func2(choice,names):
    # FEATURE EXTRACTION
    aud_file = glob('upload\\*') # to list out all files in directory
    features = np.asarray(())
    for i in range (0,len(aud_file)):
        data , sr = librosa.load(aud_file[i],sr=44100, mono='true')
        data = svt.extract_mfcc(data)
        if features.size == 0:
            features = data
        else:
            features = np.vstack((features, data))
    '''print(features)
    print(features.shape)'''

    if choice == 1:
        # MFCC FILE CREATION
        mfccfile = names
        np.savetxt(mfccfile, np.array(features[:]), fmt="%.4f", delimiter=',')
        print("Finished Saving Model")

    elif choice == 2:
        # GMM MODEL TRAINING
        title = names
        print("Start GMM training") 
        gmm = GMM(n_components = 64, max_iter = 100, covariance_type='diag',n_init = 3)
        gmm.fit(features)
        print("End GMM training")

        # GMM MODEL SAVING 
        print("Start Saving Model") 
        picklefile = title
        cPickle.dump(gmm,open(picklefile,'wb'))
        print("Model Saved")



if __name__=="__main__":
    choice=int(input("Enter your choice\n"))
    name=input("Enter file name\n")
    func2(choice,name)