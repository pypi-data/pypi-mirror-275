## Installation

You can install the alert-lvm from [PyPI](https://pypi.org/project/realpython-reader/):

    pip install alert-lvm

## How to use

### Analyze image:

```python
from alertlvm import AlertLVM

client = AlertLVM(
    token="<your token here>"
)

scenario_key = "<the key>"

image_path = "<image_path>"

result = client.analyze(scenario_key, image_path)
if result.get("error"):
        print(result.get("code"))
        print(result.get("error_message"))
    else:
        print(result.get("conclusion")) # conclusion of the analysis
        print(result.get("text")) # detail content of the analysis

        # ... your code here ...

        os.remove(result.get("frame"))
```

### Analyze video:

The default setting is to extract and analyze one frame every 750 frames (250 frames/second * 30 seconds):

```python
import os
from alertlvm import AlertLVM

client = AlertLVM(
    token="<your token here>"
)

scenario_key = "<the key>"

video_path = "<video_path>"

for result in client.analyzeVideo(scenario_key, video_path):
    if result.get("error"):
        print(result.get("code"))
        print(result.get("error_message"))
    else:
        print(result.get("frame")) # the file path of a frame extracted from the video that has been sent to the server
        print(result.get("conclusion")) # conclusion of the analysis
        print(result.get("text")) # detail content of the analysis

        # ... your code here ...

        os.remove(result.get("frame"))
```

You can also define your own frame extraction strategy, which can be based on interval: 

```python
def filter(index, frame):
    return index % 900 == 0 # every 900 frames
```

or you can first process the content of the frames:

```python
def filter(index, frame):
    b = process(frame) # define a function to decide if the frame need be analyzed
    return b
```

and then use the ```filter``` function

```python
import os
from alertlvm import AlertLVM

client = AlertLVM(
    token="<your token here>"
)

scenario_key = "<the key>"

video_path = "<video_path>"

for result in client.analyzeVideo(scenario_key, video_path, filter):
    if result.get("error"):
        print(result.get("code"))
        print(result.get("error_message"))
    else:
        print(result.get("frame")) # the file path of a frame extracted from the video that has been sent to the server
        print(result.get("conclusion")) # conclusion of the analysis
        print(result.get("text")) # detail content of the analysis

        # ... your code here ...

        os.remove(result.get("frame"))
```