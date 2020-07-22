read in file at CLI, #sDeck file.k
parse file name decide if .k or .bdf then send to repective parser
Focusing only on GRID/NODE and simple elements parse in files 
convert (idk how yet)
write to other file type

The deck class is for an entire file
it contains nodes and and eleObject and a type flag
this eleObject has attributes for each type of NASTRA element and for dyna elements
these attributes contain item objects
