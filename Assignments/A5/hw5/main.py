#Starter code prepared by Borna Ghotbi, Polina Zablotskaia, and Ariel Shann for Computer Vision
#based on a MATLAB code by James Hays and Sam Birch 

import numpy as np
from util import load, build_vocabulary, get_bags_of_sifts
from classifiers import nearest_neighbor_classify, svm_classify
import pickle

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

#For this assignment, you will need to report performance for sift features on two different classifiers:
# 1) Bag of sift features and nearest neighbor classifier
# 2) Bag of sift features and linear SVM classifier

#For simplicity you can define a "num_train_per_cat" vairable, limiting the number of
#examples per category. num_train_per_cat = 100 for intance.

#Sample images from the training/testing dataset. 
#You can limit number of samples by using the n_sample parameter.

print('Getting paths and labels for all train and test data\n')
train_image_paths, train_labels = load("sift/train")
test_image_paths, test_labels = load("sift/test")
       

''' Step 1: Represent each image with the appropriate feature
 Each function to construct features should return an N x d matrix, where
 N is the number of paths passed to the function and d is the 
 dimensionality of each image representation. See the starter code for
 each function for more details. '''

        
recalculate = False  # Set this to True if you want to recalculate features

if not recalculate:
    # Load the saved kmeans model, feature vectors, and labels
    with open('kmeans_model.pkl', 'rb') as f:
        kmeans = pickle.load(f)
    with open('train_image_feats.pkl', 'rb') as f:
        train_image_feats = pickle.load(f)
    with open('train_labels.pkl', 'rb') as f:
        train_labels = pickle.load(f)
    with open('test_image_feats.pkl', 'rb') as f:
        test_image_feats = pickle.load(f)
    with open('test_labels.pkl', 'rb') as f:
        test_labels = pickle.load(f)
else:
    # Code for recalculating features
    kmeans = build_vocabulary(train_image_paths, vocab_size=60)
    train_image_feats = get_bags_of_sifts(train_image_paths, kmeans)
    test_image_feats = get_bags_of_sifts(test_image_paths, kmeans)
    
        # Save the kmeans model, feature vectors, and labels
    with open('kmeans_model.pkl', 'wb') as f:
        pickle.dump(kmeans, f)
    with open('train_image_feats.pkl', 'wb') as f:
        pickle.dump(train_image_feats, f)
    with open('train_labels.pkl', 'wb') as f:
        pickle.dump(train_labels, f)
    with open('test_image_feats.pkl', 'wb') as f:
        pickle.dump(test_image_feats, f)
    with open('test_labels.pkl', 'wb') as f:
        pickle.dump(test_labels, f)

        
#If you want to avoid recomputing the features while debugging the
#classifiers, you can either 'save' and 'load' the extracted features
#to/from a file.

# Come up with the average histogram for each category
def get_average_histograms(image_feats, labels, num_categories):
    # Initialize a matrix to hold the sum of histograms for each category
    sum_histograms = np.zeros((num_categories, image_feats.shape[1]))
    count_per_category = np.zeros(num_categories)

    # Sum histograms for each category
    for i, histogram in enumerate(image_feats):
        category = int(labels[i])        
        sum_histograms[category] += histogram
        count_per_category[category] += 1

    # Compute average histograms
    avg_histograms = sum_histograms / count_per_category[:, None]

    return avg_histograms

# avg_histograms = get_average_histograms(train_image_feats, train_labels, 15)

def plot_average_histograms(avg_histograms, num_categories):
    plt.figure(figsize=(15, 10))
    for i in range(num_categories):
        plt.subplot(3, 5, i+1)  # Adjust the grid size based on your number of categories
        plt.bar(range(avg_histograms.shape[1]), avg_histograms[i])
        plt.title(f'Category {i}')
        plt.xlabel('Cluster Index')
        plt.ylabel('Average Frequency')

    plt.tight_layout()
    plt.show()

# plot_average_histograms(avg_histograms, 15)


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


print('---Evaluation---\n')
# Step 3: Build a confusion matrix and score the recognition system for 
#         each of the classifiers.
# TODO: In this step you will be doing evaluation. 
# 1) Calculate the total accuracy of your model by counting number
#   of true positives and true negatives over all. 
# 2) Build a Confusion matrix and visualize it. 
#   You will need to convert the one-hot format labels back
#   to their category name format.

def calculate_accuracy(true_labels, predicted_labels):
    correct_predictions = np.sum(true_labels == predicted_labels)
    total_predictions = len(true_labels)
    accuracy = correct_predictions / total_predictions
    return accuracy

accuracy_knn = calculate_accuracy(test_labels, pred_labels_knn)
accuracy_svm = calculate_accuracy(test_labels, pred_labels_svm)

print(f"Accuracy of KNN Classifier: {accuracy_knn * 100:.2f}%")
print(f"Accuracy of SVM Classifier: {accuracy_svm * 100:.2f}%")

def plot_confusion_matrix(true_labels, predicted_labels, classes, title):
    matrix = confusion_matrix(true_labels, predicted_labels, labels=classes)
    plt.figure(figsize=(10, 8))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='Blues', xticklabels=classes, yticklabels=classes)
    plt.title(title)
    plt.ylabel('Actual Labels')
    plt.xlabel('Predicted Labels')
    plt.show()

# Assuming that your labels are not one-hot encoded. If they are, convert them first.
classes = np.unique(test_labels)  # Get the unique class labels

plot_confusion_matrix(test_labels, pred_labels_knn, classes, "Confusion Matrix for KNN Classifier")
plot_confusion_matrix(test_labels, pred_labels_svm, classes, "Confusion Matrix for SVM Classifier")

# Interpreting your performance with 100 training examples per category:
#  accuracy  =   0 -> Your code is broken (probably not the classifier's
#                     fault! A classifier would have to be amazing to
#                     perform this badly).
#  accuracy ~= .10 -> Your performance is chance. Something is broken or
#                     you ran the starter code unchanged.
#  accuracy ~= .40 -> Rough performance with bag of SIFT and nearest
#                     neighbor classifier. 
#  accuracy ~= .50 -> You've gotten things roughly correct with bag of
#                     SIFT and a linear SVM classifier.
#  accuracy >= .60 -> You've added in spatial information somehow or you've
#                     added additional, complementary image features. This
#                     represents state of the art in Lazebnik et al 2006.
#  accuracy >= .85 -> You've done extremely well. This is the state of the
#                     art in the 2010 SUN database paper from fusing many 
#                     features. Don't trust this number unless you actually
#                     measure many random splits.
#  accuracy >= .90 -> You used modern deep features trained on much larger
#                     image databases.
#  accuracy >= .96 -> You can beat a human at this task. This isn't a
#                     realistic number. Some accuracy calculation is broken
#                     or your classifier is cheating and seeing the test
#                     labels.
