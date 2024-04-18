Model: "sequential_1 CNN"
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
3150/3150 [==============================] - 1824s 578ms/step - loss: 0.6221 - accuracy: 0.7065 - precision_1: 0.7065 - recall_1: 0.7065 - f1_score: 0.7060 - logcosh: 0.0859 - val_loss: 0.3885 - val_accuracy: 0.8404 - val_precision_1: 0.8404 - val_recall_1: 0.8404 - val_f1_score: 0.8402 - val_logcosh: 0.0579
Epoch 2/5
3150/3150 [==============================] - 1806s 573ms/step - loss: 0.3761 - accuracy: 0.8219 - precision_1: 0.8219 - recall_1: 0.8219 - f1_score: 0.8219 - logcosh: 0.0572 - val_loss: 0.2623 - val_accuracy: 0.8831 - val_precision_1: 0.8831 - val_recall_1: 0.8831 - val_f1_score: 0.8827 - val_logcosh: 0.0382
Epoch 3/5
3150/3150 [==============================] - 1817s 577ms/step - loss: 0.2530 - accuracy: 0.8938 - precision_1: 0.8938 - recall_1: 0.8938 - f1_score: 0.8938 - logcosh: 0.0364 - val_loss: 0.1383 - val_accuracy: 0.9417 - val_precision_1: 0.9417 - val_recall_1: 0.9417 - val_f1_score: 0.9416 - val_logcosh: 0.0191
Epoch 4/5
3150/3150 [==============================] - 2336s 742ms/step - loss: 0.1794 - accuracy: 0.9261 - precision_1: 0.9261 - recall_1: 0.9261 - f1_score: 0.9261 - logcosh: 0.0252 - val_loss: 0.0948 - val_accuracy: 0.9609 - val_precision_1: 0.9609 - val_recall_1: 0.9609 - val_f1_score: 0.9609 - val_logcosh: 0.0130
Epoch 5/5
3150/3150 [==============================] - 2094s 664ms/step - loss: 0.1376 - accuracy: 0.9435 - precision_1: 0.9435 - recall_1: 0.9435 - f1_score: 0.9435 - logcosh: 0.0191 - val_loss: 0.0853 - val_accuracy: 0.9623 - val_precision_1: 0.9623 - val_recall_1: 0.9623 - val_f1_score: 0.9623 - val_logcosh: 0.0122
876/876 [==============================] - 135s 89ms/step - loss: 0.2251 - accuracy: 0.9238 - precision_1: 0.9238 - recall_1: 0.9238 - f1_score: 0.9236 - logcosh: 0.0265
Test Accuracy: 0.9237554669380188
Test Precision: 0.9237554669380188
Test Recall: 0.9237554669380188
Test F1-Score: [0.9204041  0.92683595]
Test Logarithmic Loss: 0.0264816302806139
