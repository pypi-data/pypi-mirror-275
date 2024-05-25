# nx: threaded
import NXOpen
import NXOpen.CAM
import json
import numpy

from ift-dbms.IFTBase import IFTCore, IFTGeometryObject, IFTGeometryCollection
print_nx = IFTCore.print_nx 
nx_logger = IFTCore.nx_logger 

class IFTMachiningPartCollection(IFTGeometryCollection):

	def __init__(self):
		super().__init__()
		self.workpieces = dict()
		# -- Search for Machining Parts in CAM-Group Collection --
		group_collection = NXOpen.Session.GetSession().Parts.Work.CAMSetup.CAMGroupCollection
		for cam_group in group_collection:
			if isinstance(cam_group, NXOpen.CAM.FeatureGeometry): # cycle through every WORKPIECE
				millGeomBuilder1 = group_collection.CreateMillGeomBuilder(cam_group)
				geometrySetList1 = millGeomBuilder1.PartGeometry.GeometryList
				contents = geometrySetList1.GetContents()
				collector = contents[0].ScCollector
				objects = collector.GetObjects()
				for object in objects:
					part = object.OwningPart
					self.workpieces[part.JournalIdentifier] = cam_group
					self.nx_objects[self.nx_counter] = part
					self.nx_counter +=1
				millGeomBuilder1.Destroy()

