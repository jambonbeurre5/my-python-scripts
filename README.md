# GIF Creation Script

## Prerequisites
The script requires the `imageio` library to be installed. You can install it using pip:

```pip install imageio```

## Customization

* Edit the filenames list in the script to include the names of your desired image files, in the order you want them to appear in the GIF.

* Change 'chara.gif' in the iio.imwrite() line to set a different name for the output GIF file.

* Adjust the duration parameter (in milliseconds) to control how long each frame is displayed.

  ```Example: duration=500 means each frame lasts half a second.```

* The loop=0 parameter sets the GIF to loop infinitely. You can change it if you want the GIF to stop after a number of loops.
