from Ductsoup_MLX90614 import *
mlx = MLX90614()
print 'Ambient temperature : %8.2f C' % mlx.read_ambient()
print 'Cloud temperature 1 : %8.2f C' % mlx.read_object1()
print 'Cloud temperature 2 : %8.2f C' % mlx.read_object2()
print 'Estimated cloud base: %8.2f M' % mlx.read_cloud_base()
