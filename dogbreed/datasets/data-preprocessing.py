import os
import csv
import shutil
import random
def divide_dataset():
    row_list = []
    with open('labels.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            row_list.append(row)
    row_list = row_list[1:]    
    type_list = set([i[1] for i in row_list])
    train_dir_list = ['./train/'+ i for i in type_list]
    val_dir_list = ['./val/'+ i for i in type_list]
    
    for each in train_dir_list:
        if os.path.exists(each) == False:
            os.makedirs(each)
    
    for each in val_dir_list:
        if os.path.exists(each) == False:
            os.makedirs(each)
    
    prefix = ['./train/', './val/']
    random.seed(0)
    f = lambda x:prefix[1] if x>0.8 else prefix[0]
    
    file_list = [['./train/' +i[0]+'.jpg',f(random.random())+i[1]+'/'+i[0]+'.jpg'] for i in row_list]
    
    for each in file_list:
        shutil.copy(each[0],each[1])