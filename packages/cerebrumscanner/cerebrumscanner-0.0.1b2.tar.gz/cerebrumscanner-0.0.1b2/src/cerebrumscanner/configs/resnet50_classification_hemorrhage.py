# License: BSD
# Author: Sasank Chilamkurthy

from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy

from PIL import Image

plt.ion()   # interactive mode


# Data augmentation and normalization for training
# Just normalization for validation
data_transforms = {
    'train': transforms.Compose([
        #transforms.RandomResizedCrop(224),
        #transforms.Resize((800,600)),
        transforms.Resize((256,256)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        # transforms.Resize((800,600)),
        transforms.Resize((256,256)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

# data_dir = os.path.join(os.getcwd(), 'data','rsna-mini','train-png-splitted')
data_dir = os.path.join(os.getcwd(), 'data','rsna','train-png-splitted')
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                          data_transforms[x])
                  for x in ['train', 'val']}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4,
                                             shuffle=True, num_workers=4)
              for x in ['train', 'val']}
dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
class_names = image_datasets['train'].classes




device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")



def read_dataset_csv(csv_path):
    import csv
    data_dict = dict()
    # Open the CSV file
    with open(csv_path, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        
        # Read the header row
        header = next(reader)
        
        # Print the header
        print("Header:", header)
        
        # Read and process each row of data
        for row in reader:

            id, hem_type, val = row[0].split('_')[1], row[0].split('_')[2], float(row[1])

            if f'{id}' in data_dict.keys(): pass
            else: data_dict[f'{id}'] = {}
            data_dict[f'{id}'][hem_type] = val
            valid_hem_types = ['epidural',
                            'intraparenchymal',
                            'intraventricular',
                            'subarachnoid',
                            'subdural',
                            'any',]
            if hem_type in valid_hem_types: pass
            else:
                print('Hemorrhage type error!') 
                import pdb; pdb.set_trace()

        # import pdb; pdb.set_trace()
    return data_dict


def imshow(inp, title=None):
    """Imshow for Tensor."""
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated

'''
# Get a batch of training data
inputs, classes = next(iter(dataloaders['train']))

# Make a grid from batch
out = torchvision.utils.make_grid(inputs)

imshow(out, title=[class_names[x] for x in classes])
'''



def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since = time.time()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        # Each epoch has a training and validation phase
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()   # Set model to evaluate mode

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    # backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                # statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
            if phase == 'train':
                scheduler.step()

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]

            print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_acc))

            # deep copy the model
            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())

        print()

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    models_path = os.path.join(os.getcwd(),'models')
    if not os.path.exists(models_path): os.mkdir(models_path)
                
    # save the model
    torch.save(best_model_wts, os.path.join(os.getcwd(),'models','hemorrhage.pth'))

    # load best model weights
    model.load_state_dict(best_model_wts)

    return model


