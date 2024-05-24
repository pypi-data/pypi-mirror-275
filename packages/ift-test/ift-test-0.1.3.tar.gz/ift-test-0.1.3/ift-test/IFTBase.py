# nx: threaded

import NXOpen
import NXOpen.CAM
import NXOpen.UF
import json
from datetime import datetime
from pymongo import MongoClient
import os 
import numpy
import sys
from inspect import currentframe, getframeinfo, stack, getmodule


class IFTCollection:
	"""
	This class organizes the IFTObjects and is needed to created them. The IFTObject instances are
	stored as dictionary in the IFTCollection.ift_objects attribute. The IFTCollection is also used
	to first get the NXObjects. They are stored in the IFTCollection.nx_objects.
	"""

	def __init__(self):
		self.nx_counter = 0  # counts number of NXOpen.Object instances
		self.nx_objects = dict()  # container of NXOpen.Object instances
		self.ift_counter = 0  # counts number of IFTObject instances
		self.ift_objects = dict()  # container of IFTObject instances

	def get_dict(self):
		data_dict = dict()
		data_dict["id"] = self.id
		return data_dict
	

class IFTObject:
	'''
	An IFTObject is the personalized class to store data retrieved from an Siemens NX CAM setup.
	
	It also stores the NXOpen.Object as class attribute. This class willl be used for inheritence
	to other classes in this package. 

	Attributes
	----------
	relation_name_single : str (class attribute)
		defines the foreign key in the JSON structure if it is a One-To-Many relation
	relations_name_plural : str (class attribute)
		defines the foreign key in the JSON structure if it is a Many-To-Many relation
	nx_object : NXOpen.Object
		stores the corresponding object from NXOpen 
	id : str
		the unique identifier of the object within a CAM setup
	has_data_attributes : bool
		defines if data was already retrieved from NXOpen
	foreign_ids_dict : dict
		stores relations to other IFTObject instances
	data_dict : dict
		container of the data contained in the instance (is used for the JSON structure)

	Methods
	-------
	get_data_attributes()
		retrieves all relevant data by using the NXOpen API
	set_data_attributes()
		here the number of class attributes are defined
	get_data_dict()
		returns the data_dict attribute
	print_data_dict()
		prints the data_dict attribute to the NXOpen.ListingWindows
	add_relations_to_data_dict()
		inserts the foreign_ids_dict to data_dict

	'''
	relation_name_single = "ObjectId" # name that is used to relate from other classes to one of this class
	relation_name_plural = "ObjectIds"
	# these values have to be overridden in every subclass (e.g., IFTTool -> relation_name_single = toolId)

	def __init__(self, ift_collection:IFTCollection, idx:int):
		"""
		Initialize an IFTObject

		Parameters
		----------
		ift_collection : IFTCollection
			the IFTCollection instance belonging to the IFTObject class (e.g, IFTTool --> IFTToolCollection)
		idx : int
			the index of the NXOpen.Object instance in the IFTCollection.nx_objects attribute
		"""
		nx_object = ift_collection.nx_objects[idx]  # getting the NXOpen.Object from the collection
		self.set_data_attributes() # initiates the data attributes as None values
		if idx > ift_collection.nx_counter:
			IFTCore.nx_logger("ERROR", f"Cannot create instance of type {type(self)}. Number of index exceeds number of nx_objects")
		if nx_object.JournalIdentifier in ift_collection.ift_objects.keys():
			IFTCore.nx_logger("WARNING", f"Instance {nx_object.JournalIdentifier} of type {type(self)} already exists.")
		else:  
			self.nx_object = nx_object  # stores the NXOpen.Object as instance in the IFTObject class
			self.id = ift_collection.nx_objects[idx].JournalIdentifier  # sets identifier - here the JournalIdentifier is used
			ift_collection.ift_objects[self.nx_object.JournalIdentifier] = self  # stores instance IFTCollection class
			ift_collection.ift_counter +=1  # sets new counter of class instances
			self.has_data_attributes = False  # boolean variable that checks if NX data was already extracted
			self.foreign_ids_dict = dict()  # dictionary for foreign ids - this is used for the data relations
			self.set_data_attributes()
			self.data_dict = {}
			
	def get_data_attributes(self):
		"""
		By using get_data_attributes, relevant data from Siemens NX is extracted and stored to the current instance.
		This method must be overloaded and customized for every sub-class.
		"""
		IFTCore.nx_logger("ERROR", f"Method get_data_attributes is not defined for object of type {type(self)}.")

	def set_data_attributes(self):
		"""
		Here all relevant attributes of the class are initialized. This method must be overloaded and customized
		for every sub-class
		"""
		pass 

	def get_data_dict(self):
		"""
		Returns dictionary with data
		"""
		if not self.has_data_attributes:
			self.get_data_attributes()	
		return  {"id":self.id, "type":str(type(self))}

		
	def print_data_dict(self):
		"""
		Prints the data_dict to the NXOpen.ListingWindow
		"""
		IFTCore.print_nx(json.dumps(self.get_data_dict(), indent = 2))

	def add_relations_to_data_dict(self):
		"""Adds relations in foreign_ids_dict to the data_dict attribute"""
		for key, value in self.foreign_ids_dict.items():
			self.data_dict[key] = value 


