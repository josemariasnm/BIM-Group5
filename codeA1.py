import ifcopenshell 
from blenderbim.bim.ifc import IfcStore
file=IfcStore.get_file()

spaces=file.by_type('IfcSpace')
beams=file.by_type("IfcBeam")
walls=file.by_type("IfcWall")
columns=file.by_type("IfcColumn")
slabs=file.by_type("IfcSlab")
storeys=file.by_type("IfcBuildingStorey")



spaces_in_model = len(file.by_type("IfcSpace"))
print("\nThere are "+str(spaces_in_model)+" spaces in the model")

    
    
beams_in_model = len(file.by_type("IfcBeam"))
print("\nThere are "+str(beams_in_model)+" beams in the model")


walls_in_model = len(file.by_type("IfcWall"))
print("\nThere are "+str(walls_in_model)+" walls in the model")

columns_in_model = len(file.by_type("IfcColumn"))
print("\nThere are "+str(columns_in_model)+" columns in the model")


slabs_in_model = len(file.by_type("IfcSlab"))
print("\nThere are "+str(slabs_in_model)+" slabs in the model")


storeys_in_model = len(file.by_type("IfcBuildingStorey"))
print("\nThere are "+str(storeys_in_model)+" storeys in the model")

for i in spaces:
    print(i.LongName)
     
#for i in beams:
    #for definition in beam.IsDefinedBy: #IsDefinedBy is the name of the beam column in the excel file#
        #if definition.is_a('IfcRelDefinesByProperties')
       # property_set=definition.RelatingPropertyDefinition
        
        
