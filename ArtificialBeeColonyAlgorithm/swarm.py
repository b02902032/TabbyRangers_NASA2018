import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation, animation3D

eval_function = [
					tf.ackley_function,
				]
"""
					tf.ackley_function, 
					tf.bukin_function,
					tf.cross_in_tray_function, 
					tf.sphere_function, 
					tf.bohachevsky_function, 
					tf.sum_squares_function, 
					tf.sum_of_different_powers_function, 
					tf.booth_function, 
					tf.matyas_function,
					tf.mccormick_function,
					tf.dixon_price_function,
					tf.six_hump_camel_function,
					tf.three_hump_camel_function,
					tf.easom_function,
					tf.michalewicz_function,
					tf.beale_function,
					tf.drop_wave_function ]
"""

for func in eval_function:
	alh = SwarmPackagePy.aba(50, func, -10, 10, 2, 20)
	animation(alh.get_agents(), func, -10, 10)
	animation3D(alh.get_agents(), func, -10, 10)