import pandas as pd 
import tkinter as tk 
from tkinter import ttk 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
 
# Event dataset 
events = [ 
    {'name': 'Music Fest Highlights', 'category': 'NON-TECH', 'views': 203, 
'likes': 45}, 
    {'name': 'Photography Walk',      'category': 'NON-TECH', 'views': 160, 
'likes': 38}, 
    {'name': 'Dance Competition',     'category': 'NON-TECH', 'views': 150, 
'likes': 89}, 
    {'name': 'Art Exhibition',        'category': 'NON-TECH', 'views': 120, 
'likes': 67}, 
    {'name': 'Hackathon 2025',        'category': 'TECH',     'views': 95,  
'likes': 42}, 
    {'name': 'AI Workshop',           'category': 'TECH',     'views': 80,  
'likes': 35}, 
] 
 
# User profiles 
users = [ 
    {'initials': 'AK', 'name': 'Arjun K'}, 
    {'initials': 'SR', 'name': 'Sneha R'}, 
    {'initials': 'VS', 'name': 'Vikram S'},