---
layout: page
title: Course Project
order: 3
---

# Goal

The goal of the course project is for you to organize and prepare a
report and preliminary analysis for the physical oceanographic data
collected in Saanich Inlet.  The emphasis will be on presenting the
data and a rough qualitative and quantitative (where possible)
analysis.

![Booo](/figs/bow.jpg)

# Background Reading

  - [Gargett et al 2003](/Readings/GargettEtAl03.pdf)
  - [Manning et al 2010](/Readings/ManningEtAl10.pdf)

# Saanich Inlet Data Analysis

The project is to write a short cruise report detailing the
observations made in Saanich Inlet.  You will organize the data and
make plots of the results.  Some comparison with previous data is
required.  Any interpretation of the results will be welcome.   

## Getting data...

The data will be in a database at:

<http://web.uvic.ca/~sarahjt/OSM/OSMCruiseData/>


### `ctd` :
   - Individual CTD casts are named by station "`S4`, `S5`..."
  - A 1-m vertical grid of the CTD casts: `CtdGrid.mat`
  - The variables should be self explanatory. One exception is `cgrid.alongx`, which is an along-inlet co-ordinate system that is useful if you want to plot x,z,T plots (for instance).  This has varied a bit over the years, and for 2016 is the distance from the head of the inlet.  Other years it has been distance from S4.  Sorry for the confusion, but distance from S4 is not a very good co-ordinate system if you don't always do the same line.  To correct, you need to find the cast with `S4` data in it and subtract its value of `cgrid.alongx` from the rest to compare with other years.  

### `BPS`:
   - This year we have Buoyed Profiler System data from Ocean Networks Canada.  There is a map at <http://www.oceannetworks.ca/installations/observatories/salish-sea/saanich-inlet> showing its location.  The CTD and Oxygen data from this profiler is collected usually 4 times a day, though there are data gaps.  I have binned these into 1-day bins and interpolated over most gaps to give a nice time series.  How does this data fit into your observations of the along-channel sections?  
  - <http://dmas.uvic.ca/DataSearch?location=YPVP>
  - [Slides about BPS Courtesy D. Riddell, ONC](/Readings/EOS311_Nov2016.pdf)

## Introduction

Write a brief introduction to your report. State the objectives of the
cruises and what scientific questions they were designed to answer.  

## Methods and Site

Describe what vessel was used and what instrumentation was aboard.  Be
as specific as possible, including model numbers and any specifying
information.  Processing methods should be described at this point:
i.e. if you bin the CTD data onto 1-m depth bins, this would be the
place to mention it.

Also describe where the cruise went.  This will be done with a cruise
track over a plot of bathymetry.  Include an indication of when and
the ship was at different positions.  The Inlet location should be
indicated on a larger regional map as well.  Below you are asked to
compare with previous seasons and other years.  Indicate which
station(s) you are using to make this comparison.  

### Tides

Load bottom pressure data from VENUS for a month centered around the
cruise.  Also upload tidal predictions from IOS.  Indicate where our
cruise was.  How well did the tidal prediction do?  What are the
differences and similarities?

Indicate where the data collection falls in the tidal phase and spring-neap cycle.  

### Local Weather

What was the weather like that day?  At least mention. Ask your
classmates for the weather on their leg.  Or, download the met data
from

<http://web.uvic.ca/~sarahjt/OSM/OSMCruiseData/RegionalData/>


## Observations

The overall goal here is to compare our new data and put in context with different timescales in the Inlet.  

### Multi-year comparison

UVic visits Saanich Inlet almost every year in July since 2007.  A fun comparison is to look at the data from station S4 and/or S5 for those years and see if there are any changes.  Particularly focus on the deep water as the surface water is quite variable.  Are there any years that are anomolous in any of the properties, and are there reasonable explanations for this?


### Seasonal comparison

Similarly, we visit at different times of year.  Is the inlet different in Jan, June, and July?   Again, be careful about focusing on the near-surface data.  The BPS data (see above) was collected from Jan until now, and can give the best picture of the inlet's state over most of the year.  How representative were the CTD casts collected at other times of year?  Did they happen to catch an interesting event?  What "events" can you see in the BPS data?  Again, I suggest you strongly focus on the deeper water, though the upper water is interesting as well.


### Cruise CTD Section

We ran from the Haro Strait to Saanich Inlet in `201407`, `201509a`, `201510`, `201609a`, `201609b`, and `201610`.  Plot the sections, preferably in space.  Make sure to indicate salinity, temperature, O2, and fluorescence (the radiometer is less useful), and from that density.  How and where do the water masses change in Satellite Channel?  Preference would be to focus on 2016 data, but you are free to look at the previous cruises as well to compare and contrast.

### General presentation hints:

You may also want to look at the O2 data.  You'll likely cover this in
your other classes, but while you have the plotting routines made it
is pretty easy to go through and make another set of plots.  

For the CTD data, `pcolor` and `contour` are sometimes good.  It is also
sometimes more helpful to simply `plot` vertical profiles. i.e. to
compare July 2007 to July 2014 it might be most effective to plot
profiles of T at S4 in 2007 and J1 in 2010 on the same plot, but
colour them uniquely.  Similarly with S.  

A very useful technique for
determining water masses is a plot of T on the y-axis, versus S on the
x-axis.  You can do the same with O2 versus T or S (Flu isn't as interesting).  

Be judicious in your plots and comparisons.  We don't need to see
all the data in each report.  Tell a story with the data.

Make sure your colormaps and axes limits are meaningful.  The surface water varies a lot.  If you want to talk about that, that is great, but be prepared to make another plot that zooms in on the deeper water that doesn't have as much variation.  

## Summary and discussion

Summarize the findings.  How did the observations conform to your
expectations and what surprises did you find?  How did they agree with
previous measurements published by other authors (briefly!). Feel free
to speculate on what mechanisms are causing the observations you are
seeing.  This section may be a few subsections where interesting
tidbits from your analysis above are discussed in more detail, perhaps
with a speculative air.

# Format

You will each prepare a separate report.  You may use the software
package of your choice, but be sure to hand in a **PDF** of your final
report.

All sections should be identified with clear headings, in bold.  

I don't require a bibliography, but if you prepare one put it at the
end.  Make sure to use an Author/Year citation style in the text
i.e. "Gargett et al. (2003) found that deep water renewal into the
inlet was episodic...."

Figures are the heart of this report.  They should all be legible.
Each should have a caption including a figure number.  Most software
packages have ways of keeping automatic counters of figure numbers.
In the main text, reference should be made to figure numbers.

Figures *must* include axes labels, legends, and colorbars.  Text
annotations on the figures are sometimes useful.  

## Grading:

The goal is to present the data as clearly as possible.  This requires
figures, figure captions, and some prose.  The grading is as follows:

  - Prose (out of 11)
    - Introduction
    - Description of the experiment
    - Explain the data in the figures
    - Compares the data sets
    - Attempts to explain relevant physical processes
    - Refers to published literature if relevant.  
  - Figures (out of 14)
    - Clear, properly labeled
    - Clear and concise captions
    - Explain the data efficiently
