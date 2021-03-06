---
layout: default
title: Heat and Salt Budgets, and Quantifying Mixing
---

# Reading
  - OU Sec 6.1--6.3
  - [Mixing.pdf](../../Readings/Mixing.pdf)

      ![Oceanic surface heat fluxes with inferred heat transports indicated with arrows](../../figs/NetHeatTrans.jpg)

# Things to learn

## Heat Budget
  - Why on the whole does the surface of the ocean receive less
    insolation than the land?
<!-- albedo, more clouds) -->
  - What are the terms in the heat equation?
<!--
[//]: # insolation: shortwave sun.
[//]: # back reflection: long wave emmisivity.
[//]: # sensible heat loss: diffusion of heat from warm to cold[//]: #
[//]: # evaporative heat loss  -->
  - What are their approximate relative magnitudes?
<!-- [//]: # 100:45:10:45 (roughly)...
-->
  - How do you estimate each?
<!-- [//]: # insolation: can measure from sensors -->
<!-- [//]: # back radiation: same sensors turned upside down.  But very -->
<!-- [//]: # inhomogenous. -->
<!-- [//]: # sensible heat loss: temperature difference, but alos depends a lot -->
<!-- [//]: # on wind speed and boundary layers -->
<!-- [//]: # evaporative: humidity, temperature difference, also wind speeds and -->
<!-- [//]: # BL turbulences. -->
  - Which terms are the most difficult to parameterize and what
    physics makes them difficult?
<!-- [//]: # sensible and evaporative are hard -->
  - Try to understand the patterns to Q_h and Q_e in Figs 6.7 and 6.8.  
<!-- [//]: # western heat losses are due to warm water being brought in from S in -->
<!-- [//]: # Gulf Stream and Kuroshio. Also dry cold air from continents -->
  - Why is the heat flux markedly different between the N and S
    hemispheres?  
<!-- [//]: # Dry cold air from continents! -->
  - If no latitude is to change temperature too drastically, what
    direction must heat flow according to figure 6.9c (average the two
    curves by eye to get an estimate of mean heat flux for the year)?
<!-- [//]: # From equator to approx 30 N/30 S -->

<!-- [//]: #  - How is this different than the answer in the Atlantic (Fig 5.12)? (note: we'll see later that the Atlantic is relatively special in terms of its circulation) -->
<!-- [//]: # Atlantic has net flow to the N at all latitudes. -->

## Conservation of Salt
  - What is the difference between saying that salt in the ocean is
    conserved and saying that it is constant?
  - What units is salinity usually expressed in?  What is the physical
    meaning of these units?
  - What factors change salinity?
  - How does the derivation of eqs 6.5 compare to the Knudsen
    Relation we looked at in the previous class?
  - What is the "residence time"?
  - From Fig 6.11, where is precipitation high?
<!-- [//]: # high: sub-polar regions, equator (ITZC)  -->
  - From Fig 6.11, which ocean might you expect is the freshest?
<!-- [//]: # Expect Pacific to be the freshest. -->
  - Why is there an east/west asymmetry to E-P in the ocean basins?
<!-- [//]: # Upwelling makes water colder, and thus less likely to evaporate. -->
<!-- [//]: # Currents carry water on the western boundaries.  More evaporation in -->
<!-- [//]: # the east because the trades blow from east to west at these -->
<!-- [//]: # latitudes and have not had as much time to become humid.   -->


## Mixing:
  From [Mixing.pdf](../../Readings/Mixing.pdf)

  - For salt, we've already talked about advection (what comes in, must go out), and evaporation and precipitation (QS).  What extra term can change the salinity at any given location?  
<!-- [//]: # mixing! -->
  - How do we quantify the diffusive flux and transport?  
<!-- [//]: # flux is -k dC/dx in x direction. -->
  - If water is salty on the bottom of a tank, and fresh near the top, what direction will the diffusive flux of salt be?
<!-- [//]: # from salty to fresh   -->
  - What is the difference between molecular diffusion and turbulent diffusion?  
<!-- [//]: # turbulent is like stirring a cup of coffee. -->
  - What is the approximate time scale to mix a 0.2 m tall beaker of salt-stratified water if the turbulent diffusivity is $ 10^{-4}\ m^2s^{-1} $ instead of the molecular diffusivity of $ 10^{-9}\ m^2s^{-1}$?
<!--[//]: # about 1 hour   -->


# Exercise:
[ExerciseHeatBudget](../ExerciseHeatBudget)

<!--- <comment>

## In class Exercise:  

If the heat-flux into the ocean looks like a cos-wave between the
Equator and the north pole, what must the advective heat flux be at
the equator, pole, and at 45 N?  Sketch the advective heat flux
between these points.


## Concepts:
  - parameterization of subgridscale
  -
</comment>
--->
