#!/usr/bin/python3 
import sys 
sys.path.insert(0,"/var/www/Visualizer/") 
sys.path.insert(0,"/var/www/Visualizer/Visualizer/") 
 
import logging
logging.basicConfig(stream=sys.stderr) 
 
from Visualizer import app as application
