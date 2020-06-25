# Kitten RNG

## What?

It's a wonderfully practical python module that generates random numbers based off a kitten livestream. 

## Installation

Make sure you have a 3.* version of python installed along with pip. Then you install via pip from pypi:
```bash
python -m pip install --upgrade kitten-rng
```

## Usage

### The Command Line Tool

To get a massive random number based off the kitten livestream:

```bash
python -m KRNG
```

### The Module

To get a random number from the cat livestream:

```python
from KRNG import RNGs

number = RNGs.KRN()
print(number)
```

To get a random number generator seeded with a Kitten Random Number (KRN):

```python
from KRNG import RNGs

rng = RNGs.KPRNG()
print(rng.random())
```

## Why?

So I was watching Tom Scott videos when I heard [this](https://youtu.be/1cUUfMeOijg). So, now I have created a tool that makes a random number based of a kitten livestream that can be found [here](https://www.youtube.com/watch?v=M5huFQWHyVI). What a wonderfully practical invention.

## How?

So I used pafy to get the url for the actual video file, and then fed that url into a cv2 VideoCapture and got the first frame (which I can do because pafy only gets a few frames of the livestream). Then I feed that data into a sha256 urllib hash function and convert that to a semi-number.
