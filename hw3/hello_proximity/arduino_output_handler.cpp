/* Copyright 2019 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#include "output_handler.h"

#include "Arduino.h"
#include "constants.h"
#include <Arduino_APDS9960.h>

// The pin of the Arduino's built-in LED
int led = LED_BUILTIN;

// Track whether the function has run at least once
bool initialized = false;

// Animates a dot across the screen to represent the current x and y values
void HandleOutput(tflite::ErrorReporter* error_reporter, float x_value,
                  float y_value) {
  // Do this only once
  if (!initialized) {
    // Set the LED pin to output
    pinMode(led, OUTPUT);
    initialized = true;
  }

  // Calculate the brightness of the LED such that y=-1 is fully off
  // and y=1 is fully on. The LED's brightness can range from 0-255.
  int brightness = (int)(127.5f * (y_value + 1));

  // check if a proximity reading is available
  if (APDS.proximityAvailable()) {
    // read the proximity
    // - 0   => close
    // - 255 => far
    // - -1  => error
    int proximity = APDS.readProximity();
    
    if (proximity < 200) {
      // 200 is around 4 inches from the board based on testing with a ruler
      // if within 200 proximity, write to LED as a constant keeping it lit
      // Write to serial monitor if hand is near
      brightness = 250;
      analogWrite(led, brightness);
      Serial.print("---Detected---\n");
    } else {
      // Set the brightness of the LED. If the specified pin does not support PWM,
      // this will result in the LED being on when y > 127, off otherwise.
      analogWrite(led, brightness);
      Serial.print("---Not Detected---\n");
    }
    
    // print proximity value to the Serial Monitor
    Serial.print(proximity);
    Serial.println("\tBoard Proximity\n");

    // print local analogWrite brightness to Serial Monitor
    Serial.print(brightness);
    Serial.println("\tWrite Brightness\n");
  }
  
  // Log the current brightness value for display in the Arduino plotter
  TF_LITE_REPORT_ERROR(error_reporter, "%d\n", brightness);
}
