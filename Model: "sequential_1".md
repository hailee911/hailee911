Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d_2 (Conv2D)           (None, 98, 98, 32)        320       
                                                                 
 max_pooling2d_2 (MaxPoolin  (None, 49, 49, 32)        0         
 g2D)                                                            
                                                                 
 conv2d_3 (Conv2D)           (None, 46, 46, 64)        32832     
                                                                 
 max_pooling2d_3 (MaxPoolin  (None, 23, 23, 64)        0         
 g2D)                                                            
                                                                 
 flatten_1 (Flatten)         (None, 33856)             0         
                                                                 
 dense_2 (Dense)             (None, 64)                2166848   
                                                                 
 dropout_1 (Dropout)         (None, 64)                0         
                                                                 
 dense_3 (Dense)             (None, 2)                 130       
                                                                 
=================================================================
Total params: 2200130 (8.39 MB)
Trainable params: 2200130 (8.39 MB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
Epoch 1/5
3150/3150 [==============================] - 1767s 559ms/step - loss: 0.5515 - accuracy: 0.7403 - precision_1: 0.7403 - recall_1: 0.7403 - f1_score: 0.7398 - logcosh: 0.0806 - val_loss: 0.3300 - val_accuracy: 0.8632 - val_precision_1: 0.8632 - val_recall_1: 0.8632 - val_f1_score: 0.8625 - val_logcosh: 0.0482
Epoch 2/5
3150/3150 [==============================] - 990s 314ms/step - loss: 0.3315 - accuracy: 0.8430 - precision_1: 0.8430 - recall_1: 0.8430 - f1_score: 0.8427 - logcosh: 0.0493 - val_loss: 0.2016 - val_accuracy: 0.9182 - val_precision_1: 0.9182 - val_recall_1: 0.9182 - val_f1_score: 0.9179 - val_logcosh: 0.0281
Epoch 3/5
3150/3150 [==============================] - 945s 300ms/step - loss: 0.2315 - accuracy: 0.9021 - precision_1: 0.9021 - recall_1: 0.9021 - f1_score: 0.9021 - logcosh: 0.0329 - val_loss: 0.1485 - val_accuracy: 0.9383 - val_precision_1: 0.9383 - val_recall_1: 0.9383 - val_f1_score: 0.9381 - val_logcosh: 0.0206
Epoch 4/5
3150/3150 [==============================] - 948s 301ms/step - loss: 0.1666 - accuracy: 0.9335 - precision_1: 0.9335 - recall_1: 0.9335 - f1_score: 0.9334 - logcosh: 0.0231 - val_loss: 0.1320 - val_accuracy: 0.9430 - val_precision_1: 0.9430 - val_recall_1: 0.9430 - val_f1_score: 0.9428 - val_logcosh: 0.0188
Epoch 5/5
3150/3150 [==============================] - 1208s 383ms/step - loss: 0.1240 - accuracy: 0.9490 - precision_1: 0.9490 - recall_1: 0.9490 - f1_score: 0.9490 - logcosh: 0.0173 - val_loss: 0.0597 - val_accuracy: 0.9787 - val_precision_1: 0.9787 - val_recall_1: 0.9787 - val_f1_score: 0.9787 - val_logcosh: 0.0077
876/876 [==============================] - 157s 109ms/step - loss: 0.1517 - accuracy: 0.9426 - precision_1: 0.9426 - recall_1: 0.9426 - f1_score: 0.9426 - logcosh: 0.0196
Test Accuracy: 0.9425755143165588
Test Precision: 0.9425755143165588
Test Recall: 0.9425755143165588
Test F1-Score: [0.9416376 0.9434837]
Test Logarithmic Loss: 0.01960800029337406
