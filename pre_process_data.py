import os
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
            processed_data.append((img, label))
        else:
            continue
    return processed_data

