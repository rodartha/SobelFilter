"""Sobel Filter Class."""
import math
import os
import numpy
import imageio


class SobelFilter:
    """Sobel Filter Class."""

    def __init__(self, image):
        """Initialize variables."""
        self.image = image.astype(numpy.int32)
        self.filtered_image = numpy.zeros(image.shape)

    def find_intensity(self, x, y):
        """Find intensity of a pixel."""
        red = self.image[x,y,0]
        green = self.image[x,y,1]
        blue = self.image[x,y,2]

        return red + green + blue

    def get_gx_gy(self, x, y):
        """Calculate Gx, Gy for each pixel."""
        g_x = 0
        g_y = 0

        if x == 0 and y == 0:
            g_y += 2 * self.find_intensity(x,y+1)

            g_x += 2 * self.find_intensity(x+1,y)

            g_x += self.find_intensity(x+1,y+1)
            g_y += self.find_intensity(x+1,y+1)
        elif x == 0 and y == (self.image.shape[1] - 1):
            g_y += -2 * self.find_intensity(x,y-1)

            g_x += self.find_intensity(x+1,y-1)
            g_y += -(self.find_intensity(x+1,y-1))

            g_x += 2 * self.find_intensity(x+1,y)
        elif x == (self.image.shape[0] - 1) and y == 0:
            g_x += -2 * self.find_intensity(x-1,y)

            g_y += 2 * self.find_intensity(x,y+1)
        elif x == (self.image.shape[0] - 1) and y == (self.image.shape[1] - 1):
            g_x += -(self.find_intensity(x-1,y-1))
            g_y += -(self.find_intensity(x-1,y-1))

            g_x += -2 * self.find_intensity(x-1,y)

            g_y += -2 * self.find_intensity(x,y-1)
        elif x == 0:
            g_y += -2 * self.find_intensity(x,y-1)

            g_y += 2 * self.find_intensity(x,y+1)

            g_x += self.find_intensity(x+1,y-1)
            g_y += -(self.find_intensity(x+1,y-1))

            g_x += 2 * self.find_intensity(x+1,y)

            g_x += self.find_intensity(x+1,y+1)
            g_y += self.find_intensity(x+1,y+1)
        elif y == 0:
            g_x += -2 * self.find_intensity(x-1,y)

            g_x += -(self.find_intensity(x-1, y+1))
            g_y += self.find_intensity(x-1,y+1)

            g_y += 2 * self.find_intensity(x,y+1)

            g_x += 2 * self.find_intensity(x+1,y)

            g_x += self.find_intensity(x+1,y+1)
            g_y += self.find_intensity(x+1,y+1)
        elif x == (self.image.shape[0] - 1):
            g_x += -(self.find_intensity(x-1,y-1))
            g_y += -(self.find_intensity(x-1,y-1))

            g_x += -2 * self.find_intensity(x-1,y)

            g_x += -(self.find_intensity(x-1, y+1))
            g_y += self.find_intensity(x-1,y+1)

            g_y += -2 * self.find_intensity(x,y-1)

            g_y += 2 * self.find_intensity(x,y+1)
        elif y == (self.image.shape[1] - 1):
            g_x += -(self.find_intensity(x-1,y-1))
            g_y += -(self.find_intensity(x-1,y-1))

            g_x += -2 * self.find_intensity(x-1,y)

            g_y += -2 * self.find_intensity(x,y-1)

            g_x += self.find_intensity(x+1,y-1)
            g_y += -(self.find_intensity(x+1,y-1))

            g_x += 2 * self.find_intensity(x+1,y)
        else:
            g_x += -(self.find_intensity(x-1,y-1))
            g_y += -(self.find_intensity(x-1,y-1))

            g_x += -2 * self.find_intensity(x-1,y)

            g_x += -(self.find_intensity(x-1, y+1))
            g_y += self.find_intensity(x-1,y+1)

            g_y += -2 * self.find_intensity(x,y-1)

            g_y += 2 * self.find_intensity(x,y+1)

            g_x += self.find_intensity(x+1,y-1)
            g_y += -(self.find_intensity(x+1,y-1))

            g_x += 2 * self.find_intensity(x+1,y)

            g_x += self.find_intensity(x+1,y+1)
            g_y += self.find_intensity(x+1,y+1)

        return (g_x, g_y)

    def filter_image(self):
        """Filter image into filtered_image."""
        for x in range(0, self.image.shape[0]):
            for y in range(0, self.image.shape[1]):
                g_xy_pair = self.get_gx_gy(x,y)
                g_x = g_xy_pair[0]
                g_y = g_xy_pair[1]
                gradient_length = math.sqrt((g_x * g_x) + (g_y * g_y))

                normalized_length = gradient_length / 4328 * 255
                normalized_length = int(normalized_length)

                for i in range(0,3):
                    self.filtered_image[x,y,i] = normalized_length

        self.filtered_image = self.filtered_image.astype(numpy.uint8)
        

    def get_filtered_image(self):
        """Return filtered image."""
        return self.filtered_image


@click.command()
@click.argument(image_file)
def main(image_file):
    input_dir = "input"
    output_dir = "output"

    print("Beginning Filtering, this may take several seconds...")

    if not os.path.exists(input_dir):
        print("Error: Input Directory does not exist")
        exit(1)
    if not os.path.isfile(input_dir + '/' + image_file):
        print("Error: Image file " + image_file + " does not exist in input folder.")
        exit(1)

    image_in = imageio.imread(input_dir + '/' + image_file)
    sobel = SobelFilter(image_in)
    sobel.filter_image()

    image_out = sobel.get_filtered_image()

    if not os.path.exists(output_dir):
        os.makedir(output_dir)

    file_split = image_file.split('.')
    output_filename = file_split[0] + '_sob.' + file_split[1]

    imageio.imwrite(output_dir + '/' + output_filename, image_out)
    print("Finished Filtering.")


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()
