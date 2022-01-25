# aperture-test
The modified code of a simple program that opens a fits file, finds the sources
within it and plots circles around each source discovered.

This was an example to *refactor* the code to make it more managable. 
Steps taken included;
* Naming variables well to help the code be understood.
* Adding in CONSTANTS to help change code behaviour without having to scroll through code.
* Wrapping up the main part of the program into a function.
* Placing the function in its own file `functions.py` then importing it into the `aperture.py` script
* Moving the CONSTANTS and logging settings to `settings.py` and importing them in `aperture.py`


## Running the code

The code requires python3 and astropy, numpy and matplotlib.

To install these run the following commands in a terminal

```shell
pip install matplotlib
pip install numpy
pip install astropy
```

If that has worked you may be able to run the examply by typing;

```shell
python3 aperture.py
```