def visualize_model(model, num_images=6):
    was_training = model.training
    model.eval()
    images_so_far = 0
    fig = plt.figure()

    csv_path = "C:\\Users\\cgksu\\Dropbox\\Business\\Nekodu_Technology\\IndividualFolders\\Cihan\\cerebrum-scanner\\data\\rsna\\stage_2_train.csv"
    data_dict = read_dataset_csv(csv_path)
    #######
    
    from PIL import Image
    import numpy as np

    paths = []
    path_to_file = 'C:\\Users\\cgksu\\Dropbox\\Business\\Nekodu_Technology\\IndividualFolders\\Cihan\\cerebrum-scanner\\data\\rsna\\train-png-splitted\\val\\nohemorrhage\\ID_0b35992d3.png' # no-hemorrhage
    paths.append(path_to_file)
    path_to_file = 'C:\\Users\\cgksu\\Dropbox\\Business\\Nekodu_Technology\\IndividualFolders\\Cihan\\cerebrum-scanner\\data\\rsna\\train-png-splitted\\val\\hemorrhage\\ID_0bd6cfba5.png' # intraparenchymal
    paths.append(path_to_file)

    path_to_file = 'C:\\Users\\cgksu\\Dropbox\\Business\\Nekodu_Technology\\IndividualFolders\\Cihan\\cerebrum-scanner\\data\\rsna\\train-png-splitted\\val\\hemorrhage\\ID_6de957d4f.png' # epidural
    paths.append(path_to_file)

    # path_to_file = 'C:\\Users\\cgksu\\Dropbox\\Business\\Nekodu_Technology\\IndividualFolders\\Cihan\\cerebrum-scanner\\data\\rsna\\train-png-splitted\\val\\hemorrhage\\ID_df3a49785.png' # subarachnoid
    # paths.append(path_to_file)
    # path_to_file = 'C:\\Users\\cgksu\\Dropbox\\Business\\Nekodu_Technology\\IndividualFolders\\Cihan\\cerebrum-scanner\\data\\rsna\\train-png-splitted\\val\\hemorrhage\\ID_e5d2595fa.png' # subdural
    # paths.append(path_to_file)
    
    img_id = 0
    for path_to_file in paths:
        img_id += 1    
        im = Image.open(path_to_file)
        im_frame = im.convert('RGB')
        np_frame = np.array(im_frame)
        img_PIL = Image.fromarray(np.uint8((np_frame - np.min(np_frame))/np.max(np_frame - np.min(np_frame))*255))
        
        my_dataloader = {
            'train': transforms.Compose([
                #transforms.RandomResizedCrop(224),
                #transforms.Resize((800,600)),
                transforms.Resize((256,256)),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ]),
            'val': transforms.Compose([
                # transforms.Resize((800,600)),
                transforms.Resize((256,256)),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ]),
        }

        with torch.no_grad():
            input_image_trans = my_dataloader['val'](img_PIL)
            
            input_image_device = input_image_trans.to(device)
            input_ready = torch.unsqueeze(input_image_device,0)
            output = model(input_ready)
            _, preds = torch.max(output, 1)

        model.train(mode=was_training)

        ax = plt.subplot(1, 3, img_id)
        ax.axis('off')
        hem_type = 'intraparenchymal' if img_id==2 else 'epidural' 
        title_to_show = 'AI: No hemorrhage\nNeurologist: No hemorrhage' if int(preds) == 1 else f'AI: Suspected hemorrhage\nNeurologist: {hem_type}'
        ax.set_title(title_to_show, color='g', loc='left') if int(preds) == 1 else ax.set_title(title_to_show, color='r', loc='left')
        
        plt.imshow(np_frame)

    import pdb; pdb.set_trace()




    # with torch.no_grad():
    #     for i, (inputs, labels) in enumerate(dataloaders['val']):
    #         inputs = inputs.to(device)
    #         labels = labels.to(device)

    #         outputs = model(inputs)
    #         _, preds = torch.max(outputs, 1)

    #         for j in range(inputs.size()[0]):
    #             images_so_far += 1
    #             ax = plt.subplot(num_images//2, 2, images_so_far)
    #             ax.axis('off')
    #             ax.set_title('predicted: {}'.format(class_names[preds[j]]))
    #             imshow(inputs.cpu().data[j])

    #             if images_so_far == num_images:
    #                 model.train(mode=was_training)
    #                 return
    #     model.train(mode=was_training)



def main():

    # import pdb; pdb.set_trace()      
    # model_ft = models.resnet50(pretrained=True)
    # model_ft = models.resnet50(weights='ResNet50_Weights.DEFAULT')
    model_ft = models.resnet18(weights='ResNet18_Weights.DEFAULT')


    num_ftrs = model_ft.fc.in_features
    # Here the size of each output sample is set to 2.
    # Alternatively, it can be generalized to nn.Linear(num_ftrs, len(class_names)).
    model_ft.fc = nn.Linear(num_ftrs, 2)

    model_ft = model_ft.to(device)

    criterion = nn.CrossEntropyLoss()

    # Here 's just to train!
    '''
    # Observe that all parameters are being optimized
    optimizer_ft = optim.SGD(model_ft.parameters(), lr=0.001, momentum=0.9)

    # Decay LR by a factor of 0.1 every 7 epochs
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)

    model_ft = train_model(model_ft, criterion, optimizer_ft, exp_lr_scheduler,
                        num_epochs=5)

    '''
    
    model_ft.load_state_dict(torch.load('C:\\Users\\cgksu\\Dropbox\\Business\\Nekodu_Technology\\IndividualFolders\\Cihan\\cerebrum-scanner\\models\\hemorrhage.pth'))       

    visualize_model(model_ft)

    import pdb; pdb.set_trace()         



if __name__ == '__main__':
    main()
