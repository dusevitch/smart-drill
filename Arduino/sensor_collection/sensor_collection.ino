#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
unsigned long clocktime;

Adafruit_BNO055 bno = Adafruit_BNO055(55);

void setup(void) 
{
  Serial.begin(115200);
  Serial.println("Orientation Sensor Test"); Serial.println("");
  
  /* Initialise the sensor */
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  
  delay(10);
    
  bno.setExtCrystalUse(true);
}

void loop(void) 
{
  clocktime=millis();
  imu::Vector<3> accel = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  imu::Vector<3> lin_accel = bno.getVector(Adafruit_BNO055::VECTOR_LINEARACCEL);
  imu::Vector<3> magnetometer = bno.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER);
  /* Display the floating point data from Accelerometer (m/x^2)*/
  Serial.print("TIME: ");
  Serial.print(clocktime);
  Serial.print(" X: ");
  Serial.print(accel.x());
  Serial.print(" Y: ");
  Serial.print(accel.y());
  Serial.print(" Z: ");
  Serial.print(accel.z());
    /* Display the floating point data from Linear Accelerometer (m/x^2)*/
  Serial.print(" X: ");
  Serial.print(lin_accel.x());
  Serial.print(" Y: ");
  Serial.print(lin_accel.y());
  Serial.print(" Z: ");
  Serial.print(lin_accel.z());
//    /* Display the floating point data from magnetometer (uT)*/
//  Serial.print(" X: ");
//  Serial.print(magnetometer.x());
//  Serial.print(" Y: ");
//  Serial.print(magnetometer.y());
//  Serial.print(" Z: ");
//  Serial.print(magnetometer.z());
  Serial.println("");
  delay(2);
}
