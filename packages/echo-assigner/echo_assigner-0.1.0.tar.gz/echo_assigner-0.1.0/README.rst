# EchoAssigner

This is a python library that automatically composes an accompaniment part for a melody consisting of a single note in a piano performance.
The created musical score data can be handled as a `music21` object.

* `Input`：MIDI file of a melody consisting of a single note.
* `Output`：MIDI file of the melody with the accompaniment part added.
* Supported midi formats:
    * `4/4 time signature`
    * `BPM constant`
    * `major key`

## Installation

```bash
$ pip install echo-assigner
```

## Usage
See `tutorial.py` for details.

```python
from echo_assigner import EchoAssigner

# create EchoAssigner instance
ea = EchoAssigner(INPUT_MIDI, distmethod=0) 

# check settings params
ea.cui.show_params()

# show assigned measure
ea.cui.show_assigned_part() 

# show accuracy of simulaly of input melody and knowledge base melody
ea.cui.accuracy() 

# create m21.stream.Stream
stream = ea.create.fit_stream() 

# write midi file
stream.write("midi", OUTPUT_MIDI) 

```

## How is this doing
#### 1. Divide the input melody at regular intervals. (Divided intervals can be set with `division` parameter)

#### 2. Extract specific features for each divided interval and express the melody as a vector. The features change depending on the `model` parameter.

#### 3. Calculate the distance between the input melody and the knowledge base melody for each divided interval.

#### 4. Assign the knowledge base melody with the smallest distance to the input melody.


## Class and methods Description
### `class - EchoAssigner()`
#### [need]
* `input_path`: path of input midi file
* `distmethod`: method of distance calculation
    * `0` :Euclidean
    * `1` :Chebyshev
    * `2` :Manhattan
    * `3` :Minkowski
    * `4` :Cosine

#### [optional]
* `logs`: whether to output logs at runtime (default: `True`)
* `model`: model selection
    * `pitchclass`: model with pitch class as feature
    * `statistic`: model with 5 features
        * first pitch 
        * average pitch
        * variance of pitch
        * average change in pitch
        * note density as features

* `division`: section of extracted features
    * `0.5` :1/2 measure
    * `1` :1 measure
    * `2` :2 measure

### `class instance - EchoAssigner.cui`
* `.show_params()`: show settings params
* `.show_assigned_part()`: show information of assigned part
    * `method`:
        * `text`: show as text in terminal
        * `png`: save score as png & musicxml file
        * `midi`: save score as midi file
    * `dirpath`: directly path to save score (default: `None`)
* `.show_similar_melody()`: show information of melody of high similarity
    * `method`:
        * `text`: show as text in terminal
        * `png`: save score as png & musicxml file
        * `midi`: save score as midi file
    * `dirpath`: directly path to save score (default: `None`)
* `.show_melody_vector()`: show melody vector of similarity of input and knowledge base
* `.accuracy()`: show accuracy of similarity of input melody and knowledge base melody


### `class instance - EchoAssigner.create`
* `.score()`: Returns similarity numbers and knowledge base part labels
* `.give_measures()`: Return scale for each measure and note from part label
* `.setup_part()`: Construct and return stream.Part from the scale of each measure and note
* `.shift_notes()`: Shift stream.Part configured in setup_part to the input scale
* `.fit_stream()`: Configure stream.Stream
