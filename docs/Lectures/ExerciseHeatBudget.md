---
layout: default
title: Exercise - Budgets
---

## Heat budget of the surface mixed layer

  1. What is the specific heat capacity of water?
  2. Sketch what the temperature profile below would look like if it
lost enough heat so that it was a uniform temperature to 100 m?

![Time Series at HOTS](../../figs/HotsTsm.jpg)

  3. How much heat would have to be lost from the surface of the ocean
     for this to happen? Estimate from the temperature profile and
     show how you calculated this.   
  4. What is the average heat flux this heat loss would represent if
     it occured over 6 months, in W/m^2.  Based on the plots in the
     reading is this a reasonable net surface heat flux?

##  Interpret the evolution of the surface mixed layer

Based on the following plot, try and answer the following questions:

![From Emery et. al. 2007](../../figs/MixedLayerPapaSm.png)

***Q*** Why does the mixed layer deepen in the winter?  

***Q*** Why does it shoal in the spring and summer?  

***Q*** Why do you think there is often a spring bloom at Station Papa?  Why
does it stop?   

## Diffusive fluxes...

The geometry and units of fluxes are a bit difficult to get clear, so
lets practice them here.  Consider the following table of data points:

Depth [m]  |    Concentration Sulfur [$g\,m^{-3}$]
 5 | 2
15 | 3
25 | 6
35 | 6
45 | 4
55 | 2

***Q*** Sketch the *profile* of Sulfur with depth.

***Q*** Doing this sort of thing abstractly becomes hard.  Lets assume this
profile was collected in a column of water that is 65-m high, 1 meter
wide and 1 meter deep.  Divide the column into 10 x 1 x 1 m^3 blocks
centered on our measurements.  Approximately, how many grams of Sulfur
are there in each of the 6 blocks?

***Q*** *Approximate* the gradient of Sulfur concentration at each the
boundaries of each of the boxes (i.e. 10 m, 20 m, etc..).   

***Q*** If the turbulent diffusivity is $K=10^{-3}\ \mathrm{m^2\,s^{-1}}$
what is the diffusive *transport* across each of the block
faces?  Make sure you get the direction correct.  Report your result
in grams/second.  

***Q*** Consider any one block.  You now should know the value and direction
of flux (in $g/s$) across the upper and lower face, and you should know
the total grams inside the block.  If you assume the flux remains constant
for 1000 s, how many grams of Sulfur are in your cell after 1000 s?

***Q*** Repeat for all 6 cells (hint, use a computer!) and plot the new
sulfur profile after a 1000 s.  

***Q*** repeat the procedure 9 more times to get the gradient after 10000 s;
(Hint: *really* use a computer;).  Plot the sulfur profile at each timestep.

***Q*** Do the changes of the profile correspond to your intuition of
how diffusion works?  