class IFTGeometryCollection(IFTCollection):
	"""
	The IFTGeometryCollection is a collection class for NXOpen.Objects that have geometric objects
	as instances for example faces, edges. The get_many_to_many_relation and the 
	get_one_to_many_relation is used to get the relations between two IFTGeometryObjects. 

	Methods 
	-------
	get_many_to_many_relation(self, other):
		Maps the relations between the IFTGeometryObjects of two IFTGeometryCollection instances
	get_one_to_many_relation(self, other):
		Maps the relations between the IFTGeometryObjects of two IFTGeometryCollection instances

	"""

	def __init__(self):
		super().__init__()

	def get_many_to_many_relation(self, other):
		"""
		Function to realize many to many relation.

		Parameters
		----------
		other : IFTGeometryCollection
			the collection the self collection is related with

		Notes
		----- 
		Adds the related IFTGeometryObjects of another IFTGeometryCollection
		to the attribute foreign_ids_dict dictionary
		
		"""
		for self_object in self.ift_objects.values():
			if not self_object.has_relations:
				foreign_ids = list() # initialize list containing the foreign mapped
				# add object ids if they have faces in common
				for other_object in other.ift_objects.values():
					for self_face_id in self_object.face_ids:
						if self_face_id in other_object.face_ids:
							# list containing all ids of the other object sharing a face with the self object
							foreign_ids.append(other_object.id)        
				if len(foreign_ids) == 0: # there could no object be found with sharing faces
					IFTCore.nx_logger("WARNING", f"No related {other_object} for object {self_object} could be found.")
				else: # add list of related object to foreign_ids
					self_object.foreign_ids_dict[other_object.relation_name_plural] = list(numpy.unique(foreign_ids))

	def get_one_to_many_relation(self, other):
		"""
		Function to realize one to many relation.

		Adds the related IFTGeometryObjects of different contained in the given 
		IFTGeometryCollections to the self.foreign_ids_dict dictionary

		Parameters
		----------
		other : IFTGeometryCollection
			the collection the self collection is related with

		Notes
		----- 
		Adds the related IFTGeometryObjects of another IFTGeometryCollection
		to the attribute foreign_ids_dict dictionary
		"""

		for self_object in self.ift_objects.values():
			if not self_object.has_relations:
				foreign_ids = list() # initialize list containing the foreign mapped
				# add object ids if they have faces in common
				for other_object in other.ift_objects.values():
					for self_face_id in self_object.face_ids:
						if self_face_id in other_object.face_ids:
							# list containing all ids of the other object sharing a face with the self object
							foreign_ids.append(other_object.id)        
				if len(foreign_ids) == 0: # there could no object be found with sharing faces
					IFTCore.nx_logger("WARNING", f"No related {other_object} for object {self_object} could be found.")
				else: # check if relation is unique and if not choose the most frequent value
					foreign_id, frequency = IFTCore.find_most_frequent(foreign_ids)
					if frequency > 1:
						IFTCore.nx_logger("WARNING", f"Ambiguous relation of object {self_object._id}")
					self_object.foreign_ids_dict[other_object.relation_name_single] = foreign_id   


