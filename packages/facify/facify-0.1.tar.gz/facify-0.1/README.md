# facify Package

  This is the package extracting faces form images.

## Installation

Install facify with pip

```bash
  pip install facify
```

    
## Usage/Examples

To see loaded image
```python
from facify import show
path = 'image_path'
show(path)
```
To extract faces from images
```python
from facify import detect
path = 'image_path'
detect(path)
```

The extracted faces stored in faces directory
