# Whatsapp-Tracker
 This is a python script that tracks the online status of an user.
 
## Pre-requisites
 Refer to the requirements.md file for installing the required python packages.
 [Link to Python package requirements file to run the code](requirements.md)

## Using the script
 To use the script, first create a new channel on notify.run
 
 Alternately, run (in a Jupyter Notebook):
 
         from notify_run import Notify
         notify = Notify()
         notify.register()
      
 Then enter the URL of the channel as the endpoint attribute in the python script.
 
 Also, scan the QR code provided to you by notify.run on the device you intend to be notified on and hit 'Subscribe on this Device'
 
 Make  sure that notifications have been enabled for the browser that you use to subscribe.
 
 The script is now good to go!
