
# coding: utf-8

from math import log
import argparse

def load_data(filepath):
    file = open(filepath)
    line = file.readline()
    line = line.strip()
    labels = line.split(',')
    data_set = []
    line = file.readline()
    class_value = []
    
    while line:
        line = line.strip()
        line_list = line.split(',')
        data_set.append(line_list)
        line = file.readline()
        if line_list[-1] not in class_value:
            class_value.append(line_list[-1])
        
    return data_set,labels[:-1],class_value


def predict(mdl_dict, labels, class_values, test_data):
    
    key = list(mdl_dict.keys())[0]
    index_number = labels.index(key)
    
    while mdl_dict[key][test_data[index_number]] not in class_value:
        mdl_dict = mdl_dict[key][test_data[index_number]]
        key = list(mdl_dict.keys())[0]
        index_number = labels.index(key)
    
    return mdl_dict[key][test_data[index_number]]


def majority(classList):
    cl_count={}
    for class_v in classList:
        if class_v not in cl_count.keys(): 
            cl_count[class_v] = 0
        cl_count[class_v] += 1
    
    max_number = -1
    class_value = None
    for key in cl_count.keys():
        if cl_count[key] > max_number:
            max_number = cl_count[key]
            class_value = key
    
    return class_value


def split(data, index, val):
    new_data = []
    for data_list in data:
        if data_list[index] == val:
            reduced = data_list[:index]
            reduced.extend(data_list[index+1:])
            new_data.append(reduced)
    return new_data


def entropy(data):
    entries = len(data)
    labels = {}
    for data_list in data:
        label = data_list[-1]
        if label not in labels.keys():
            labels[label] = 0
        labels[label] += 1
    entropy = 0.0
    for key in labels:
        prob = float(labels[key])/entries
        entropy -= prob * log(prob,2)
    return entropy


def choose_attribute(data):
    attributes = len(data[0]) - 1
    baseEntropy = entropy(data)
    max_InfoGain = 0.0;
    bestattr = -1
    for i in range(attributes):
        featList = [d[i] for d in data]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            new_data = split(data, i, value)
            prob = len(new_data)/float(len(data))
            newEntropy += prob * entropy(new_data)
        infoGain = baseEntropy - newEntropy
        if infoGain > max_InfoGain:
            max_InfoGain = infoGain
            bestattr = i
    return bestattr


def tree(data,labels):
    classList = [d[-1] for d in data]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # if there is no more attribute, return the majority of remaining classes 
    if len(data[0]) == 1:
        return majority(classList)
    # choose the best attribute
    best_feat = choose_attribute(data)
    best_label = labels[best_feat]
    tree_contain = {best_label:{}}
    #del(labels[best_feat])
    labels = labels[:best_feat] + labels[best_feat+1:]
    featValues = [d[best_feat] for d in data]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        tree_contain[best_label][value] = tree(split(data, best_feat, value),subLabels)
    return tree_contain


parser = argparse.ArgumentParser(description='DT')
parser.add_argument('-d','--datapath', default='iris.data.txt')
args = parser.parse_args()
datapath = args.datapath
data_set, labels, class_value = load_data(datapath)
model = tree(data_set,labels)
print(model)
right_number = 0
for data_list in data_set:
    result = predict(model, labels, class_value, data_list[:-1])
    if result == data_list[-1]:
        right_number += 1     
print('accuracy: {}%'.format(right_number/len(data_set)*100))


print('Please type the attributes to predict (END means exit):')
line = input()
while not line.startswith('END'):
    line = line.strip()
    test_data = line.split(' ')
    if len(test_data) != len(labels):
        test_data = line.split(',')
    result = predict(model, labels, class_value, test_data)
    print(result)
    print('Please type the attributes to predict (END means exit):')
    line = input()