class IFTGeometryObject(IFTObject):
	"""
	An IFTGeometry is the personalized class to store data retrieved from an Siemens NX CAM setup
	containing geometrical features like faces and edges. This class is inherited from IFTObject.
	It also stores the NXOpen.Object as class attribute. This class willl be used for inheritence
	to other classes in this package. 

	Attributes
	----------
	relation_name_single : str (class attribute)
		defines the foreign key in the JSON structure if it is a One-To-Many relation
	relations_name_plural : str (class attribute)
		defines the foreign key in the JSON structure if it is a Many-To-Many relation
	nx_object : NXOpen.Object
		stores the corresponding object from NXOpen 
	id : str
		the unique identifier of the object within a CAM setup
	has_data_attributes : bool
		defines if data was already retrieved from NXOpen
	foreign_ids_dict : dict
		stores relations to other IFTObject instances
	data_dict : dict
		container of the data contained in the instance (is used for the JSON structure)
	faces : list
		Contains the NXOpen.Face objects of the NXOpen.Object instance
	edges : list
		Contains the NXOpen.Egde objects of the NXOpen.Object instance
	face_ids : list 
		Contains the JournalIdentifiers of the NXOpen.Face instances in faces
	edge_ids : list
		Contains the JournalIdentifiers of the NXOpen.Edge instances in edges
	has_relation : bool
		Tells if the relations were already mapped to the object or not 

	Methods
	-------
	get_data_attributes()
		retrieves all relevant data by using the NXOpen API
	set_data_attributes()
		here the number of class attributes are defined
	get_data_dict()
		returns the data_dict attribute
	print_data_dict()
		prints the data_dict attribute to the NXOpen.ListingWindows
	add_relations_to_data_dict()
		inserts the foreign_ids_dict to data_dict

	"""

	def __init__(self, ift_geometry_collection:IFTGeometryCollection, idx:int):
		super().__init__(ift_geometry_collection, idx)
		self.faces = list() # list of NXOpen.Face objects
		self.face_ids = list() # list of NXOpen.Face.JournalIdentifiers
		self.edges = list() # list of NXOpen.Edge objects
		self.edge_ids = list() # list of NXOpen.Edge.JournalIdentifiers
		self.has_relations = False 


