Controlling Mindstorm with Python
=================================
to create a new robot to control, use the command
  
    robot = Robot(robot_name)
    
where robot_name will look something like 'ICTCLUB1'.
This robot can't do anything, we need to extend it to give it some actions.

Mover Extension
---------------
to extend your robot with the mover extension use the command

    robot.extend(Mover(left_motor_port, right_motor_port))
    
where left\_motor\_port and right\_motor\_port will look something like PORT_C and PORT_B.

this extension will give your robot a load of new actions.

**robot.forward(seconds, power)**
    
move forward for specified number of seconds, power should be between 1-100
example:

    robot.forward(2, 60)
          
**robot.backward(seconds, power)**

like forward but in the other direction

**robot.turnLeft(degrees)**

turns left for the specified number of degrees (roughly)
example:

    robot.turnLeft(90)
        
**robot.turnRight(degrees)**

turns right for the specified number of degrees (roughly)
        
**robot.startTurningLeft(power)**

robot turns left forever until you call robot.stopTurning(), power should be between 1-100
example:
    
    robot.startTurningLeft(65)
        
**robot.startTurningRight(power)**

like startTurningLeft but in the other direction

**robot.stopTurning()**

stops the robot turning if you have called robot.startTurningLeft or robot.startTurningRight

Shooter Extension
-----------------
to extend your robot with the shooter extension use the command

    robot.extend(Shooter(shooter_motor_port))
    
the shooter extension gives your robot the shoot method called with the command

**robot.shoot()**
    
Light Extension
---------------
to extend your robot with the light extension use the command

    robot.extend(Light(light_port))
    
this extension will give your robot a load of new actions.

**robot.lightBlue()**
    
makes the robots' light blue
          
**robot.lightRed()**

makes the robots' light red

**robot.lightGreen()**

makes the robots' light green

**robot.lightAll()**

turns all the lights on
       
**robot.lightOff()**

turns all the lights off

Sonar Extension
---------------
to extend your robot with the sonar extension use the command

    robot.extend(Sonar(sonar_port))
    
the sonar extension gives your robot the howFar method called with the command

**robot.howFar()**
    
this will return a number from 0-255, telling you how far away the object the sonar sensor has detected is, if the sensor hasn't detected an object it will return 255