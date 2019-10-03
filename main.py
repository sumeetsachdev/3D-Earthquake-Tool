import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PolyCollection
import pandas as pd
import numpy as np
import tkinter as tk

##def get_map(mag):
def get_map():
    map = Basemap(projection='cyl',llcrnrlat=-90,urcrnrlat=90,\
                llcrnrlon=-180,urcrnrlon=180,resolution='c')

    fig = plt.figure()
    ax = Axes3D(fig)

    ax.add_collection3d(map.drawcoastlines(linewidth=0.25))
    ax.add_collection3d(map.drawcountries(linewidth=0.35))

    polys = []
    for polygon in map.landpolygons:
        polys.append(polygon.get_coords())


    lc = PolyCollection(polys, edgecolor='black',
                        facecolor='#DDDDDD', closed=False)

    ax.add_collection3d(lc)

    df = pd.read_csv('database.csv')
    trench = pd.read_csv('trench.csv')
    ridge = pd.read_csv('ridge.csv')
    transform = pd.read_csv('transform.csv')



##    tempx = trench['Latitude']
##    tempy = trench['Longitude']
##    tx = []
##    ty = []
##    alphabets = [chr(i) for i in range(ord('a'),ord('z')+1)]
##    for latitude, longitude in zip(tempx,tempy):
##        if any(i in alphabets for i in str(latitude)) or any(i in alphabets for i in str(longitude)):
##            pass
##        else:
##            tx.append(latitude)
##            ty.append(longitude)
##    tx = np.array(tx).astype(float)
##    ty = np.array(ty).astype(float)


    tempx = ridge['Latitude']
    tempy = ridge['Longitude']
    rx = []
    ry = []
    for latitude, longitude in zip(tempx,tempy):
        if latitude in ("<", ">"):
            pass
        else:
            rx.append(latitude)
            ry.append(longitude)


    tempx = transform['Latitude']
    tempy = transform['Longitude']
    transx = []
    transy = []
    alphabets = [chr(i) for i in range(ord('a'),ord('z')+1)]
    for latitude, longitude in zip(tempx,tempy):
        if any(i in alphabets for i in str(latitude)) or any(i in alphabets for i in str(longitude)):
            pass
        else:
            transx.append(latitude)
            transy.append(longitude)
    transx = np.array(transx).astype(float)
    transy = np.array(transy).astype(float)

##    mag = int(input("Enter the minimum magnitude "))
##    query = df[df['Magnitude'] >= int(mag)]

##    lat=query['Latitude']
##    long=query['Longitude']        
##    dep=query['Depth']


##    ax.scatter(long, lat, dep, color='blue', label='Earthquake Locations')
    ax.plot(rx, ry, color='yellow', label='Ridge')
##    ax.plot(tx, ty, color='green', label='Trench')
    ax.scatter(transx, transy, color='red', label='Transform')
    ax.set_zlim(-1.1, 700)
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')
    ax.set_zlabel('Depth')
    plt.legend(loc=0)
    ax.invert_zaxis()
    plt.show()

get_map()


##
##HEIGHT = 700
##WIDTH = 800
##
##root = tk.Tk()
##
##canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
##canvas.pack()
##
##"""background_image = tk.PhotoImage(file='bg.jpg')
##background_label = tk.Label(root, image=background_image)
##background_label.place(relwidth=1, relheight=1)"""
##
##
##def clear_entry(event, entry):
##    entry.delete(0, tk.END)
##    usercheck = True
##
##
##frame = tk.Frame(root, bg='#abc',bd=5)
##frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
##
##entry = tk.Entry(frame, bg='white', font=40)
##entry.insert(0, 'Enter the minimum magnitude')
##entry.place(relwidth=0.65, relheight=1)
##entry.bind("<Button-1>", lambda event: clear_entry(event, entry))
##
##button = tk.Button(frame, text='Submit', font=40, command=lambda: get_map(entry.get()))
##button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)
##
##
##lower_frame = tk.Frame(root, bg="#abc", bd=10)
##lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
##
##label = tk.Label(lower_frame)
##label.place(relwidth=1, relheight=1)
##
##
##root.mainloop()
