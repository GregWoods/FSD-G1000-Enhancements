# FSD G1000 Enhancements

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



