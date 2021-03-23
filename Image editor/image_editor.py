# Name: image_editor
#
# Student IDs: 18004208 and 18091405
#
# Description:
# This program applies 11 different special effects on ppm images
# The user chooses the desired effect and input file and the program
# produces an output file applying the effect selected
#

import os.path

OPTION_RANGE = 11
HEADER_LENGTH = 3
LINE_LENGTH = 10


def greyscale(image_list):
    """ Convert the image_list to greyscale by replacing the r, g, b
        values with an average of the 3 values.

	:return image_list
	"""

    for i in range (0, rows * cols):
        avg = int((image_list[i][0] + image_list[i][1] + image_list[i][2])/3)
        for j in range (0, 3):
            image_list[i][j] = avg
    return image_list


def only_red(image_list):
    """ Remove the green and blue channels in image_list by setting them
	to zero.

	:return image_list
	"""

    for i in range (0, rows * cols):
        image_list[i][1] = 0
        image_list[i][2] = 0
    return image_list


def only_blue(image_list):
    """ Remove the green and red channels in image_list by setting them
	to zero.

	:return image_list
	"""

    for i in range (0, rows * cols):
        image_list[i][0] = 0
        image_list[i][1] = 0
    return image_list



def only_green(image_list):
    """ Remove the blue and red channels in image_list by setting them
	to zero.

	:return image_list
	"""

    for i in range (0, rows * cols):
        image_list[i][0] = 0
        image_list[i][2] = 0
    return image_list


def negative_red(image_list):
    """ Change the red channel in the image_list to its negative value
	by subtracting the value from 255.

	:return image_list
	"""

    for i in range (0, rows * cols):
        image_list[i][0] = 255 - image_list[i][0]
    return image_list



def negative_green(image_list):
    """ Change the green channel in image_list to its negative value
	by subtracting the value from 255.

	:return image_list
	"""

    for i in range (0, rows * cols):
        image_list[i][1] = 255 - image_list[i][1]
    return image_list


def negative_blue(image_list):
    """ Change the blue channel in the image to its negative value
	by subtracting the value from 255.

	:return image_list
	"""

    for i in range (0, rows * cols):
        image_list[i][2] = 255 - image_list[i][2]
    return image_list


def negative_image(image_list):
    """ Change image_list to a negative by subtracting the value
	of each pixel from 255.

	Uses functions previously defined

	:return image_list
	"""

    return negative_red(negative_green(negative_blue(image_list)))


def extreme_contrast(image_list):
    """ Change pixels in image_list to either 0 or 255. If the current value is
	less than the midpoint, set to zero. If the current value is greater than
	the midpoint, set to 255.

	:return image_list
	"""

    for i in range (0, rows * cols):
        for j in range (0,3):
            if image_list[i][j] < int(255/2):
                image_list[i][j]=0
            else:
                image_list[i][j]=255
    return image_list


def green_grad(image_list):
    """Make a greyscale but with green tones instead of grey.

    Uses previously defined functions

    Parameters:
    image_list: list of pixels (as list of rbg values themselves) in image

    :return image_list

    """

    return only_green(greyscale(image_list))


def avg_red(image_list):
    """Replace r channel of pixels with average of r value of all pixels
     to create an interesting colour effect on the picture.

    Parameters:
    image_list: list of pixels (as list of rbg values themselves) in image

    :return image_list

    """
    sum = 0
    for i in range(0, rows * cols):
        sum += image_list[i][0]
        avg = int(sum / (rows * cols))
    for i in range(0, rows * cols):
        image_list[i][0] = avg
    return image_list


def shaking(image_list):
    """Replace r,g,b channels of squares of four pixels with average
     r/g/b value to create "shaky" effect.

    Parameters:
    image_list: list of pixels (as list of rbg values themselves) in image

    :return image_list

   """
    for h in range(0, (rows - 1) * cols - 1, 2):
        for j in range(0, 3):
            avg = int((image_list[h][j] + image_list[h + 1][j] +
                       image_list[h + cols][j] + image_list[h + cols + 1][j])/4)
            image_list[h][j] = avg
            image_list[h + 1][j] = avg
            image_list[h + cols][j] = avg
            image_list[h + cols + 1][j] = avg
        if (h + 2) % cols == 0:
            h += cols
    return image_list


