from img_classification import ImgClassificationTension

# インスタンスの作成と画像の推論
classifier = ImgClassificationTension("ResNet152_weights.pth", 2)
results = classifier.predict("../IMG_3824.JPG")
print(results)
