# nx: threaded
import json
import NXOpen
import NXOpen.CAM
import os
from pathlib import Path

from IFT.IFTBase import IFTCore, IFTObject, IFTCollection
print_nx = IFTCore.print_nx
nx_logger = IFTCore.nx_logger 


class IFTMachine(IFTObject):

	def __init__(self):
		# -- Set data for machine -- 
		pseudo_collection = IFTCollection()
		machine = NXOpen.Session.GetSession().Parts.Work.CAMSetup.GetRoot(NXOpen.CAM.CAMSetup.View.MachineTool)
		pseudo_collection.nx_objects = {0: machine}
		super().__init__(pseudo_collection,0) 


	def get_data_attributes(self):
		# -- Get post processor -- 
		self.get_post_processor()
		# -- Get data stored in the machine library -- 
		self.get_machine_lib_values()

	def get_data_dict(self):
		self.data_dict =  {"machineId": self.id, 
				"machineType": self.type,
				"machineControl": self.control,
				"postProcessor": self.post_processor, 
				"maxFeedRate":self.max_feed_rate, 
				"spindleTorque":self.spindle_torque,
				"spindlePower":self.spindle_power,}
		return self.data_dict

	def get_post_processor(self):
		machine_data_dir = NXOpen.Session.GetSession().GetEnvironmentVariableValue("UGII_CAM_LIBRARY_MACHINE_DATA_DIR") # machine directory on your installation path
		machine_data_path = os.path.join(machine_data_dir, "machine_database.dat") # path of the configuration file of the installed machines
		
		try:
			# -- Get the installed machine -- 
			search_name = self.nx_object.Name.replace("_", " ").upper()
			with open(machine_data_path) as f:
				for line in f:
					if  search_name in line.upper() or self.nx_object.Name in line.upper():
						line_split = line.split("|")
						install_path_full = line_split[6] # install path of actual machine with {UGII_CAM_LIBRARY_INSTALLED_MACHINES_DIR}
						install_path_filtered = install_path_full.split("}")[-1]
			f.close()

			installed_machines_dir = NXOpen.Session.GetSession().GetEnvironmentVariableValue("UGII_CAM_LIBRARY_INSTALLED_MACHINES_DIR")
			installed_machine_data_path = os.path.join(installed_machines_dir, install_path_filtered) # path of the .dat file of the machine 
			with open(installed_machine_data_path)as f:
				for line in f:
					if (".tcl" in line  and ".def" in line):
						self.post_processor = line.split(",")[0]
			f.close()
		except:
			IFTCore.nx_logger("ERROR","Postprocessor is not defined or could not be found. NC-Code will not be exported")

	def get_nc_code(self, file_dir : str):
		# -- Get the NC-Groups of the CAM-Setup
		cam_setup = NXOpen.Session.GetSession().Parts.Work.CAMSetup
		program_root = cam_setup.GetRoot(NXOpen.CAM.CAMSetup.View.ProgramOrder)
		childs = program_root.GetMembers()
		nc_groups = list() # list of nc-groups
		for child in childs:
			if child.Name != "NONE": # Sort out unused items
				nc_groups.append(child)

		# == Postprocess every nc-group ==
		
		# -- Configuration of post processing --
		#path = Path(os.path.abspath(__file__)).parent.absolute()
		#file_dir = os.path.join(path, "build\\nc_code.ptp")
		output_units = NXOpen.CAM.CAMSetup.OutputUnits.PostDefined
		output_warning = NXOpen.CAM.CAMSetup.PostprocessSettingsOutputWarning.No
		review_tool = NXOpen.CAM.CAMSetup.PostprocessSettingsReviewTool.PostDefined
		post_mode = NXOpen.CAM.CAMSetup.PostprocessSettingsPostMode.Normal
		
		if len(nc_groups) > 1:
			nx_logger("ERROR","Several machining parts in CAM setup, NC code file will be overridden")
		
		# Uncomment if you want to post nc code on mongo db
		# -- Generate post for mongodb including the G-Code --
		#try:
		#	file_id = IFTCore._id
		#except:
		#	file_id = "id_not_set"
		#
		#nc_code_post = {"_id":file_id, "NCCode": {}}

		nc_group = nc_groups[0]
		cam_setup.PostprocessWithPostModeSetting(nc_group.GetMembers(), self.post_processor, file_dir, output_units, 
																output_warning, review_tool, post_mode)
		
			# Read data from written file 
			#with open(target_dir) as f:
			#	text = f.read()
			#f.close()
			#nc_code_post["NCCode"][nc_group.Name] = text 
		
		#return nc_code_post

	def get_machine_lib_values(self):
		"""
		Gets the machine library values for the used machine. 
		"""
		
		mapping_dict = {"MDM0101":"Mill","MDM0104":"TurnMill","MDM0201":"Lathe","MDM0204":"MillTurn","MDM0301":"Wedm","MDM901":"Generic"}	
		# Have a look at machine_database.dat %UGII_BASE_DIR%\MACH\resource\library\machine\ascii	
		machine = self.nx_object
		machine_builder = NXOpen.Session.GetSession().Parts.Work.CAMSetup.CAMGroupCollection.CreateMachineGroupBuilder(machine)
		for i in dir(machine_builder):
			#print_nx(i)
			pass 

		kinematic_configurator = NXOpen.Session.GetSession().Parts.Work.KinematicConfigurator
		machine_lib_builder = kinematic_configurator.CreateMachineLibraryBuilder()
		attribute_names = machine_lib_builder.GetAllAttributeNames()
		machine_names = machine_lib_builder.GetAllMachineNames()
		machine_lib_name = None 
		for machine_name in machine_names:
			if machine_name in machine.Name:
				machine_lib_name = machine_name
			
		if machine_lib_name:
			self.type = mapping_dict[machine_lib_builder.GetValue(machine_lib_name,"Type")]
			self.description = machine_lib_builder.GetValue(machine_lib_name,"Description")
			self.control = machine_lib_builder.GetValue(machine_lib_name,"Control")
			self.config_file = machine_lib_builder.GetValue(machine_lib_name,"config_file")
			self.part_file_path = machine_lib_builder.GetValue(machine_lib_name,"part_file_path")
		else:
			nx_logger("ERROR", f"No library entry for machine {machine.Name} could be found.")

		machine_lib_builder.Destroy()



		#print_nx(IFTCore.nx_cam_setup.LibraryReference)
		#print_nx(machine_builder.Description)
		#print_nx(machine_builder.RapidFeed.Value)
		#print_nx(machine_builder.ToolChangeTime.Value)

		# Properties builder
		#generalPropertiesBuilder = IFTCore.nx_work_part.PropertiesManager.CreateGeneralCAMPropertiesBuilder([machine])
		#for i in dir(generalPropertiesBuilder):
		#	print_nx(i)

		#generalPropertiesBuilder.Information()
		#print_nx(generalPropertiesBuilder)
		#generalPropertiesBuilder.Destroy()

		machine_builder.Destroy()
	
	def get_max_feed_speed(self):
		"Still needs to be implemented"
		pass

	def get_spindle_torque(self):
		"Still needs to be implemented"
		pass

	def get_spindle_power(self):
		"Still needs to be implemented"
		pass 

	def set_data_attributes(self):
		self.type = None 
		self.spindle_power = None 
		self.spindle_torque = None 
		self.control = None 
		self.post_processor = None 
		self.max_feed_rate = None 
if __name__ == '__main__':
	
	machine = IFTMachine()
	machine.get_data_attributes()
	print_nx(json.dumps(machine.get_data_dict(), indent = 2))



	