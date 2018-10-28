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
### Data preperation

### Model structure

### Results


## LEGO ev3dev
### Requirements
LEGO Mindstorm ev3dev image file: https://bit.ly/2ApPNV1
* ev3dev: https://github.com/ev3dev/ev3dev-lang-python
* numpy


