#Starter code prepared by Borna Ghotbi, Polina Zablotskaia, and Ariel Shann for Computer Vision
#based on a MATLAB code by James Hays and Sam Birch 

import numpy as np
from util import load, build_vocabulary, get_bags_of_sifts
from classifiers import nearest_neighbor_classify, svm_classify

#For this assignment, you will need to report performance for sift features on two different classifiers:
# 1) Bag of sift features and nearest neighbor classifier
# 2) Bag of sift features and linear SVM classifier

#For simplicity you can define a "num_train_per_cat" vairable, limiting the number of
#examples per category. num_train_per_cat = 100 for intance.

#Sample images from the training/testing dataset. 
#You can limit number of samples by using the n_sample parameter.

recompute = True

print('Getting paths and labels for all train and test data\n')
train_image_paths, train_labels = load("sift/train")
test_image_paths, test_labels = load("sift/test")

if recompute == True:        

    ''' Step 1: Represent each image with the appropriate feature
    Each function to construct features should return an N x d matrix, where
    N is the number of paths passed to the function and d is the 
    dimensionality of each image representation. See the starter code for
    each function for more details. '''
            
    print('Extracting SIFT features\n')
    #TODO: You code build_vocabulary function in util.py
    kmeans = build_vocabulary(train_image_paths, vocab_size=200)

    #TODO: You code get_bags_of_sifts function in util.py 
    train_image_feats = get_bags_of_sifts(train_image_paths, kmeans)
    test_image_feats = get_bags_of_sifts(test_image_paths, kmeans)
 
    np.save('train_image_feats.npy', train_image_feats)
    np.save('test_image_feats.npy', test_image_feats)
 
# train_image_feats = np.load('train_image_feats.npy')
# test_image_feats = np.load('test_image_feats.npy')

#If you want to avoid recomputing the features while debugging the
#classifiers, you can either 'save' and 'load' the extracted features
#to/from a file.

''' Step 2: Classify each test image by training and using the appropriate classifier
 Each function to classify test features will return an N x l cell array,
 where N is the number of test cases and each entry is a string indicating
 the predicted one-hot vector for each test image. See the starter code for each function
 for more details. '''

print('Using nearest neighbor classifier to predict test set categories\n')
#TODO: YOU CODE nearest_neighbor_classify function from classifers.py
pred_labels_knn = nearest_neighbor_classify(train_image_feats, train_labels, test_image_feats)

print('Using support vector machine to predict test set categories\n')
#TODO: YOU CODE svm_classify function from classifers.py
pred_labels_svm = svm_classify(train_image_feats, train_labels, test_image_feats)

print(pred_labels_knn)
print(f'Total number of test images: {len(test_labels)}')
print(f'Total number of correct labels: {sum(pred_labels_knn == test_labels)}') 
print(f'Total classes in test labels: {len(set(test_labels))}')

pred_labels_knn = pred_labels_svm
print(pred_labels_knn)
print(f'Total number of test images: {len(test_labels)}')
print(f'Total number of correct labels: {sum(pred_labels_knn == test_labels)}') 
print(f'Total classes in test labels: {len(set(test_labels))}')
