
import numpy as np
from PIL import Image


def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = np.array(pixel_values).reshape((height, width, channels))  # Corrected dimensions
    return pixel_values


def sort_and_save_image(image_path, output_path):
    """Sort all pixels in the image and save the result as a new PNG image."""
    image = get_image(image_path)

    # Flatten the image array to 2D for sorting
    flattened_values = image.reshape((-1, image.shape[-1]))
    sorted_values = np.sort(flattened_values, axis=0)

    # Reshape the sorted values back to the original image shape
    sorted_image = sorted_values.reshape(image.shape)

    # Save the sorted image as a new PNG file
    sorted_image = Image.fromarray(sorted_image.astype('uint8'))
    sorted_image.save(output_path)


# Example usage
input_image_path = "1080x1080-image4.png"
output_image_path = "sorted_image4.png"
sort_and_save_image(input_image_path, output_image_path)
