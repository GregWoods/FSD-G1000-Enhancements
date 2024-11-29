# Run using Powershell with the call operator '&'
# and pass in the path to the FCStd file as the first command line argument.
# & "C:\Program Files\FreeCAD 1.0\bin\freecadcmd.exe" .\export_stl.py  G1000_inner_knob_std.FCStd
#
# Run using Ubuntu (example path to FreeCAD uses WSL on Windows)
# "/mnt/c/Program Files/FreeCAD 1.0/bin/freecadcmd.exe" export_stl.py  G1000_inner_knob_std.FCStd

import sys
import FreeCAD 
import Part 
import Mesh
import os

# Accept a command line argument for the FCStd file path
if len(sys.argv) < 3:
    print("Please provide the path to the FCStd file as a command line argument.")
    sys.exit(1)

fcstd_file_path = sys.argv[2]
print("FCStd file path:", fcstd_file_path)

# Split the file path into directory and filename
file_dir, file_name = os.path.split(fcstd_file_path)

# Split the filename into name and extension
file_name_without_ext, file_ext = os.path.splitext(file_name)

# Print the directory, filename without extension, and extension
print("Directory:", file_dir)
print("Filename without extension:", file_name_without_ext)
print("Extension:", file_ext)

# Load your FreeCAD document
doc = FreeCAD.open(fcstd_file_path)

# Access the solid body
# Get the last object in the document 
last_object = doc.Objects[-1] 

print("Last object Name:", last_object.Name)
print("Last object TypeId:", last_object.TypeId)

# Create a mesh object from the solid body
mesh_object = Mesh.Mesh(Part.getShape(last_object).tessellate(1))

# Add the mesh to the document
mesh = doc.addObject("Mesh::Feature", "Mesh")
mesh.Mesh = mesh_object

# Export the mesh as an STL file
export_path = os.path.join(file_dir, file_name_without_ext + ".stl")
Mesh.export([mesh], export_path)