class IFTCAMSetup:
	"""
	This class holds information about the CAM setup like identifier and useful NXOpen objects
	that are often used in CAM setups.


	"""
	id = None 

	def __init__(self):
		try:
			self.nx_session = NXOpen.Session.GetSession()  # active NX session
			self.nx_uf_session = NXOpen.UF.UFSession.GetUFSession()  # active UF session
			self.nx_work_part = self.nx_session.Parts.Work  # active workpart
			self.nx_operation_collection = self.nx_work_part.CAMSetup.CAMOperationCollection  # Operation collection 
			self.nx_cam_setup = self.nx_session.Parts.Work.CAMSetup  # CAM setup
			self.nx_group_collection = self.nx_work_part.CAMSetup.CAMGroupCollection  # group collection (contains for instance tools, machine, etc.)
			self.nx_machine_root = self.nx_work_part.CAMSetup.GetRoot(NXOpen.CAM.CAMSetup.View.MachineTool)  # machine tool view parent
			self.nx_geometry_root = self.nx_work_part.CAMSetup.GetRoot(NXOpen.CAM.CAMSetup.View.Geometry)  # geometry view parent
			self.nx_program_root = self.nx_work_part.CAMSetup.GetRoot(NXOpen.CAM.CAMSetup.View.ProgramOrder)  # program view parent
		except: 
			IFTCore.nx_logger("ERROR", "Open NX session is no CAM setup")
			sys.exit(1)

		self.set_data_attributes()

	def get_data_attributes(self):
		self.get_history_info()
		self.set_id()
		self.set_setup_id_revision_and_creator()
		self.set_editor()

	def get_history_info(self):
		"""
		Returns the history events of the CAM-Setup as list of dictionaries. This contains information of the
		user that changed the CAM setup and when 
		"""
		hist_events = NXOpen.Session.GetSession().Parts.Work.GetHistoryInformation()
		hist_event_dict = {}
		for event in hist_events:
			mtimestr = event.Time.replace('\u00e4','ae')
			if len(event.User) > 0:  # there are some entries without name that are automatically created
				hist_event_dict[event.Version] = {"time": mtimestr, "program": event.Program, "machine": event.Machine, "user": event.User}
		return hist_event_dict

	def set_editor(self):
		'''
		Sets the editor of the CAM Session. The editor is represented by the actual Windows user
		'''
		self.editor = os.getlogin()

	@staticmethod
	def set_id(doe_id='ts'):
		'''
		Creates and sets a timestamp of the JSON creation time. This timestamp is used to identify the different JSON files unamigiousliy.
		'''
		if doe_id=='ts':
			ts = datetime.now()
			timestamp =  f"{ts.year}_{ts.month}_{ts.day}_{ts.hour}_{ts.minute}_{ts.second}"
			IFTCAMSetup.id = timestamp
		else:
			IFTCAMSetup.id = doe_id

	def set_setup_id_revision_and_creator(self):
		'''
		Creates and sets the setup_id, creators name and the revision number. This setup_id is the identifier for the CAM-Setup. 
		If a CAM-Setup is changed and stored again, the two documents can be distinguished by the revision number and the _id. 
		It iterates through the files of the set IFTCore.storage_dir and looks and gets so the revision number.
		'''
		# First the setup of the current CAM setup is created
		if not self.setup_id:  # case: ids are not set already 
			hist_event_dict = self.get_history_info() # history of the CAM Setup
			first_key = list(hist_event_dict.keys())[-1] 
			date = hist_event_dict[first_key]["time"]
			user = hist_event_dict[first_key]["user"]
			date_list = date.split(" ")
			month_dict = {"Jaen":1, "Feb":2, "Maer":3, "Apr":4,"Mai":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Okt":10,"Nov":11,"Dez":12}
			try:
				id_str = f"{date_list[2]}_{month_dict[date_list[1]]}_{date_list[0]}_{date_list[3].replace(':','_')}_{user}"
			except:
				id_str = date 
				IFTCore.nx_logger("ERROR", f"Setup id could not be created. Original Date was used. Revisioning of data will not work.")
			
		# # Now the revision number is determined
		# file_dir = os.path.dirname(__file__)
		# config_path = file_dir + "\\static\\configuration.json"

		# with open(config_path, "r") as file:
		# 	config = json.load(file)
		# file.close()
		# # storage_dir = config["storage_dir"]
		
		revision_counter = 0
		# for folder in os.listdir(storage_dir):
		# 	data_path = os.path.join(storage_dir, folder,"CAM_SETUP.json" )
		# 	try:
		# 		with open(data_path, "r") as file:
		# 			cam_setup_data = json.load(file)
		# 		file.close()
		# 		if cam_setup_data["setupId"] == id_str:
		# 			revision_counter +=1
		# 	except: 
		# 		IFTCore.nx_logger("WARNING", f"Could not open {data_path}.")
			
		self.revision = revision_counter # sets revision number
		self.setup_id = id_str # sets the setup id
		self.creator = user # sets the original creator of the CAM setup

	def set_data_attributes(self):
		self.data_dict = {}
		self.editor = None # last editor of the CAM setup
		self.creator = None # original creator of CAM setup
		self.id = None # the identifier for the JSON file that should be exported
		self.setup_id = None # the identifier of the CAM setup. This id stays the same when the setup is changed
		self.pdf_path = None # path where 3D PDF of CAM setup is stored
		self.nc_code_path = None # path where NC code of CAM setup is stored
		self.revision = None # revision number of the stored data

	def get_data_dict(self):
		data_dict = {}
		data_dict["_id"] = IFTCAMSetup.id
		data_dict["setupId"] = self.setup_id
		data_dict["revison"] = self.revision
		data_dict["creator"] = self.creator
		data_dict["editor"] = self.editor
		data_dict["3DPDF"] = self.pdf_path
		data_dict["NCCode"] = self.nc_code_path 
		self.data_dict = data_dict
		return data_dict


class IFTCore:
	"""
	This class contains useful functions that are not directly related to just one object type, but can be useful in general.
	"""

	storage_dir = None  # defines the storage directory where all files are stored

	@staticmethod
	def emphasize():
		"""
		Can be used to emphasize a statment in the NXOpen.Session.ListingWindow
		"""
		IFTCore.print_nx("=====================================================================================")

	@staticmethod
	def find_most_frequent(values:list):
		'''
		Returns the most frequent value of a list and the number of occurences of this value.
		'''
		value_dict = {}
		for item in values:
			value_dict[item] = value_dict.get(item, 0) + 1
		max_value = max(value_dict.values())
		counter = 0
		for key, value in value_dict.items():
			if (counter == 0 and value == max_value): 
				most_frequent = key
				counter +=1
			elif (counter != 0 and value == max_value):
				counter +=1

		return most_frequent, counter
 
	@classmethod
	def nx_logger(cls, error_level: str, string: str):
		"""
		Logs an error, writes it into the NXOpen.ListingWindow and stores it inside of a Logger file if the 
		IFTCore.storage_dir is set. If not the message will be only printed to the NXOpen.ListingWindow
		"""
		cf = currentframe()
		line = cf.f_back.f_lineno 
		frame = stack()[1]
		module = getmodule(frame[0]).__file__
		if (error_level == "INFO" or error_level == "WARNING"):
			string_conc = f"{error_level}: {string}"
		else:
			string_conc =  f"{error_level}: In module {module}, line {line} -> {string}"
		cls.print_nx(string_conc)
		
		# Write message in log file
		try:
			logging_file = cls.storage_dir + "\\logs.txt"
			with open(logging_file,'a') as file:
				file.write(string_conc + "\n")
			file.close()
		except:
			pass 

	@staticmethod
	def get_database(user, password):
		"""
		This function creates a connection to the MongoDB and returns the database. 
		
		NOTE: This is only the database. You have to specifiy the collection too by Typing the name of the collection
		as key notation or dot notation, for example:

		db["nx_data"] or db.nx_data
		"""

		cluster_name = 'Cluster0'
		connection_string = f"mongodb+srv://{user}:{password}@{cluster_name}.bnat5ra.mongodb.net/?retryWrites=true&w=majority"
		print(connection_string)
		client = MongoClient(connection_string)
		db = client["ift"]
		return db

	@classmethod
	def get_by_tag(cls, tag):
		'''
		Returns an NXOpen.Object with the corresponding NXOpen.Object.Tag
		'''
		obj = NXOpen.Utilities.NXObjectManager.Get(tag)
		return obj

	@classmethod
	def get_by_journal_identifier(cls, journal_identifier):
		'''
		Returns the NXOpen object with the corresponding journal identifier.
		ATTENTION: this still must be implemented. It only works for CAMGroupCollection objects.
		'''
		try:
			nx_object = NXOpen.Session.GetSession().Parts.Work.CAMSetup.CAMGroupCollection.FindObject(journal_identifier)
		except:
			cls.nx_logger("ERROR",f"Method IFTCore.get_by_journal_dientifier works only for objects in NXOpen.CAM.NXGroupCollection")
		return nx_object
	
	@classmethod
	def print_nx(cls, object_to_print):
		'''
		Prints given string or object into NX-Listing-Window
		'''
		session = NXOpen.Session.GetSession()
		lw = session.ListingWindow
		lw.Open()
		lw.WriteLine(str(object_to_print))

	@classmethod
	def get_storage_dir(cls):
		"""Gets the storage directory defined in ..\\static\\configuration.json"""
		file_dir = os.path.dirname(__file__)
		config_path = file_dir + "\\static\\configuration.json"

		with open(config_path, "r") as file:
			config = json.load(file)
		file.close()
		storage_dir = config["storage_dir"]

		# Add the CAMSetup.id to the storage dir
		if not IFTCAMSetup.id:
			IFTCAMSetup.set_id()
		
		cls.storage_dir = os.path.join(storage_dir, IFTCAMSetup.id)
		return cls.storage_dir


if __name__ == '__main__':
	cam_setup = IFTCAMSetup()
	cam_setup.get_data_attributes()
	data_dict = cam_setup.get_data_dict()
	IFTCore.print_nx(json.dumps(data_dict, indent = 2))
