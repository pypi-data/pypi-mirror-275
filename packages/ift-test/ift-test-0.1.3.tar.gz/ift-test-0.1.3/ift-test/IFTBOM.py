# nx: threaded

import json
import os
import NXOpen
import NXOpen.CAM
import NXOpen.UF
from IFT.IFTBase import IFTCore
print_nx = IFTCore.print_nx
nx_logger = IFTCore.nx_logger 

class IFTBOM: 
    """
    This class refers to the object of the BoM (Bills of Material, in german Stueckliste)
    The BOM has a dictionary structure (IFTBOM.bom) that contains the hierarchy of the occurring
    parts in the CAM setup.

    Parts are physically stored 3D geometries and components are just pointing to the part objects.
    For instance can a part occur several times in a BOM. The part is always the same, but the 
    component has different positions.

    Attributes
    ----------
    component_list : list
        List of components
    fixture_components : list
        List of components declared as fixture parts
    part_list : list
        List of parts 
    bom_dict : dict
        dictionary containing the structure and attributes of the BOM

    Methods
    -------
    get_component_list(self, component=None, component_list=[])
        Adds all NXOpen.Assemblies.Component instances to the component_list
    get_part_list(self, component=None, part_list=[])
        Adds all NXOpen.Part instances to the part_list
    get_data_attributes(self)
        Gets the data of the BOM
    get_fixture_components(self)
        Adds all NXOpen.Part-JournalIdentifiers of parts that are fixture parts to the fixture_component_list
    """
    def __init__(self):
        self.component_list = None  # list of components 
        self.fixture_components = None # list of fixture components
        self.part_list = None
        self.bom_dict = {}

    def get_component_list(self, component = None, component_list = []):
        """
        Description: This function returns a list of all NXOpen.Assemblies.Component instances that are part of 
        the assembly in the openend CAM setup. 

        Don't change the optional arguments. They are to initialize the variables in thte first loop, as this is 
        recursive function.

        Sets:
        - component_list:list
        """
        if not component: 
            component = NXOpen.Session.GetSession().Parts.Work.ComponentAssembly.RootComponent
        children = component.GetChildren() # all the children in a lower hirarchy
        for child in children:
            if child.GetChildren():  # child is sub-assembly
                self.get_component_list(child, component_list)
            else:  # child is part
                if child not in component_list:
                    component_list.append(child)                   
        self.component_list = component_list

    def get_part_list(self, component = None, part_list = []):
        """
        Description: This function returns a list of all NXOpen.Part instances that are part of 
        the assembly in the openend CAM setup. 

        Don't change the optional arguments. They are to initialize the variables in thte first loop, as this is 
        recursive function.

        Sets:
        - part_list:list
        """
        if not component: 
            component = NXOpen.Session.GetSession().Parts.Work.ComponentAssembly.RootComponent
        children = component.GetChildren() # all the children in a lower hirarchy
        for child in children:
            if child.GetChildren():  # child is sub-assembly
                self.get_part_list(child, part_list)
            else:  # child is part
                if child.IsOccurrence:
                    part = child.Prototype
                    if part.Bodies:
                        if part not in part_list:
                            part_list.append(part)                   
        self.part_list = part_list
    
    def get_data_attributes(self):
        """
        Generates the BOM in a hierarchical form as a dictionary.

        Sets:
        - self.bom:dict
        """
        if not self.fixture_components: # get list of fixture components if not available
            self.get_fixture_components()
        self.bom = self.get_bom_dict()

    def get_fixture_components(self):
        """
        Gets a list of components defined as fixture parts in the CAM setup.

        Sets:
        - self.fixture_parts:list
        """
        component_list = list()
        nx_session = NXOpen.Session.GetSession()
        workpart = nx_session.Parts.Work
        setup = workpart.KinematicConfigurator.ComponentCollection.FindObject("SETUP")
        try:
            fixtures = workpart.KinematicConfigurator.ComponentCollection.FindObject("FIXTURES")
        except:
            fixtures = workpart.KinematicConfigurator.ComponentCollection.FindObject("FIXTURE")
    
        kinematic_builder = workpart.KinematicConfigurator.ComponentCollection.CreateComponentBuilder(setup,fixtures)
        fixture_components = kinematic_builder.GetGeometries()
        for component in fixture_components:
            if component.IsOccurrence:      
                object = component.Prototype
                if isinstance(object, NXOpen.Part):
                    part_id = object.JournalIdentifier
                elif isinstance(object, NXOpen.Body):
                    part_id = object.OwningPart.JournalIdentifier
                
                if part_id not in component_list:
                    component_list.append(part_id)
        self.fixture_components = component_list 
                
    def get_bom_dict(self, component = None):
        """
        Creates a BOM (Bill of Materials) with additional information in a dictionary structure.

        Input:
        - component:NXOpen.Assemblies.Component

        Returns:
        - bom_dict:dict
        """
        if not component:
            component = NXOpen.Session.GetSession().Parts.Work.ComponentAssembly.RootComponent
            bom_dict = {"parts": []}
        else:
            bom_dict = {"parts": []}
        children = component.GetChildren()
        for child in children:
            child_dict = {"name": child.JournalIdentifier}
            if child.GetChildren():
                if not child.IsSuppressed:
                    child_dict["type"] = "assembly"
                    child_dict["parts"] = self.get_bom_dict(child)["parts"]
            else:
                if not child.IsSuppressed:
                    child_dict["type"] = "part"
                    position, rotation = IFTPart.get_position(child)
                    child_dict["position"] = position
                    child_dict["rotation"] = rotation
                    child_dict["material"] = IFTPart.get_material(child)
                    child_dict["STL"] = os.path.join(IFTCore.storage_dir,"STL", f"{child.JournalIdentifier}.stl" )
                    if child_dict["material"]:
                        child_dict["mass"] = IFTPart.get_mass(child)
                    else:
                        child_dict["mass"] = None
                    if child.Prototype.JournalIdentifier in self.fixture_components:
                        child_dict["isFixturePart"] = True 
                    else:
                        child_dict["isFixturePart"] = False 
            
            if not child.IsSuppressed:
                bom_dict["parts"].append(child_dict)

        return  bom_dict

    def get_data_dict(self):
        return self.bom