class IFTMachiningPart(IFTGeometryObject):
	'''
	This class represents the machined parts of the cam setup. These are the parts that are actually 
	manufactured. 
	'''

	relation_name_single = "machiningPartId"
	relation_name_plural = "machiningPartIds"
	
	def __init__(self,ift_machining_part_collection, idx):

		# -- Create IFTGeometryObject data points -- 
		super().__init__(ift_machining_part_collection, idx)
		self.workpieces = ift_machining_part_collection.workpieces

	def get_data_attributes(self):
		self.get_faces()
		self.get_blank()

	def get_faces(self):
		"""Get faces of the machining part"""
		part_features = list(self.nx_object.Features)
		for i in part_features:
			try:
				faces = list(i.GetFaces())
				for face in faces:
					self.faces.append(face)
					self.face_ids.append(face.JournalIdentifier)
			except:
				pass

	def get_data_dict(self):
		'''
		Returns the dictionary containing all the data for the export to the MongoDB
		'''
		self.data_dict["machiningPartId"] = self.id
		self.data_dict["material"] = self.material 
		self.data_dict["materialName"] = self.material_name 
		self.data_dict["materialHardness"] = self.hardness 
		self.data_dict["blankGeometryType"] = self.blank_geometry_type 
		self.data_dict["blankBlockHeight"] = self.blank_block_height
		self.data_dict["blankBlockLength"] = self.blank_block_length
		self.data_dict["blankBlockWidth"] = self.blank_block_width
		self.data_dict["blankCylinderHeight"] = self.blank_cylinder_height 
		self.data_dict["blankCylinderDiameter"] = self.blank_cylinder_diameter 
		self.data_dict["blankPartName"] = self.blank_part_name 
		return self.data_dict 
	
	def get_geometry(self):
		'''
		Gets the geometry of the machining part 
		'''
		point_list = list()
		#print_nx(machining_part.get_dict())
		#print_nx(json.dumps(machining_part.get_dict(), indent = 2))
		part = self._nx_object
		bodies = list(part.Bodies)
		for body in bodies:
			user_attributes = body.GetUserAttributes()
			for attribute in user_attributes:
				print_nx(f"{attribute.Title}: {attribute.StringValue}")
			edges = body.GetEdges()
			for edge in edges:
				#edge.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)	
				if edge.SolidEdgeType.value == 1:
					p1, p2 = edge.GetVertices()
					if p1 not in point_list:
						point_list.append(p1)
					if p2 not in point_list:
						point_list.append(p2)
		
		# Get values for coordinate transformation 
		offset, rot_matrix = self.get_assembly_position()

	def get_assembly_position(self):
		part = self._nx_object
		root_comp = IFTCore.nx_work_part.ComponentAssembly.RootComponent #.FindObject(part.JournalIdentifier)
		children = root_comp.GetChildren()
		for child in children:
			if part.JournalIdentifier == child.Prototype.JournalIdentifier:
				[offset, rot_matrix] = child.GetPosition()
		return offset, rot_matrix

	def get_blank(self):
		"""Gets the blank of the machining part. Right now there are three different geometry types that
		the blank can have - cuboid, cylinder, fromPart. From part means that the blank in Siemens NX is defined 
		by another .prt data. This may happen, when the work step is not the first one. For some configuration 
		options this function still does not work and needs more implementation."""
		
		cam_setup = NXOpen.Session.GetSession().Parts.Work.CAMSetup
		group_collection = cam_setup.CAMGroupCollection
		machining_part = self.nx_object 
		mill_geom_builder = group_collection.CreateMillGeomBuilder(self.workpieces[self.id])
		material_data = mill_geom_builder.GetMaterialData()
		self.material = material_data[0]
		self.material_name = material_data[1]
		if material_data[-1]:
			self.hardness = material_data[-1]
		definition_type = mill_geom_builder.BlankGeometry.BlankDefinitionType
		block_height = round(mill_geom_builder.BlankGeometry.BlockHeight,3)
		block_length = round(mill_geom_builder.BlankGeometry.BlockLength,3)
		block_width = round(mill_geom_builder.BlankGeometry.BlockWidth,3)

		cylinder_diameter = round(mill_geom_builder.BlankGeometry.CylinderDiameter,3)
		cylinder_height = round(mill_geom_builder.BlankGeometry.CylinderHeight,3)
		

		if definition_type == NXOpen.CAM.GeometryGroup.BlankDefinitionTypes.FromGeometry:
			self.blank_geometry_type = "fromPart"
			geometry_list = mill_geom_builder.BlankGeometry.GeometryList
			object_list = geometry_list.GetContents()
			for object in object_list:
				items = object.GetItems()
				if items:
					if items[0].IsOccurrence:
						self.blank_part_name = items[0].Prototype.OwningPart.Name # get name of owning part 
						faces = items[0].GetFaces()
						number_faces = len(faces) 
						features = items[0].GetFeatures()
						for face in faces:
							facet = face.GetNumberOfFacets
						if number_faces == 6:  # this means that the owning part is also a block
							# the idea was that if I know the part has 6 faces, then it we also have a cuboid,
							# but in special cases that would not be true
							pass
		elif definition_type == NXOpen.CAM.GeometryGroup.BlankDefinitionTypes.OffsetFromPart:
			nx_logger("ERROR", "Blank definition Type 'OffsetFromPart' not implemented")
		elif definition_type == NXOpen.CAM.GeometryGroup.BlankDefinitionTypes.AutoBlock:
			self.blank_block_width = block_width
			self.blank_block_length = block_length
			self.blank_block_height = block_height
			self.blank_geometry_type =  "cuboid"
		elif definition_type == NXOpen.CAM.GeometryGroup.BlankDefinitionTypes.Ipw:
			nx_logger("ERROR", "Blank definition Type 'IPW' not implemented")
		elif definition_type == NXOpen.CAM.GeometryGroup.BlankDefinitionTypes.BoundingCylinder:
			self.blank_cylinder_height = cylinder_height
			self.blank_cylinder_diameter = cylinder_diameter
			self.blank_geometry_type = "cylinder"
		elif definition_type == NXOpen.CAM.GeometryGroup.BlankDefinitionTypes.PartConvexHull:
			nx_logger("ERROR", "Blank definition Type 'PartConvexHull' not implemented")
		elif definition_type == NXOpen.CAM.GeometryGroup.BlankDefinitionTypes.PartOutline:
			nx_logger("ERROR", "Blank definition Type 'PartOutline' not implemented")	
		mill_geom_builder.Destroy()

	def set_data_attributes(self):
		self.material = None 
		self.material_name = None 
		self.hardness = None 
		self.blank_geometry_type = None 
		self.blank_part_name = None 
		self.blank_block_width = None 
		self.blank_block_height = None 
		self.blank_block_length = None 
		self.blank_cylinder_height = None 
		self.blank_cylinder_diameter = None 

if __name__ == '__main__':
	print_nx = IFTCore.print_nx
	collection = IFTMachiningPartCollection()
	for i in range(collection.nx_counter):
		part = IFTMachiningPart(collection,i)
		part.get_data_attributes()
		print_nx(json.dumps(part.get_data_dict(),indent = 2))


	
			









