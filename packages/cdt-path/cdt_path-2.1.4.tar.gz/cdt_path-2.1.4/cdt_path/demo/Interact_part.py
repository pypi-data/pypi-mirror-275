import matplotlib.pyplot as plt
import cdt_path as cdt
import matplotlib.tri as tri

fig ,ax = plt.subplots(figsize=(14,8))

floor = cdt.load('floor.json')
cc  = cdt.triangulate(floor)

cdt.border.plot(ax, **cc)

triang = tri.Triangulation(cc['vertices'][:,0],cc['vertices'][:,1],cc['triangles'])

cdt.Interact(ax, triang, title=False)