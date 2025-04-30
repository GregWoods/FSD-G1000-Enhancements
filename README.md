# FSD G1000 Enhancements

This is a collection of my own personal enhancements to the [FlightSimDiy](https://flightsimdiy.com/) G1000 module. https://discord.com/channels/769685829744197703/769689559499800589

It is a great design incorporating PCBs and well 3D printed files.

I have seen a lot of 95% finished designs with missing knobs, and I myself had trouble with the hole dia and length when using a 3rd party resin printing service, and after printing them myself using FDM.

To remedy this, I created my own parametric knobs. 
All designs are 100% my own, created from scratch, based on measurements taken from the FSD designs and the rotary encoders I have.


## WARNING: Using these files requires knowledge of FreeCAD

* FreeCAD is unforgiving!
* I have provided tips here, but you will need to figure out how to do those things yourself. I would love to write a tutorial, but it takes time.

## FreeCAD Tips:

* The knurling pattern on the knobs makes FreeCAD insanely slow at re-rendering. I strongly suggest you turn on "Skip Recomputes" on the document, and recompute manually
* Size adjustments are done by modifying the FreeCAD spreadsheet values and "recomputing" the body
* To create an STL file, you will first need to create a mesh from the solid body, then export the mesh as an STL

## 3D Printing Tips

* Callibrate your printer... in particular the flow rate / extrusion rate. My Ender 3 S1 Pro needed 94% flow rate, and this improved hole sizing a lot.
* [Revised Advice] Use the slicer's Hole Enlargement setting wth the supplied STL files instead of messing with FreeCAD
* Use a 0.2mm nozzle for a nicer result - as long as it doesn't clog
* Use a small layer height
* [IMPORTANT] Print on a RAFT - aprticularly for the knobs... this prevents the elephants foot effect and massively reduces the amount of deburring you will need to do to make the knobs fit

## My ToDo

* Create a tutorial
* Test using FreeCAD's Lattice2 Workbench for the knurling... to see if performance is improved

## Notes on the Fit of the Knobs

When printed on a Ender 3 S1 Pro with Elegoo filament.

Originally I was adjusting the holes in the parametric model, but due to FreeCad being mind-numbingly slow when using Multitransform for the knurling, I have instead experimented with setting the hole to the exact size of the shaft, and adjust the fit with the slicers Hole Enlargement setting. 

My advice is to print these one at a time, noting carefully the settings used to get the perfect fit.

### Common Settings

* No supports
* Raft, with air gap equal to layer height
* Nozzle size 0.4mm (I kept clogging my 0.2 nozzles)

### Holes Sizes and Hole Compensation Setting

| Model         | Actual Shaft Dia | Parametric Hole Dia | Printer Settings           | Fit Notes                           |
| :------------ | ---------------: | ------------------: | :------------------------- | :---------------------------------- |
| inner_knob    |           3.50mm |              3.63mm | 0.0mm Hole Enlargement     | Tight fit. but no trimming required |
| inner_knob    |           3.50mm |              3.50mm | 0.13mm Hole Enlargement    | Good fit, not as tight as above     |
| inner_knob    |           3.50mm |              3.50mm | 0.12mm Hole Enlargement    | Same as above                       |
| single_navcom |           5.95mm |              6.16mm | 0.0mm Hole Enlargement     | Good fit, but differnt filament, & unknown print settings |
| single_navcom |           5.95mm |              5.95mm | 0.2mm Hole Enlargement     | An initial "snap" moment, then too big  |
| single_navcom |           5.95mm |              5.95mm | 0.12mm Hole Enlargement    | Good fit. Needed a little trimming (missing chamfer)      |
| inner_tri     |           3.50mm |              3.60mm | 0.00mm Hole Enlargement    | Good fit, but differnt filament, & unknown print settings |
| inner_tri     |           3.50mm |              3.50mm | 0.12mm Hole Enlargement    | Awaiting result       |
|      |             |                | 0.0mm Hole Enlargement |   |
|      |             |                | 0.0mm Hole Enlargement |   |
|      |             |                | 0.0mm Hole Enlargement |   |




