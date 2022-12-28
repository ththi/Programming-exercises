# Habit tracker
This repository contains files that are part of the habit tracker app. You can find four files:

- loop.py : This is the main script for the habit tracker. You need only to run this file in order to use the tracker.

- func_mod.py : This file contains the analytics functions used in the main file. This file need to be in the same folder as the loop.py file.

- streak_test.py : This file is a unit-test file, testing the functionality of one of the functions from the respective file.

- track_data.csv : This file contains randomly generated habit tracking data for five habits, spanning four weeks. This file need to be in the same folder as the loop.py file, when you want to use it. It will be automatically used if its there, otherwise five predefined habits will be available, but without any tracking data. To explore all functions of the script, i recommend to use this file.

In order to start the script from commandline you need (of course a functional python environment) just navigate to the folder where all scripts are located and type *python loop.py* . The script will start and guide you throught its functions (everything commandline based).
