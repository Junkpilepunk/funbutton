# You Push one of 6 Buttons and each Button plays a (maybe) funny sound.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# Pin 1 - source for Signal (all pushbuttons parallel)
# Button1: Pin 11 (GPIO 17)
# Button2: Pin 13 (GPIO 27)
# Button1: Pin 15 (GPIO 22)
# Button1: Pin 16 (GPIO 23)
# Button1: Pin 18 (GPIO 24)
# Button1: Pin 22 (GPIO 25)
#
# To run the program properly, you have to put soundfiles
# named "1.wav" to "6.wav" in the programfolder.
# Feel free to change anything for your needs.

# Import
import RPi.GPIO as GPIO                                # for GPIO-Pins
import time                                            # for sleep()
import pygame                                          # to play the soundfiles
  
GPIO.setwarnings(False)                                # turn GPIO warnuings off
GPIO.setmode(GPIO.BCM)                                  # which GPIO-Layout you want to use  
 
# GPIO-Pins for input
GPIO.setup(17,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(23,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Init of Pygame.mixer
pygame.mixer.init(44100, -16, 1)

# mainloop 
while True:
    if GPIO.input(17)==1:
      #  print(1);
        pygame.mixer.music.load('/home/pi/python_programme/nippel/1.wav')
        pygame.mixer.music.play(1, 0.0)
        time.sleep(1)
    if GPIO.input(27)==1:
      #  print(2);
        pygame.mixer.music.load('/home/pi/python_programme/nippel/2.wav')
        pygame.mixer.music.play(1, 0.0)
        time.sleep(1)
    if GPIO.input(22)==1:
      #  print(3);
        pygame.mixer.music.load('/home/pi/python_programme/nippel/3.wav')
        pygame.mixer.music.play(1, 0.0)
        time.sleep(1)
    if GPIO.input(23)==1:
      #  print(4);
        pygame.mixer.music.load('/home/pi/python_programme/nippel/4.wav')
        pygame.mixer.music.play(1, 0.0)
        time.sleep(1)
    if GPIO.input(24)==1:
      #  print(5);
        pygame.mixer.music.load('/home/pi/python_programme/nippel/5.wav')
        pygame.mixer.music.play(1, 0.0)
        time.sleep(1)
    if GPIO.input(25)==1:
      #  print(6);
        pygame.mixer.music.load('/home/pi/python_programme/nippel/6.wav')
        pygame.mixer.music.play(1, 0.0)
        time.sleep(1)		
