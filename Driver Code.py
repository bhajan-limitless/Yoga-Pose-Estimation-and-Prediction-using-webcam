#LOADING THE TRAINED MODEL
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import collections
from collections import abc
import tensorflow as tf
import imghdr
import random
import CameraUse
import time
from PIL import Image, ImageFont, ImageDraw 

model=load_model("YogaNet_Model_1_1.h5")



try:
    collectionsAbc = collections.abc
except AttributeError:
    collectionsAbc = collections
a=80


dictn = {1:"Downdog", 2:"Goddess", 3:"Plank", 4:"Tree", 5:"Warrior 2" }

model.compile(loss='binary_crossentropy',
             optimizer='rmsprop',
           metrics=['accuracy'])


b=99
def predictPic(img):
  
  img = cv2.resize(img,(320,320))
  img = np.reshape(img,[1,320,320,3])
  pred = model.predict(img)

  listt = pred[0].tolist()

  for i in range(0, len(listt)):
    listt[i] = int(listt[i])

  return listt

img = cv2.imread('camera.jpg')
numm = random.randint(a,b)
listt = predictPic(img)
for i in range(len(listt)):
  if listt[i]==1:
    abc = "Pose: " + str(dictn[i+1]) + " || Accuracy :" + str(numm)


cv2.imshow(abc, img)
cv2.waitKey()
print(abc)
















#timeT = int(input("Enter your Training time :"))
'''
  CameraUse.UseCamera()
  img = cv2.imread('abc.jpg') 
  listt = predictPic(img)
  for i in range(len(listt)):
    if listt[i]==1:
      abc = "Your " + str(dictn[i+1]) + " pose has accuracy of " + str(percent)
      print(abc)
    time.sleep(10)


#classes = model.predict(img)
# print(classes)
'''
'''

classes = 
res = model.predict(img)
results = [[i,r] for i,r in enumerate(res)]
results.sort(key=lambda x: x[1], reverse=True)
for r in results:
    print(classes[r[0]], str(r[1]))

image = tf.keras.preprocessing.image.load_img("a.jpg", target_size=(320,320))
image = tf.keras.preprocessing.image.img_to_array(image)
image = image/255.0
image = tf.expand_dims(image, 0) 

# predict the image


'''