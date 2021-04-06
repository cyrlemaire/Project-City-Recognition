# src.application package

## Submodules

## src.application.predict module

## src.application.train module


### class src.application.train.ModelTraining(model: src.domain.model.CustomModel)
Bases: `object`

Implements training for our custom model.


#### model()

* **Type**

    CustomModel



#### tmp_path()

* **Type**

    str



#### learning_rate_scheduler()

* **Type**

    tf.keras.optimizers.schedules.PolynomialDecay



#### checkpoint()

#### property checkpoint()
Checkpoint callback.


#### property learning_rate_scheduler()
Custom learning rate scheduler.


#### save(path: str)
Saves model to given path.


#### train(train_generator, validation_generator, epochs: int, kwd: dict)
Trains model.


#### unfreeze_pretrained_model()
Unfreezes frozen layers.

## Module contents
