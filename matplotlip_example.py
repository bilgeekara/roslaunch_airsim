import matplotlib.pyplot as plt
import numpy as np
x = [24,-10,34,10,-15,42]
y = [33,2,-27,8,-1,34]
figure, axes = plt.subplots(figsize=(8,8))
Drawing_uncolored_circle7 = plt.Circle( (-12.5, 0.5 ), 8 ,fill = True, alpha=0.4, color='red' )
Drawing_uncolored_circle1 = plt.Circle( (-10, 2 ), 8 ,fill = False )
Drawing_uncolored_circle2 = plt.Circle( (24, 33 ), 8 ,fill = False )
Drawing_uncolored_circle3 = plt.Circle( (34 , -27 ), 8 ,fill = False )
Drawing_uncolored_circle4 = plt.Circle( (10, 8 ), 8 ,fill = False )
Drawing_uncolored_circle5 = plt.Circle( (-15, -1 ), 8 ,fill = False)
Drawing_uncolored_circle6 = plt.Circle( (42, 34 ), 8 ,fill = False )

plt.title("İHA'ların Konumları", fontsize=20)                                      
plt.xlabel(" x ekseni ", fontsize=15)
plt.ylabel(" y ekseni ", fontsize=15)                                  
plt.scatter(x, y, marker='o', color='blue') 
axes.set_aspect( 1 )
axes.add_artist( Drawing_uncolored_circle1 )
axes.add_artist( Drawing_uncolored_circle2 )
axes.add_artist( Drawing_uncolored_circle3 )
axes.add_artist( Drawing_uncolored_circle4 )
axes.add_artist( Drawing_uncolored_circle5 )
axes.add_artist( Drawing_uncolored_circle6 )
axes.add_artist( Drawing_uncolored_circle7 )
plt.show()
