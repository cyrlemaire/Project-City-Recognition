# src.domain package

## Submodules

## src.domain.model module


### class src.domain.model.CustomModel(number_classes: int)
Bases: `object`

Implements our custom architecture.


#### model()

* **Type**

    tf.keras.Model



#### image_scaler()

* **Type**

    tf.keras.Sequential



#### pretrained_model()

* **Type**

    tf.keras.Model



#### specific_task_learner()

* **Type**

    tf.keras.Sequential



#### property image_scaler()
Image scaler.


#### property model()
Builds custom model.


#### property pretrained_model()
Pretrained model.


#### property specific_task_learner()
Final layers for specific task learning.

## Module contents
