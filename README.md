# FSD G1000 Enhancements

This is a collection of my own personal enhancements to the [FlightSimDiy](https://flightsimdiy.com/) G1000 module. https://discord.com/channels/769685829744197703/769689559499800589

It is a great design incorporating PCBs and well 3D printed files.

I have seen a lot of 95% finished designs with missing knobs, and I myself had trouble with the hole dia and length when using a 3rd party resin printing service, and after printing them myself using FDM.

To remedy this, I created my own parametric knobs. 
All designs are 100% my own, created from scratch, based on measurements taken from the FSD designs and the rotary encoders I have.

I will not ever produce STL files for these. The whole point is that even with a well callibrated printer, the tolerances for a good fitting knob are small, and the best way to ensure a good fit is to "print-test-adust-repeat"

## WARNING: Using these files requires knowledge of FreeCAD

* FreeCAD is unforgiving!
* I have provided tips here, but you will need to figure out how to do those things yourself. I would love to write a tutorial, but it takes time.

## FreeCAD Tips:

* The knurling pattern on the knobs makes FreeCAD insanely slow at re-rendering. I strongly suggest you turn on "Skip Recomputes" on the document, and recompute manually
* Size adjustments are done by modifying the FreeCAD spreadsheet values and "recomputing" the body
* To create an STL file, you will first need to create a mesh from the solid body, then export the mesh as an STL

## 3D Printing Tips

* Callibrate your printer... in particular the flow rate / extrusion rate. My Ender 3 S1 Pro needed 94% flow rate, and this improved hole sizing a lot
* Use a 0.2mm nozzle for a nicer result
* Use a small layer height
* Print on a RAFT... this prevents the elephants foot effect and massively reduces the amount of deburring you will need to do to make the buttons fit

## My ToDo

* Create a tutorial
* Test using FreeCAD's Lattice2 Workbench for the knurling... to see if performance is improved
