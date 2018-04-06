---
layout: post
title: Digital Graffiti
categories: research
---

As a Systems Engineering course project, teams of 3 CMU engineering graduate students designed exhibits for the [Pittsburgh Children’s Museum](http://www.pittsburghkids.org/). My group designed a “Digital Graffiti” wall, which tracks plastic ball collisions with a white wall using a Microsoft Kinect and simulates the resulting paint splatter on the wall using a projector and speakers.

![Digital Graffiti at the Children's Museum of Pittsburgh]({{ "/assets/24217-1303425281-5-l.jpg" | absolute_url }})
Image courtesy of [lrippel](http://www.photoblog.com/lrippel/2011/04/21/).

The wall “resets” every 60 seconds, saving the images to our website so kids can retrieve their art when they get home. Check the website for more details and, in a few weeks, source code! In the meantime, to install the drivers we used in this project, check this post.

Below is a short video of the exhibit at the Children's Museum of Pittsburgh.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/zLPFMEKUUI4?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

As you can see, the exhibit has two operating modes: paint phase and cleanup phase. During the paint phase, kids would throw balls at the wall and watch and listen to the results. During the cleanup phase, kids would (sometimes) collect the balls to refill the bins while music played. For this project, we used audio created by the artist [Waterflame](http://www.myspace.com/waterflamelegit). Some kids continued throwing balls against the wall during this phase and others (especially the toddlers) would begin dancing. The exhibit was very popular and had nearly zero idle time during the 3 days it was present at the museum. When school field trip groups came through, the system had as many as 16 simultaneous users yelling, screaming, throwing balls, blocking throws, rolling around and causing general (but expected) chaos.

A unique shape-color-number pattern was generated at the end of each phase, which kids could use to retrieve their image from the project website.

The main bottlenecks in the system right now are:
* The 30 FPS poll rate of the Kinect – balls thrown too fast do not register. An absorbent material attached to the wall would help mitigate this problem.
* Timing issues between the color and depth camera – balls thrown at extreme angles have a location mismatch between the color and depth images when using factory calibration transformations. I think this is caused by a small delay between the camera polling.
* The high reflectivity of the plastic balls, complicating proper color identification. Foam balls were investigated but did not weigh enough for proper throwing. Colorspace shifting and further investigation into foam ball vendors and methods of adding weight are possible solutions to this problem.

In other news, we were approached by a company designing exhibits for the Science Museum of Beersheba. They were interested in setting up the exhibit and we were able to get it set up and configured remotely. Their integration looks much more slick!

<iframe width="560" height="315" src="https://www.youtube.com/embed/ga_2CcbONLo?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

This was a great project and I’m glad to finally have proper Kinect drivers set up! For more information about the project, including setting up your own Digital Graffiti wall, check out the [Digital Graffiti Homepage](https://sites.google.com/site/pitdigitalgraffiti).
