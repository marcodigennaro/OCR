from matplotlib import pyplot as plt


def display_image_inline(im_path, output_path=None):
    """
    Display an image inline in a Jupyter notebook.

    Parameters:
    im_path (str): The file path to the image to be displayed.

    This function reads an image from the specified file path, calculates the
    appropriate figure size based on the image dimensions and a fixed DPI (dots per inch),
    and then displays the image using Matplotlib with axes and spines hidden.
    """
    dpi = 80  # Dots per inch for the figure
    im_data = plt.imread(im_path)  # Read the image data from the file

    height, width = im_data.shape[:2]  # Get the image dimensions

    # Calculate the figure size in inches
    fig_size = width / float(dpi) / 2, height / float(dpi) / 2

    # Create a figure with the calculated size and add an axes that takes up the full figure
    fig = plt.figure(figsize=fig_size)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide the axes, spines, and ticks
    ax.axis('off')

    # Display the image
    ax.imshow(im_data, cmap='gray')

    plt.show()  # Show the figure

    if output_path:
        fig.savefig(output_path, bbox_inches='tight', pad_inches=0, dpi=dpi)

    plt.close(fig)  # Close the figure to free up memory
