# TabbyRangers_NASA2018
Project created in NASA Hackathon 2018

## ArtificialBeeColonyAlgorithm
### Requirements
* SwarmPackagePy: https://github.com/SISDevelop/SwarmPackagePy
* numpy
* matplotlib


### Algorithm
```
BEGIN
Initialize the population
Find current best bee for the initial iteration
Calculate the number of scouts, onlookers and employed bees
SET global best to current best
FOR iterator = 0 : iteration
  evaluate fitness for each agent
  sort fitness in ascending order and get best agents
  from best agents list select agents from a to c
  Create new bees which will fly to the best solution
  Evaluate current best agent
  IF function(current best) < function (global best)
    global best = current best
  END IF
END FOR
Save global best
```

## DamageRecognitionCNN
### Requirements
* keras
* tensorflow-gpu
* numpy
### Data Preperation and Generation
![data example](https://github.com/b02902032/TabbyRangers_NASA2018/blob/master/images/data_demo.gif)


To simulate the damage on the sapcecraft surface, i.e. holes and scratches, we applied several stacked formulas to create 3D surfaces. The data is depth bitmaps with size 45x45, and followings are the details: 


|Damage Type                    |Quantity                     |
|-------------------------------|-----------------------------|
|Scratch                        |           2000              |
|Small hole                     |           2000              |
|Big hole                       |           2000              |

### Model Structure
![data example](https://github.com/b02902032/TabbyRangers_NASA2018/blob/master/images/summary.png)

We used a convolutional neural network (CNN) to classify and predict the damage samples, the above is the model structure.

### Results
![data example](https://github.com/b02902032/TabbyRangers_NASA2018/blob/master/images/result.png)


## LEGO ev3dev
### Requirements
LEGO Mindstorm ev3dev image file: https://bit.ly/2ApPNV1
* ev3dev: https://github.com/ev3dev/ev3dev-lang-python
* numpy


