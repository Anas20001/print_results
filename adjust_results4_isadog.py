dognames_dic = dict()
    # Reads in dognames from dogfile, 1 name per line & automatically closes file
    with open(dogfile, "r") as infile:
        line = infile.readline()
        while line != "":
         #process line by striping new line from line
            line = line.rstrip()
            
            #adds dogname to dogsnames_dic if it doesn't already exist in dic
            if line not in dognames_dic:
                dognames_dic[line] = 1
            else:
                print ("Warning: Duplicate dog names", line)
            
            #Reads in next line in file to be processed with while loop if this line isn't              empty (EOF)
            line = infile.readline()
        
     # Add to whether pet labels & classifier labels are dogs by appending
    # two items to end of value(List) in results_dic. 
    # List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND 
    # List Index 4 = whether(1) or not(0) Classifier Label is a dog
    # How - iterate through results_dic if labels are found in dognames_dic
    # then label "is a dog" index3/4=1 otherwise index3/4=0 "not a dog"
    for key in results_dic:
        #If pet image label is found in dognames_dic, it IS a dog
        if results_dic[key][0] in dognames_dic:
            #If classifier label IS found in dognames_dic, it IS a dog hence append 
            #(1,1) to results_dic - both pet and classifier labels are dogs.
            
            #If classifier label IS NOT in dognames_dic, then it IS NOT a dog, append
            #(1,0) to results_dic - only pet image label is a dog.
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1,1))
            else:
                results_dic[key].extend((1,0))
       
        #If pet image label IS NOT in dognames_dic but classifier label IS in dognames_dic         #then append (0,1) - only classifier label is a dog.
        else:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0,1))
            #Neither pet image label nor classifier label is a dog hence append (0,0)
            else:
                results_dic[key].extend((0,0))
