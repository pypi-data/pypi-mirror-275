from .data_preprocessing import upload_datasets

print("DATASET UPLOADING!")
anger_train, anger_dev, anger_data, anger_test = upload_datasets(
    "../dataset/2018-EI-oc-En-anger-dev.txt",
    "../dataset/EI-oc-En-anger-train.txt",
    "../dataset/2018-EI-oc-En-anger-test.txt",
)

fear_train, fear_dev, fear_data, fear_test = upload_datasets(
    "../dataset/EI-oc-En-fear-train.txt",
    "../dataset/2018-EI-oc-En-fear-dev.txt",
    "../dataset/2018-EI-oc-En-fear-test.txt",
)

joy_train, joy_dev, joy_data, joy_test = upload_datasets(
    "../dataset/EI-oc-En-joy-train.txt",
    "../dataset/2018-EI-oc-En-joy-dev.txt",
    "../dataset/2018-EI-oc-En-joy-test.txt",
)

sad_train, sad_dev, sad_data, sad_test = upload_datasets(
    "../dataset/EI-oc-En-sadness-train.txt",
    "../dataset/2018-EI-oc-En-sadness-dev.txt",
    "../dataset/2018-EI-oc-En-sadness-test.txt",
)

print("DATASET UPLOADED!")
