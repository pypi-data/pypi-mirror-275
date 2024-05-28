from .data_preprocessing import upload_datasets

print("DATASET UPLOADING!")
anger_train, anger_dev, anger_data, anger_test = upload_datasets(None, None, None)

fear_train, fear_dev, fear_data, fear_test = upload_datasets(None, None, None)

joy_train, joy_dev, joy_data, joy_test = upload_datasets(None, None, None)

sad_train, sad_dev, sad_data, sad_test = upload_datasets(None, None, None)


print("DATASET UPLOADED!")
