---
layout: post
title: OpenNI Kinect drivers for Windows
categories: research
---

When I got my Kinect back in December, after several failed attempts with ROS cturtle and OpenNI drivers I gave up and began using the Windows CLNUI drivers and libfreenect Ubuntu drivers. Recently, with the help of a very good friend, I have finally migrated from using the [CLNUI Kinect drivers]({{ "/assets/kinect-drivers.zip" | absolute_url }}) to the OpenNI Windows drivers, which have easy-to-use access to the internal calibration matrix of between the RGB and depth cameras. This zip file includes a README in the base directory which should tell you the basics of getting it set up, along with the necessary files and an example cpp file. This is basically the same process as listed at [www.codeproject.com](http://www.codeproject.com/Articles/148251/How-to-Successfully-Install-Kinect-on-Windows-Open.aspx) except that as of Monday the stable versions of each requisite library would not play nicely with each other (yeah, nothing new there!). So these are much older drivers (sadly, no audio drivers). If you have a set of more up to date drivers that work, please let me know!

A few interesting things I found
* Installing in a place other than the default directory may mess it up (or I’m just missing a library import setting somewhere).
* Windows 7 has some power saving features which may cause the drivers to fail within minutes of usage on some laptops. I have a Lenovo x200 and my RGB feed would quickly desynchronize/jitter and cause the drivers to crash immediately afterwards.

To fix that I had to do the following
1. Plug in the Kinect
2. Open Device Manager
3. Go through USB Root Hubs and look at Power tab for Kinect (labelled as “Generic USB Hub (3 ports)”)
4. In the USB Root Hub’s Power Management tab, uncheck “Allow computer to turn off this device to save power”

I’ll post why I got the drivers working in a few days. Enjoy!
