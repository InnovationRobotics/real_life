# realLife - Run everything needed to run the real car
The goal of this software package is to run anything needed in order to communicate with the real vehicle.
It is mainly a launch file.

It starts by trying to run: 
 * rosserial for connecting to the ARDUINO board.
 * apm.launch file for connecting to the pixhawk via MAVROS.
 * the velodyne node and nodelets
 * the innovation pose node
 * the quaternion to roll pitch yaw node
 * the recorder node
 * the rc node
 
 



