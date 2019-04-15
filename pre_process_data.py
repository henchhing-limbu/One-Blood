import csv
import os
import pandas as pd
from keras.preprocessing import image

def pre_process_data(directory, label):
    processed_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpeg"):
            # print(os.path.join(directory, filename))
            img = image.load_img(directory + '/' + filename,  target_size=(299, 299, 3),
                                 grayscale=True)
            img = image.img_to_array(img)
            img = img / 255
            processed_data.append([img, label])
        else:
            continue
    return processed_data

bloodcell_subtypes = {
	"LYMPHOCYTE":   [1,0,0,0]
	, "EOSINOPHIL": [0,1,0,0]
	, "MONOCYTE":   [0,0,1,0]
	, "NEUTROPHIL": [0,0,0,1]
}
def create_dataset(directory, data_type):
	processed_data = []
	# creating a csv file
    	# go through the directory
	for key, val in bloodcell_subtypes.items():
		processed_data += pre_process_data(directory + "/" + key, val)
	print("Length of processed data: " + str(len(processed_data)))
	df = pd.DataFrame(processed_data, columns=["Input","Label"])		
		 
	df.to_csv(data_type + ".csv" , index=False)	

create_dataset("/Users/henchhing/Downloads/blood-cells/dataset2-master/images/TEST", "testing")   
