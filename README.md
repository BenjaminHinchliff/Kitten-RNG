# Kitten RNG

## Why?

So I was watching Tom Scott videos when I heard [this](https://youtu.be/1cUUfMeOijg). So, now I have created a tool that makes a random number based of a kitten livestream that can be found [here](https://www.youtube.com/watch?v=M5huFQWHyVI). What a wonderfully practical invention.

## How?

So I used pafy to get the url for the actual video file, and then fed that url into a cv2 VideoCapture and got the first frame (which I can do because pafy only gets a few frames of the livestream). Then I feed that data into a sha256 urllib hash function and convert that to a semi-number.