class IFTPart: 
    """
    This class contains all important functionalities to get data of a NXOpen.Part or NXOpen.Assembly.Component
    that may be usefull in the BOM (Bills of Materials) generated in the IFTBOM class.
    """
    @classmethod
    def get_mass(cls, component):
        part = component.Prototype
        uf_session = NXOpen.UF.UFSession.GetUFSession()
        weight_props = uf_session.Weight.AskProps(part.Tag, NXOpen.UF.Weight.UnitsType.UNITS_KM)
        if weight_props.Mass == 0: # mass has to be calculated first
            weight_props, _ = uf_session.Weight.EstabPartProps(part.Tag, 0.99, False, NXOpen.UF.Weight.UnitsType.UNITS_KM)	
            mass = weight_props.Mass
        else:
            mass = weight_props.Mass
        return mass 
  
        
        return weight_props.Mass

    @classmethod
    def get_quantity(cls, component):
        """
        Gets the number of occurrances of an object in the CAM setup

        Input:
        - component:NXOpen.Assemblies.Component

        Returns:
        - quantity:int
        """
        quantity = component.GetIntegerQuantity()
        return quantity 

    @classmethod
    def get_position(cls, component):
        """
        Gets the 3D coordinates of a and the rotation of a component.

        Example of output:
        position = {"x": 10, "y": 20, "z": 30}
        rotation = {"xx": 1, "xy": 0, "xz":0, "yx": 0, "yy": 1, "yz": 0, "zx": 0, "zy": 0, "zz": 1}

        Input:
        - component: NXOpen.Assemblies.Component

        Returns:
        - position:dict 
        - rotation:dict
        """
        pos, rot = component.GetPosition() # Gets the position coordinates and rotation matrix
        position = {"x": round(pos.X,3), "y": round(pos.Y,3), "z": round(pos.Z,3)}
        rotation = {"xx": round(rot.Xx,3), "xy": round(rot.Xy,3), "xz": round(rot.Xz,3),
                    "yx": round(rot.Yx,3), "yy": round(rot.Yy,3), "yz": round(rot.Yz,3),
                    "zx": round(rot.Zx,3), "zy": round(rot.Zy,3), "zz": round(rot.Zz,3)}
        return position, rotation

    @classmethod
    def get_material(cls, component):
        """
        Gets the physical material of the components/parts. This is not to be confused with the material of the 
        machining part. If a physical material is available, the mass of the component/part can be calculated.

        The returned value is the name of the material in the material library

        Input:
        - component:NXOpen.Assemblies.Component

        Returns:
        - material:str
        """
        material = None
        if component.IsOccurrence:
            part = component.Prototype
            materials = part.MaterialManager.PhysicalMaterials.GetUsedMaterials()
            if len(materials) == 1:
                material = materials[0].Name
            elif len(materials) > 1:
                nx_logger(f"ERROR","Part '{part.Name}' has multiple materials")
        return material 
    
    @classmethod
    def export_stl(cls, part:NXOpen.Part, output_dir:str): 
        """
        Exports the STL file of a part to a desired output directory.
        
        Inputs:
        - part:NXOpen.Part 
        - output_dir:str 
        """
        body_collection = list(part.Bodies)
        if len(body_collection) == 1:
            for body in body_collection:
                # Create STL export builder:
                stl_creator = NXOpen.Session.GetSession().DexManager.CreateStlCreator()
                stl_creator.AutoNormalGen = True
                # Tolerances of output file
                stl_creator.ChordalTol = 0.080000000000000002 
                stl_creator.AdjacencyTol = 0.080000000000000002
                stl_creator.ExportSelectionBlock.Add(body)
                stl_creator.OutputType = NXOpen.STLCreator.OutputTypeEnum.Binary
                stl_creator.OutputFile = output_dir 
                stl_creator.Commit()
                stl_creator.Destroy()
        elif len(body_collection) > 1:
            nx_logger("ERROR", f"STL for NXOpen.Part '{part.JournalIdentifier} could not be exported, due to multiple bodies.")
        else:
            nx_logger("ERROR", f"STL for NXOpen.Part '{part.JournalIdentifier} could not be exported, because of missing body.")

if __name__ == '__main__':
    if True: 
        ift_bom = IFTBOM()
        ift_bom.get_data_attributes()
        print_nx(json.dumps(ift_bom.get_data_dict(), indent = 2))


    if False: 
        for part in ift_bom.part_list:
            stl_dir = "C:\\Users\\julia\\Desktop\\stl_documents"
            nx_logger("INFO",f"STL of {part.JournalIdentifier} was generated in {stl_dir}")
            IFTPart.export_stl(part, stl_dir)


