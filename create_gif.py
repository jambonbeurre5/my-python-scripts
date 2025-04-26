import imageio.v3 as iio

filenames = ['chara1.png', 'chara2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('chara.gif', images, duration = 500, loop = 0)