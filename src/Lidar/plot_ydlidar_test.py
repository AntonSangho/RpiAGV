import os
import ydlidar
import time
import sys
from matplotlib.patches import Arc
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

RMAX = 32.0
#RMAX = 16.0


fig = plt.figure()
fig.canvas.set_window_title('YDLidar LIDAR Monitor')
lidar_polar = plt.subplot(polar=True)
lidar_polar.autoscale_view(True,True,True)
lidar_polar.set_rmax(RMAX)
lidar_polar.grid(True)
ports = ydlidar.lidarPortList();
port = "/dev/ydlidar";
for key, value in ports.items():
    port = value;
    
laser = ydlidar.CYdLidar();
laser.setlidaropt(ydlidar.LidarPropSerialPort, port);
#laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 230400)
laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 128000);
laser.setlidaropt(ydlidar.LidarPropLidarType, ydlidar.TYPE_TRIANGLE);
laser.setlidaropt(ydlidar.LidarPropDeviceType, ydlidar.YDLIDAR_TYPE_SERIAL);
laser.setlidaropt(ydlidar.LidarPropScanFrequency, 10.0);
#laser.setlidaropt(ydlidar.LidarPropScanFrequency, 13.0);
laser.setlidaropt(ydlidar.LidarPropSampleRate, 9);
#laser.setlidaropt(ydlidar.LidarPropSampleRate, 16);
#laser.setlidaropt(ydlidar.LidarPropSingleChannel, False);
laser.setlidaropt(ydlidar.LidarPropSingleChannel, True);
scan = ydlidar.LaserScan()

def animate(num):
    
    r = laser.doProcessSimple(scan);
    if r:
        angle = []
        ran = []
        intensity = []
        for point in scan.points:
            angle.append(point.angle);
            ran.append(point.range);
            intensity.append(point.intensity);
        lidar_polar.clear()
        #lidar_polar.scatter(angle, ran, c=intensity, cmap='hsv', alpha=0.95)
        lidar_polar.scatter(angle, ran, c=intensity, cmap='hsv', alpha=0.30)

ret = laser.initialize();
if ret:
    ret = laser.turnOn();
    if ret:
        #ani = animation.FuncAnimation(fig, animate, interval=50)
        ani = animation.FuncAnimation(fig, animate, interval=25)
        plt.show()
    laser.turnOff();
laser.disconnecting();
plt.close();
