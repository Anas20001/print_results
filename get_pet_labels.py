from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    filenames = listdir(image_dir)
    
    #create an empty dictionary for pet labels
    results_dic = dict()
    
    #go through each file in the directory and extract only the words of the files containing pet image label
    for idx in range(0, len(filenames), 1):
        if filenames[idx][0] != ".":           
            root_ext = os.path.splitext(filenames[idx]) # remember to import path from os
            image_name = root_ext[0].split('_')
            print(image_name)
            pet_label = " "
            for word in image_name:
                if word.isalpha():
                    pet_label += word + " "
                    
            pet_label = pet_label.strip()        
            if filenames[idx] not in results_dic:
                results_dic[filenames[idx]] = [pet_label]
                
            else:
                print("Warning: Duplicate files exist in directory", filenames[idx])
    return results_dic
