# nx: threaded
import json
import NXOpen
import NXOpen.CAM
from IFT.IFTBase import IFTCore, IFTObject, IFTGeometryObject, IFTGeometryCollection
import os
print_nx = IFTCore.print_nx
nx_logger = IFTCore.nx_logger 

class IFTMachiningFeatureCollection(IFTGeometryCollection):
	'''
	Collection of machining features in the machining part. 
	Sometimes machining parts are not used by the engineer. 
	Therefore an auto feature recognition will be applied.
	'''
	
	def __init__(self):
		super().__init__()
		try:
			existing_features = list(NXOpen.Session.GetSession().Parts.Work.CAMFeatures)
		except:
			existing_features = list()
			nx_logger("ERROR", "Problem with cam features detected")
		if len(existing_features) > 0:
			nx_logger("INFO", f"INFO: Already {len(existing_features)} features detected")
		features = self.feature_recognition() # list of recognized NXOpen.CAM.CAMFeature 
		features.extend(existing_features)
		for feature in features:
			self.nx_objects[self.nx_counter] = feature
			self.nx_counter +=1

	@classmethod
	def feature_recognition(cls):
		'''
		This function causes an automatic generation of Features in Siemens NX. 
		Returns a list of NXOpen.CAM.CAMFeature instances

		Returns:
		- feature_list:list
		'''
		# -- Create feature recognition builder -- 
		session = NXOpen.Session.GetSession()
		frb = session.Parts.Work.CAMSetup.CreateFeatureRecognitionBuilder(NXOpen.CAM.CAMObject.Null)

		# -- Setup feature recognition builder
		frb.AddCadFeatureAttributes = True
		frb.MapFeatures = False
		frb.AssignColor = True
		frb.RecognitionType = NXOpen.CAM.FeatureRecognitionBuilder.RecognitionEnum.Parametric
		frb.UseFeatureNameAsType = True
		frb.IgnoreWarnings = False
		frb.SetMachiningAccessDirection([], 0.0)

		# -- Get the list of features that should be recognized. 
		# You can change the .\\static\\featuretypes.txt file if you want to remove certain features
		feature_types = cls.get_feature_types()
		frb.SetFeatureTypes(feature_types)
		frb.GeometrySearchType = NXOpen.CAM.FeatureRecognitionBuilder.GeometrySearch.Workpiece
		feature_list = list(frb.FindFeatures())
		frb.Destroy()
		return feature_list

	@staticmethod
	def get_feature_types():
		'''
		Creates list of all feature types that are defined in the featuretypes.txt file 
		which can be found in the static folder of the package. 

		Returns:
		- feature_types:list
		'''
		feature_types = list()
		module_path = os.path.dirname(os.path.abspath(__file__))
		file_path = module_path + "\\static\\featuretypes.txt"

		with open(file_path) as file: 
			for line in file:
				if not '#' in line:
					feature_types.append(line.strip("\n"))
		return feature_types

class IFTMachiningFeature(IFTGeometryObject):
	'''
	Class for the IFTFeatures. Here the machining features of Siemens NX are mapped to the ones of
	ISO 10303-1814:2019(E). 
	The ISO HTML document for this part of ISO 10303 can be found here:
	https://ap238.org/SMRL_v8_final/data/modules/machining_features/sys/cover.htm
	'''

	relation_name_single = "machiningFeatureId"
	relation_name_plural = "machiningFeatureIds"

	def __init__(self, feature_collection, idx):
		super().__init__(feature_collection, idx)
		# Create warning if status is not up-to-date 
		feature = self.nx_object
		if (feature.Status != NXOpen.CAM.CAMFeature.State.UpToDate and feature.Status != NXOpen.CAM.CAMFeature.State.Updated):
			nx_logger("WARNING", f"Feature {feature.Name} is not up-to-date")

	def get_data_attributes(self):
		self.get_faces()
		self.type = self.nx_object.Type
		self.get_feature_attributes()

	@classmethod
	def get_attribute_value(cls, attribute: NXOpen.CAM.CAMAttribute):
		"""
		Gets the key, value pair of the current attribute. These attributes can be of different types.
		Thats why NXOpen offers different methods to get the values.

		Input: attribute: NXOpen.CAM.CAMAttribute 
		Output: key: str, value: str
		"""
		key = attribute.Name
		try:
			if NXOpen.CAM.CAMAttribute.ValueType.Integer == attribute.Type:
				value = attribute.GetIntegerValue()
			elif NXOpen.CAM.CAMAttribute.ValueType.Double == attribute.Type:
				value = round(attribute.GetDoubleValue(),3)
			elif NXOpen.CAM.CAMAttribute.ValueType.String == attribute.Type:
				value = attribute.GetStringValue()
			elif NXOpen.CAM.CAMAttribute.ValueType.Bool == attribute.Type:
				value = attribute.GetBoolValue()
			elif NXOpen.CAM.CAMAttribute.ValueType.Point3 == attribute.Type:
				value = attribute.GetPoint3Value()
			elif NXOpen.CAM.CAMAttribute.ValueType.Vector3 == attribute.Type:
				value = attribute.GetVector3Value()
		except:
			value = None
		
		return key, value 

	def get_faces(self):
		"""
		Gets the faces of the machining part
		"""
		for face in self.nx_object.GetFaces():
			if face.IsOccurrence:  # In this case the NXOpen.Face is a copied Object and not the original
				face = face.Prototype
			self.faces.append(face) 
			self.face_ids.append(face.JournalIdentifier)
	
	def get_feature_attributes(self):
		'''
		Sets a dictionary of key, value pairs of the attributes belonging to the IFTFeature instance.

		Sets: self._attributes: dict
		'''
		feature = self.nx_object
		attributes = feature.Attributes # every feature has attributes depending on the type of feature
		
		# Get dictionary of attributes
		attribute_dict = dict()
		for attribute in attributes:
			key, value = self.get_attribute_value(attribute)
			attribute_dict[key] = value
		self.attributes = attribute_dict

	def set_data_attributes(self):
		self.machining_part_id = None 
		self.type = None 
		self.attributes = None

	def get_data_dict(self):
		"""
		Returns dictionary for the MongoDB export. The argument attributes is a dictionary that changes 
		depending on the feature type. 
		"""
		self.data_dict["machiningFeatureId"] = self.id 
		self.add_relations_to_data_dict()
		self.data_dict["type"] = self.type
		self.data_dict["attributes"] = self.attributes
		return self.data_dict 


if __name__ == '__main__':
	print_nx = IFTCore.print_nx
	features = IFTMachiningFeatureCollection()
	if True:
		for idx in range(features.nx_counter):
			feature = IFTMachiningFeature(features, idx)
			feature.get_data_attributes()
			print_nx(feature.id)
			print_nx(feature.face_ids)
			#print_nx(json.dumps(feature.get_data_dict(),indent = 2))

	






	


		


