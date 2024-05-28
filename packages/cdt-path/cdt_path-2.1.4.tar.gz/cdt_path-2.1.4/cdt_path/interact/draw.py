import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.backend_bases import MouseButton
import json
class Draw:
	def __init__(self, ax, save='data', r=1):
		self.ax = ax
		# self.r = r
		self.points = []
		self.segments = []
		self.l=0
		
		plt.connect('button_press_event', self.on_click)
		plt.connect('key_press_event', self.on_press)
		ax.axes.set_aspect('equal')
		plt.show()
		
		for i in range(self.l,len(self.points)-1):
			self.segments.append((i,i+1))
		self.segments.append((len(self.points)-1,self.l))
		data={"vertices":self.points, "segments":self.segments}
	
		if save[-5:]!=".json":
			save+='.json'
			
		with open(save,'w',encoding='utf-8') as f:
			json.dump(data, f, ensure_ascii=False, indent=4)
			
	def on_click(self, event):  
		if event.inaxes:
			rounded_x = round(event.xdata, r)  
			rounded_y = round(event.ydata, r)  
			  
			self.points.append((rounded_x, rounded_y))  
			print(f"Added point: ({rounded_x}, {rounded_y})")  
			  
			plt.scatter(rounded_x, rounded_y, color='red')  # 可视化新添加的点  
			plt.draw()  # 更新图形
	  
	def on_press(self, event):
		print('press', event.key)
		if event.key == 'x':
			for i in range(self.l,len(self.points)-1):
				self.segments.append((i,i+1))
			self.segments.append((len(self.points)-1,self.l))
			self.l=len(self.points)
			
	  