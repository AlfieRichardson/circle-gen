# circle-gen
A quick Python script that creates Java variables that can be used to test if a point on a grid is within a circle. The output file has been included in this repo so you can take a look.

Pair programmed with [sharpened-ferret](https://github.com/sharpened-ferret) over the course of an evening for a mutual friend to use in a project.

```
[user@pc]$ python3 circle-gen.py --help
usage: circle-gen.py [-h] [-m MINIMUM] [-x MAXIMUM]

options:
  -h, --help            show this help message and exit
  -m MINIMUM, --minimum MINIMUM
                        The smallest circle's diameter (Default: 1)
  -x MAXIMUM, --maximum MAXIMUM
                        The biggest circle's diameter (Default: 32)
```