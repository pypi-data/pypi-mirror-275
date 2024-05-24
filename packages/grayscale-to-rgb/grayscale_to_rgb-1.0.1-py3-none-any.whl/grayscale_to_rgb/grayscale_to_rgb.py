import sys
from matplotlib import pyplot as plt
from matplotlib import colors as cls
import argparse
from PIL import Image, UnidentifiedImageError

# global keyboardInterrupt (Ctrl-C) handler
# return exit code 129 on keyboard interrupt (Ctrl-C)
# this makes it possible to handle Ctrl-C different in calling bash script
def keyint_except_hook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        sys.exit(129)
    else:
        sys.__excepthook__(exctype, value, traceback)

sys.excepthook = keyint_except_hook

# Unidentified image exception handler
# Returns exit code if a file with an image-type suffix is not verified as image
def verify_img(img_path):
    try:
        test_image = Image.open(img_path)
        test_image.verify()
    except UnidentifiedImageError:
        print('The provided input file',img_path,'could not be verified as an image.\n'
              'The file may be corrupted, empty, or is in fact not an image.')
        sys.exit(130)
def init():
# import grayscale and respective rgb images
    gray_path = args.input_picture_path

    # extract and edit jet cmap
    norm_cols = [0,0.007,0.25,0.5,0.75,0.993,1]
    cols_mod = ["black","blue","cyan","lime", "yellow","red", "white"]
    cols_tuples = list(zip(norm_cols, cols_mod))
    jet_mod_cmap = cls.LinearSegmentedColormap.from_list("", cols_tuples)

    # verify image before loading it
    verify_img(gray_path)

    gray_plt = plt.imread(gray_path)

    plt.axis('off')
    plt.plot(figsize=[gray_plt.shape[1], gray_plt.shape[0]])
    plt.imshow(gray_plt, cmap = jet_mod_cmap)

# save image
    plt.savefig(args.output_picture_path, dpi=600.5,
                bbox_inches='tight', pad_inches=0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Input Arguments
    parser.add_argument("--input-picture-path",
                    required = True)

    parser.add_argument("--output-picture-path",
                    default = 'out_pic.png',
                    required = False)

    args = parser.parse_args()
    init()