def rotate180(image_list):
    """Swap each pixel from beginning with its correspondent counting
     from end of list to rotate image by 180 degrees.

    Parameters:
    image_list: list of pixels (as list of rbg values themselves) in image

    :return image_list

   """
    for i in range(0, (rows * cols - 1) // 2):
        pixel1 = image_list[i]
        image_list[i] = image_list[(rows * cols) - 1 - i]
        image_list[(rows * cols) - 1 - i] = pixel1
    return image_list


def flip_vertical(image_list):
    """Should swap first pixel from each row with last,
    second with penultimate, etc. to flip image along
    vertical axis.

    Works for tinypix.ppm only, not sure why.

    Parameters:
    image_list: list of pixels (as list of rbg values themselves) in image

    :return image_list

   """
    j = 0
    while j <= ((rows - 1) * cols):
        for i, k in zip(range(j, j + cols // 2), range(0, cols // 2)):
            pixel1 = image_list[i]
            image_list[i] = image_list[j + cols - 1 - k]
            image_list[j + cols - 1 - k] = pixel1
        j = j + cols
    return image_list


def print_menu():
    print("\n\n\toptions: ")
    print("\t\t[1]  convert to greyscale")
    print("\t\t[2]  just the reds")
    print("\t\t[3]  just the blues")
    print("\t\t[4]  just the greens")
    print("\t\t[5]  negative image")
    print("\t\t[6]  extreme contrast")
    print("\t\t[7]  green gradient")
    print("\t\t[8]  average red")
    print("\t\t[9]  shaky")
    print("\t\t[10]  rotate180")
    print("\t\t[11]  flip vertical")

def get_menu_option(prompt):

    valid_option = False

    while not valid_option:
        print_menu()
        try:
            option = int(input(prompt))
            if option in range(1, OPTION_RANGE + 1):
                valid_option = True
            else:
                raise ValueError
        except ValueError:
            print("\n\n\tthat's not a valid choice, please try again.")
    return option


def get_valid_filename(prompt):
    """Use prompt (a string) to ask the user to type the name of a file. If
    the file does not exist, keep asking until they give a valid filename.
    Return the name of that file.
    """

    filename = input(prompt)
    while not os.path.exists(filename):
        print("That file does not exist.")
        filename = input(prompt)
    return filename


def get_dimensions(input_filename):
    """ Read the image size from the file header.
        Return a tuple containing the number of rows and columns.
    """

    with open(input_filename, "r") as file:
        file.readline()
        dimensions = file.readline().split()
    rows = int(dimensions[0])
    cols = int(dimensions[1])

    return rows, cols


def get_file_contents(input_filename):
    """
    Return the tokens in the file as a list.
    Ignore the file header.
    """

    line_count = 1
    read_data = []

    with open(input_filename, "r") as file:

        for line in file:
            # ignore the header
            if line_count <= HEADER_LENGTH:
                line_count += 1
            else:
                read_data += line.split()
    return read_data


def read_image(input_filename):
    """
    Return a list of the pixels in the file.
    """

    read_data = get_file_contents(input_filename)

    # convert all the ascii pixel values to numbers
    read_data = [int(x) for x in read_data]

    # put the r,g,b values in a list
    all_pixels = []
    for i in range(0, len(read_data), 3):
        rgb = read_data[i : i + 3]
        all_pixels.append(rgb)
    return all_pixels


def write_image(rows, cols, image, output_filename):
    """ Write the list of pixels to a file. """

    with open(output_filename, "w") as file:
        file.write("P3\n")
        file.write(str(rows) + " " + str(cols) + "\n")
        file.write("255\n")

        for i in range(len(image)):
            for channel in image[i]:
                file.write(str(channel))
                file.write(" ")
            file.write("\t")

            if i % LINE_LENGTH == 0:
                file.write("\n")


if __name__ == "__main__": #do not need to edit following

    print("Welcome to the Portable Pixmap (PPM) Image Editor!")

    prompt = "\n\tenter the name of the image file: "
    input_image_filename = get_valid_filename(prompt)

    # This isn't a very efficient approach but it's best for the coursework
    rows, cols = get_dimensions(input_image_filename)

    image_list = read_image(input_image_filename)

    output_image_filename = input("\n\tenter the name of the output file: ")

    prompt = "\n\tyour choice: "
    menu_choice = get_menu_option(prompt)

    if menu_choice == 1:
        greyscale(image_list)
    elif menu_choice == 2:
        only_red(image_list)
    elif menu_choice == 3:
        only_blue(image_list)
    elif menu_choice == 4:
        only_green(image_list)
    elif menu_choice == 5:
        negative_image(image_list)
    elif menu_choice == 6:
        extreme_contrast(image_list)
    elif menu_choice == 7:
        green_grad(image_list)
    elif menu_choice == 8:
        avg_red(image_list)
    elif menu_choice == 9:
        shaking(image_list)
    elif menu_choice == 10:
        rotate180(image_list)
    elif menu_choice == 11:
        flip_vertical(image_list)
    write_image(rows, cols, image_list, output_image_filename)
    print("\nImage written to file", output_image_filename)
