# ThermalSatReport
I got a new toy. A thermal receipt printer! Sure, I could have it spit out a shopping list or crank out a sheet every time a Tweet comes through from various people. But let's have it present me with a list of amateur radio satellite passes for a 24 hour period so I can plan which birds to wave my Yagi around at.

Please read the comments inside the Python code to see where to add the bits you'll need to supply - some API keys and other info specific to your printer (IP address and whatnot). I'm just a hobbiest but I tried to make this easy for someone else to follow or to use as a basis for another project.

This make use of the Python-Escpos Library for using Python with thermal printers. You can find the documentation here: https://python-escpos.readthedocs.io/en/latest/

My printer is a POLONO PL330 Thermal Receipt Printer and can handle ip, serial, or USB connections to it. 

I have a item listed in the Windows Task Scheduler to run at midnight to run the .py script and spit out the paper. 

The image included should be changed unless you're a neigbor I don't know about in FN10 :) Feel free to use the image as a template for size comparison.

<img src="https://i.imgur.com/Lmk4HSe.jpg" width=30%>
