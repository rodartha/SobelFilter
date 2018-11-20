# SobelFilter
This is a simple python program that runs a Sobel filter on any image type (transparent png excluded).

# Running the filter
to run this filter on an image please run the following command:
````
./bin/sobelfilter IMAGEFILE
````
Where IMAGEFILE is either an image that has been placed in the input folder of this repository.

Output of the program will appear in the output folder with the title [original-picture-name]_sob.[orignal-filetype]

# Examples
Below is an few example of a picture run through the program, you can see more in the Examples folder.

## Before
![alt text](https://github.com/rodartha/SobelFilter/blob/master/Examples/Sagrada-Familia.png)
## After
![alt text](https://github.com/rodartha/SobelFilter/blob/master/Examples/Sagrada-Familia_sob.jpg)

# FAQ
### How long does it take to run?
This depends on the size of the image and the speed of your computer. For smaller images it takes only a couple seconds but for larger images it can take close to a minute.

### How do I set up my virtual environment to run this?
To set up a python virtual environment run the following command:
````
python3 -m venv env
````
To activate/reactivate your virtual environment type the following command:
````
source env/bin/activate
````
For first time set up, run the following command to install everything in setup.py
````
pip install -e .
````
Additionally, if the path for the bash script isn't working run the following
````
chmod +x bin/sobelfilter
````

### What is a sobel filter?
A sobel filter is an image manipulation that uses specific kernel matrices to determine the edges within a picture and then creates a new image based on the found edges.
