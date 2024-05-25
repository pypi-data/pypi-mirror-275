# nx: threaded
import NXOpen
import NXOpen.CAM
import NXOpen.Annotations
from inspect import currentframe, getframeinfo
import json

from ift-dbms.IFTBase import IFTCore, IFTObject, IFTGeometryObject, IFTGeometryCollection
from ift-dbms.IFTMachiningPart import IFTMachiningPartCollection
print_nx = IFTCore.print_nx
nx_logger = IFTCore.nx_logger

class IFTPmiCollection(IFTGeometryCollection):
	'''
	An IFTPmiCollection is a container of all NX Pmi Objects.
	'''

	def __init__(self):
		super().__init__()
		machining_parts = IFTMachiningPartCollection() # list ofparts that are defined for machining in WORKPIECE
		for part in machining_parts.nx_objects.values():
			for pmi in part.PmiManager.Pmis:
				self.nx_objects[self.nx_counter] = pmi 
				self.nx_counter += 1


class IFTPmi(IFTGeometryObject):
	"""
	An IFTPmiCollection is a container of all NX Pmi Objects.

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
	view_ids : list
		list telling in which views of the NX CAM setup the PMI can be seen
	type : str
		defines the category of the PMI 
	configuration : dict
		contains the parameters according to the current PMI type

	Methods
	-------
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
	get_faces_and_edges

	"""
	relation_name_single = "PmiId"
	relation_name_plural = "PmiIds"

	def __init__(self,pmi_collection, idx):

		# -- Create IFTGeometryObject data points --
		super().__init__(pmi_collection, idx)
		self.set_data_attributes()

	def get_faces_and_edges(self):
		"""
		Gets and sets faces and edges of IFTPMI object
		"""
		pmi = self.nx_object
		assoc_obj = pmi.GetAssociatedObject()
		pmi_comps = assoc_obj.GetObjects() # components (faces, edges) of pmi
		for comp in pmi_comps:
			if isinstance(comp, NXOpen.Face):  # case: Object is NXOpen.Face
				face = comp 
				if face.IsOccurrence: # case: Object is occurrence
					face = face.Prototype
				self.face_ids.append(face.JournalIdentifier) 
				self.faces.append(face)
			elif isinstance(comp, NXOpen.Edge): # case: Object is NXOpen.Edge
				edge = comp 
				if edge.IsOccurrence: 
					edge = edge.Prototype
				self.edge_ids.append(edge.JournalIdentifier)
				self.edges.append(edge)
			else:
				nx_logger("ERROR", f"Cannot handle geometry object of type {type(obj)}")
	
	def get_data_attributes(self):
		pmi = self.nx_object
		# -- Get general IFTPmi data points --
		if len(pmi.GetDisplayInstances()) == 1:
			pmi_annotation = pmi.GetDisplayInstances()[0]
			self.pmi_annotation = pmi_annotation
			self.type = str(self.pmi_annotation).replace("<class'>","")
		else:
			nx_logger("ERROR", f"PMI {pmi.id} has more than one or no DisplayInstances.")
		
		# -- Get faces and edges --
		self.get_faces_and_edges()
		
		# -- Get Views
		views = pmi_annotation.GetViews()
		for view in views:
			self.view_ids.append(view.JournalIdentifier)

		self.machining_part_id = pmi.OwningPart.JournalIdentifier # Journal Identifier of Owning Part
		self.configuration = dict()  # empty configuration - if there is a configuration specified, it is filled in the section below

		# ==== Get specific information of PMI class ==== 

		# == Surface Finish ==
		if isinstance(pmi_annotation, NXOpen.Annotations.SurfaceFinish):  # case: pmi is specification of surface quality
			tolerance = pmi_annotation.GetTolerance()
			lower_tolerance = tolerance.GetLowerToleranceMm()
			upper_tolerance = tolerance.GetUpperToleranceMm()
			tolerance_type = tolerance.ToleranceType # returns NXOpen.Annotations.ToleranceType
			pmi_annotation.GetInvertSymbol()
			pmi_annotation.GetUnitsFormatPrefs()

			# create builder for surface finish pmi
			builder = pmi.OwningPart.PmiManager.PmiAttributes.CreateSurfaceFinishBuilder(pmi_annotation)
			# it is important to refer to the OwningPart of the pmi, because the workport of a CAM Setup
			# generally does not include pmis

			# enumeration: https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_net/a00809.html#aa74724eb363a92d6822fa6ace3a5b241
			standard_enum = ["ANSI","ISO","JIS","DIN", "ISO 2002", "DIN 2002", "Gb", "Eskd"] # 
			finish_enum = ["Basic", "Modifier", "Modifier, All Around", "Material Removal Required", 
						"Modifier, Material Removal Required", "Modifier, Material Removal Required, All Around",
						"Material Removal Prohibited", "Modifier, Material Removal Prohibited, All Around"]

			self.type = "SurfaceFinish"
			self.configuration = {
				"standard": standard_enum[builder.Standard.value],
				"finishType": finish_enum[builder.Finish.value],
				"A1": builder.A1,
				"A2": builder.A2,
				"C": builder.C, 
				"D": builder.D, 
				"E": builder.E, 
				"F1": builder.F1,
				"F2": builder.F2
			}
			builder.Destroy()

		# == Datum Feature Symbol ==
		elif isinstance(pmi_annotation, NXOpen.Annotations.Datum):
			builder = pmi.OwningPart.Annotations.Datums.CreatePmiDatumFeatureSymbolBuilder(pmi_annotation)
			self._configuration = {"letter": builder.Letter}
			builder.Destroy()

		# == Feature Control Frame == 
		elif isinstance(pmi_annotation, NXOpen.Annotations.Fcf):
			builder = pmi.OwningPart.Annotations.CreatePmiFeatureControlFrameBuilder(pmi_annotation) # class builder: FeatureControlFrameBuilder
			data_builder_list = builder.FeatureControlFrameDataList.GetContents()

			# Enumeration from: https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_net/a00505.html#ac4e9805107eafc75dfcb8588808f20f5
			area_symbol_enum = ["Rectangular", "Circular", "Spherical", "Square"]
			zone_shape_enum = ["no zone shape", "diameter", "spherical diameter", "square"] 
			material_modifier_enum = ["no material modifier", "least material condition", "maximum material condition", "regardless of feature size condition"]

			# Enumeration from: https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_net/a00503.html#a288f00d817db34c87dff91426d3ed3ce
			characteristic_enum = ["straightness", "flatness", "circularity", "cylindricity", "profile of a line", "profile of a surface", "angularity",
								"perpendicularity", "parallelism", "position", "concentricity", "symmetry", "circular runout", "total runout", "axis intersection"]
			data_builder = data_builder_list[0]  # class data_builder: FeatureControlFrameDataBuilder

			if data_builder.MaximumTolerance:
				maximum_tolerance = data_builder.MaximumToleranceValue
			else: 
				maximum_tolerance = None 

			self._configuration = {
				"characteristic": characteristic_enum[builder.Characteristic.value],
				"areaSymbol": area_symbol_enum[data_builder.AreaSymbol.value],
				"materialCondition": material_modifier_enum[data_builder.MaterialModifier.value],
				"toleranceValue": data_builder.ToleranceValue,
				"maximumTolerance": maximum_tolerance,
				"primaryDatumReference": {
					"letter": data_builder.PrimaryDatumReference.Letter,
					" materialCondition": material_modifier_enum[data_builder.PrimaryDatumReference.MaterialCondition.value]
					},
				"primaryDatumReferenceMaterial"
				"zoneShape": zone_shape_enum[data_builder.ZoneShape.value]
			}
			builder.Destroy()

		# == Note ==

		# == Linear == 
		
		# == Radial == 

		# == Angular == 

		# == Hole and Thread Callout == 

		# == Ordinate ==

		# == Chamfer == 

		# == Datum Target == 

		# == Weld Symbol == 

		# == Baloon == 

		# == PMI Class not implemented ==
		else:
			nx_logger("ERROR",  f"Setup for PMI {type(pmi_annotation)} not defined")

	def get_data_dict(self):
		self.data_dict["pmiId"] = self.id 
		self.add_relations_to_data_dict()
		self.data_dict["type"] = self.type
		self.data_dict["configuration"] = self.configuration
		return self.data_dict

	def set_data_attributes(self):
		self.view_ids = list()
		self.type = None 
		self.configuration = None 
		
if __name__ == '__main__':
	print_nx = IFTCore.print_nx
	pmi_collection = IFTPmiCollection()
	for idx in range(pmi_collection.nx_counter):
		ift_pmi = IFTPmi(pmi_collection, idx)
		print_nx(ift_pmi.has_relations)


	#	ift_pmi.get_data_attributes()
	#	print_nx(json.dumps(ift_pmi.get_data_dict(),indent = 2))

	


	'''
	Arten von PMIs (NXOpen.Annotations):
	URL: https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_net/a00321.html 
	Es gibt noch weitere untergruppen
	BaseArrow ..
	BaseFrameBar ..
	CutingPlaneSymbol
	Dimension
	DimensionSet
	DraftingAid
	DraftingImage
	Hatch
	PmiAtriute
	PmiWave
	Region
	TableSection
	TitleBlock
	'''

	'''
	Interessante Methoden und Properties:

	NXOpen.Annotations.Annotations:
		GetViews
		SetViews(NXOpen.View[] modelViews)


	'''