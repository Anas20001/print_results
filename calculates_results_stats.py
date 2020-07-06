def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
                     if results_dic[key][2:] == 3:                
            results_stats_dic['n_correct_breed'] += 1 
    """ 
    results_stats_dic = dict()
   
    #Set all counters to zero
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0  
   
    #Process through the results_dic dictionary
    for key in results_dic:
        #Pet and classifier labels match exactly
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
            
        # Pet Image Label is a Dog AND Labels match- counts Correct Breed
        if results_dic[key][2] and results_dic[key][3]:
            results_stats_dic['n_correct_breed'] += 1
            
        # Pet Image Label is a Dog - counts number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # Classifier classifies image as dog (& pet image is a dog)
            # counts number of correct dog classifications
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1    
                
            #Pet image label is not a dog
        else:
            # Classifier classifies image as NOT a dog(& pet image isn't a dog)
            # Counts number of correct NOT dog clasifications.
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1
         

 # Calculates run statistics (counts & percentages) below that are calculated
 # using the counters from above.
    
 # Calculates number of total images
    results_stats_dic['n_images'] = len(results_dic)
