# nx: threaded
import json
import sys
import os
import math
import numpy 
import statistics
from time import time
import csv 
import NXOpen
import NXOpen.CAM
import NXOpen.UF
from inspect import currentframe, getframeinfo

from ift-dbms.IFTBase import IFTCore, IFTObject, IFTGeometryObject
from ift-dbms.IFTBase import IFTGeometryCollection
#from IFT.IFTIpw import IFTIpw
from ift-dbms.IFTTool import IFTToolCollection, IFTTool
print_nx = IFTCore.print_nx
nx_logger = IFTCore.nx_logger
import traceback


class IFTOperationCollection(IFTGeometryCollection):
	"""
	Class that contains the Operation Objects of the Siemens NX session. 
	"""
	def __init__(self):
		super().__init__()
		self.parents = list()
		for operation in NXOpen.Session.GetSession().Parts.Work.CAMSetup.CAMOperationCollection:
			self.nx_objects[self.nx_counter] = operation  # all operation objects from nx
			self.nx_counter +=1


class IFTOperation(IFTGeometryObject):
	'''
	This class generates all data points of the Operations. First Data which is available for all kinds of
	operations is generated. Later more specific data is retrieved by getting the certain OperationBuilders
	'''

	relation_name_single = "operationId"
	relation_name_plural = "operationsId"
	
	def __init__(self, ift_operations, idx, ipw = None, store_data = False):

			super().__init__(ift_operations, idx)
			self.set_data_attributes()
			self.store_data = store_data # this is just for debugging purposes and can be ignored
			self.ipw = ipw 
			self.ift_operations = ift_operations
			self.find_machining_feature()
					
	def get_data_attributes(self):
		operation = self.nx_object

		# -- Generate or actualize toolpath if necessary
		self.generate_toolpath()

		# -- Create relation data points -- 
		self.work_piece_id = NXOpen.Session.GetSession().Parts.Work.JournalIdentifier 
		self.machining_feature_id = None  # this value is set in the main file with IFTCore.match_by_faces()
		self.tool_id = operation.GetParent(NXOpen.CAM.CAMSetup.View.MachineTool).JournalIdentifier

		# -- Create general IFTOperation data points -- 
		self.method = self.get_operation_method()
		self.type = str(type(operation)).strip("<class '>'")  # type of operation
		self.cutting_length = round(operation.GetToolpathCuttingLength(),3)  # unit: [mm]
		self.cutting_time = round(operation.GetToolpathCuttingTime(),3)  # unit: [min]
		self.toolpath_length = round(operation.GetToolpathLength(),3)  # unit [mm]
		self.toolpath_time = round(operation.GetToolpathTime(),3)  # unit [mm]

		# -- Get toolpath information -- 
		try:
			self.toolpath = IFTToolpath(self.nx_object) 
			self.toolpath.get_toolpath_volume()
		except Exception as e:
			nx_logger("ERROR", f"Toolpath info for operation {self.id} could not be generated.")
	
		# -- Get operation type --
		self.get_operation_type()

		# ==== Getting data of the different OperationBuilder ====
		operation_builder = self.get_operation_builder()
		# Overview over Operations on https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_net/a03120.html

		# == Data that can be retreived from every operation builder ==
		# Was first ment to get the information of cooling, but is not necessary any more,
		# however, maybe you can find other interesting data from the UDEs
		#if isinstance(operation_builder, NXOpen.CAM.OperationBuilder):
			#self.get_ude(operation_builder)

		# == Data for Mill Operations ==
		if isinstance(operation_builder, NXOpen.CAM.MillOperationBuilder): 
			self.get_mill_operation_data(operation_builder, self.ift_operations)
								
		# # == Data for HoleMachiningBuilder ==
		elif isinstance(operation_builder, NXOpen.CAM.HoleMachiningBuilder):
			self.get_hole_machining_operation_data(operation_builder, self.ift_operations)

		# # == None of the above cases ==
		else:
			nx_logger("ERROR", f"Information for OperationBuilder {type(operation_builder)} not implemented")
		#-- Destroy operation builder if exists --
		try:
			operation_builder.Destroy()
		except:
			pass

	def find_machining_feature(self):
		'''
		If an operation was generated in the Machining Feature Navigator by selecting the feature 
		and create feature process, the machining feature already is available and shouldn't be found
		by comporing the facesa belonging to the operation. This function checks if there is already
		a machining feature available for this operation and adds the machining feature id to the
		operation.
		'''
		operation = self.nx_object
		cam_features = list(NXOpen.Session.GetSession().Parts.Work.CAMFeatures)
		for cam_feature in cam_features:
			operations_list = cam_feature.GetOperations()
			for i in operations_list:
				if i.JournalIdentifier == operation.JournalIdentifier:
					self.nx_machining_feature = cam_feature 
					self.machining_feature_id = cam_feature.JournalIdentifier
					self.foreign_ids_dict = {"machiningFeatureIds": [cam_feature.JournalIdentifier]}
					self.has_relations = True

	def get_data_dict(self):
		'''
		Returns the dictionary which is later used to store the data in the MongoDB.
		'''

		self.data_dict["operationId"] = self.id
		self.data_dict["toolId"] = self.tool_id 
		self.add_relations_to_data_dict()
		self.data_dict["operationType"] = self.operation_type
		self.data_dict["operationSubtype"] = self.operation_subtype
		self.data_dict["operationMethod"] = self.method
		self.data_dict["materialRemoval"] = self.material_removal
		self.data_dict["meanMaterialRemovalRate"] = self.mean_material_removal_rate
		self.data_dict["feedRate"] = self.feed_rate
		self.data_dict["floorStock"] = self.floor_stock
		self.data_dict["wallStock"] = self.wall_stock
		self.data_dict["spindleSpeed"] = self.spindle_speed
		self.data_dict["axialCuttingDepth"] = self.axial_cutting_depth
		self.data_dict["radialCuttingDepth"] = self.radial_cutting_depth
		self.data_dict["coolantTypeOpen"] = self.coolant_type_open
		self.data_dict["coolantTypeClosed"] = self.coolant_type_closed
		self.data_dict["cuttingLength"] = self.cutting_length
		self.data_dict["cuttingTime"] = float(self.cutting_time)*60
		self.data_dict["toolpathLength"] = self.toolpath_length
		self.data_dict["toolpathTime"] = float(self.toolpath_time)*60
		self.data_dict["drillingCycleDepth"] = self.drilling_cycle_depths
		return self.data_dict
	
	def get_faces(self, operation_builder):
		"""
		Gets the faces of the operation

		Sets:
		- IFT.Operation.faces:list
		- IFT-Operation.face_ids:list
		"""

		# -- Get floor faces of operation -- 
		cut_area_geometry = operation_builder.CutAreaGeometry
		geometry_set_list = cut_area_geometry.GeometryList
		contents = geometry_set_list.GetContents()
		sc_collector = contents[0].ScCollector
		faces = sc_collector.GetObjects()
		for face in faces:
			if face.IsOccurrence:
				face = face.Prototype
			self.floor_faces.append(face.JournalIdentifier)
			self.faces.append(face)
			self.face_ids.append(face.JournalIdentifier)
		# -- Get wall faces of operation -- 
		wall_area_geometry = operation_builder.WallGeometry
		geometry_set_list = wall_area_geometry.GeometryList 
		contents = geometry_set_list.GetContents()
		sc_collector = contents[0].ScCollector
		faces = sc_collector.GetObjects()
		for face in faces:
			if face.IsOccurrence:
				face = face.Prototype
			self.wall_faces.append(face.JournalIdentifier)
			self.faces.append(face)
			self.face_ids.append(face.JournalIdentifier)
		pass
	
	def get_hole_machining_operation_data(self, operation_builder, ift_operations):
		'''
		Get the data of hole_machining operations. An overview of all hole machining builders can be found
		here: https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_net/a02899.html
		'''
		self.surface_speed = operation_builder.FeedsBuilder.SurfaceSpeedBuilder.Value
		self.feed_per_tooth = operation_builder.FeedsBuilder.FeedPerToothBuilder.Value
		self.spindle_speed = operation_builder.FeedsBuilder.SpindleRpmBuilder.Value
		self.feed_rate = operation_builder.FeedsBuilder.FeedCutBuilder.Value
		feed_rate_unit_enum = ["none", "per minute", "per revolution", "rapid", "cut percent"]
		self.feed_rate_unit = feed_rate_unit_enum[operation_builder.FeedsBuilder.FeedCutBuilder.Unit.value]

		# == Data for drilling builder ==
		if isinstance(operation_builder, NXOpen.CAM.HoleDrillingBuilder):

			# Getting the depth of the drilling operation
			# stepover_type_enum = ["None","Constant","Scallop","PercentToolFlat","Multiple","Number","Maximum","Angular","VariableAverage"
			# 					"VariableMaximum","UseCutDepth","PercentRemaining","PercentWire","StockPerPass","PercentThreadLength","Exact",
			# 					"PercentFluteLength","BlankContourConstant","Degression","PercentDegression","UserDefined"]
			# stepover_type = stepover_type_enum[operation_builder.CycleTable.AxialStepover.StepoverType.value]

			# In this case the length of the cutting path of the drilling operation is the depth
			self.drilling_cycle_depths = list()
			for cut in self.toolpath.cuts:
				self.drilling_cycle_depths.append(round(cut['length'],3))

			# -- Get the drilling cycle depths --
			self.get_drill_removal_rate(ift_operations)
			
		else:
			nx_logger("ERROR",f"Data extraction for {type(operation_builder)} not implemented.")

	def get_drill_removal_rate(self, ift_operation_collection):
		"""
		Drilling operations unfortunately don't provide the material removal rate options, which it has to be extracted manually here.-
		"""	
		tool_diameter = self.toolpath.tool_diameter
		feed_rate = self.feed_rate 
		hole_deepness = sum(self.drilling_cycle_depths)

		# -- checking if prior drill operation with same feature -- 

		for operation in ift_operation_collection.ift_objects.values():
			is_same_feature = operation.machining_feature_id == self.machining_feature_id 
			is_same_operation = operation.id == self.id 
			if (is_same_feature and not is_same_operation):
				is_enlarging = True 
				prior_diameter = operation.toolpath.tool_diameter 
			else: 
				is_enlarging = False 
		

		# the material removal rate is the feed_rate in mm/s multiplied by the tool diameter if the drilling operation is
		# drilling into solid
		if is_enlarging: 
			drilling_area = (tool_diameter**2-prior_diameter**2)*math.pi/4
			self.operation_subtype = "enlarging"
		else:
			drilling_area = tool_diameter**2*math.pi/4
			self.operation_subtype = "solidDrilling"

		mrr = round(drilling_area * feed_rate/60, 3)
		mr = round(hole_deepness * drilling_area,3)
		
		self.mean_material_removal_rate = mrr 	
		self.material_removal = mr

	def get_mill_operation_data(self, operation_builder, ift_operations):
		'''
		Gets the data for mill operations. The mill operation class contains a bunch of operations,
		which is why in this function there are further checks of subclasses
		'''
		self.material_removal, self.mean_material_removal_rate = IFTOperation.calc_material_removal(self.nx_object)

		self.surface_speed = round(operation_builder.FeedsBuilder.SurfaceSpeedBuilder.Value,3)
		self.feed_per_tooth = round(operation_builder.FeedsBuilder.FeedPerToothBuilder.Value,3)
		self.spindle_speed = round(operation_builder.FeedsBuilder.SpindleRpmBuilder.Value,3)
		self.feed_rate = round(operation_builder.FeedsBuilder.FeedCutBuilder.Value,3)
		feedrate_unit_enum = ["none", "per minute", "per revolution", "rapid", "cut percent"]
		self.feed_rate_unit = feedrate_unit_enum[operation_builder.FeedsBuilder.FeedCutBuilder.Unit.value]

		cut_parameters = operation_builder.CutParameters
		self.floor_stock = round(cut_parameters.FloorStock.Value,3)
		self.part_stock = round(cut_parameters.PartStock.Value,3)
		self.wall_stock = round(cut_parameters.WallStock.Value,3) 
	
		# coolant_type_enum = ["Off","Flood","Thru","Mist","Air","Air Thru"]
		# open_region_builder = operation_builder.GetCustomizableItemBuilder("Open Region Context:")
		# open_region_builder_info = open_region_builder.GetCustomizableItemBuilder("Coolant Type")
		# self.coolant_type_open = coolant_type_enum[open_region_builder_info.Value]

		# closed_region_builder = operation_builder.GetCustomizableItemBuilder("Closed Region Context:")
		# closed_region_builder_info = closed_region_builder.GetCustomizableItemBuilder("Coolant Type")
		# self.coolant_type_closed = coolant_type_enum[closed_region_builder_info.Value]

		# -- Data for PlanarOperations -- 
		if isinstance(operation_builder, NXOpen.CAM.FaceMillingBuilder):
			self.get_face_milling_operation_data(operation_builder, ift_operations)
		elif isinstance(operation_builder, NXOpen.CAM.SurfaceContourBuilder):
			self.get_face_milling_operation_data(operation_builder, ift_operations)

		# -- None of the above cases --
		else:
			nx_logger("ERROR",f"Data extraction for {type(operation_builder)} not implemented")

	def get_operation_type(self):
		'''
		Gets operation type (milling, drilling, etc.)
		'''
		if isinstance(self.nx_object,(NXOpen.CAM.HoleMaking, NXOpen.CAM.HoleDrilling)):
			self.operation_type = "drilling"
		elif isinstance(self.nx_object, (NXOpen.CAM.MillOperation, NXOpen.CAM.ChamferMilling, NXOpen.CAM.CylinderMilling, 
										NXOpen.CAM.ThreadMilling, NXOpen.CAM.RadialGrooveMilling, NXOpen.CAM.SurfaceContour)):
			self.operation_type = "milling"
		else:
			nx_logger("ERROR", f"Could not get operation category for {self.nx_object.Journalidentifier}")
	
	@staticmethod
	def get_wall_and_floor_faces(operation):
		operation_builder = operation.get_operation_builder()
		floor_faces = {}
		wall_faces = {}
		# -- Get Floor Faces -- 
		floor_area_geometry = operation_builder.CutAreaGeometry
		geometry_set_list = floor_area_geometry.GeometryList
		contents = geometry_set_list.GetContents()
		sc_collector = contents[0].ScCollector
		faces = sc_collector.GetObjects()
		for face in faces:
			if face.IsOccurrence:
				face = face.Prototype
			floor_faces[face.JournalIdentifier] = face


		# -- Get Wall Faces -- 
		wall_area_geometry = operation_builder.WallGeometry
		geometry_set_list = wall_area_geometry.GeometryList 
		contents = geometry_set_list.GetContents()
		sc_collector = contents[0].ScCollector
		faces = sc_collector.GetObjects()
		for face in faces:
			if face.IsOccurrence:
				face = face.Prototype
			wall_faces[face.JournalIdentifier] = face
		operation_builder.Destroy()
		return wall_faces, floor_faces
		
	def get_operation_method(self):
		operation_method = self.nx_object.GetParent(NXOpen.CAM.CAMSetup.View.MachineMethod).JournalIdentifier
		if operation_method == "MILL_ROUGH":
			method = "rough"
		elif operation_method == "MILL_FINISH":
			method = "finish"
		elif operation_method == "DRILL_METHOD":
			method = None 
		else:
			nx_logger("Error",f"Operation Method {operation_method} not known")
		return method 
	
	def get_face_milling_operation_data(self, operation_builder, ift_operations):
		if not (self.wall_faces or self.floor_faces):
			self.get_faces(operation_builder)
		
		# -- Get milling subtype according to DIN 8589-3 -- 
		if (self.wall_faces and self.floor_faces):
			self.operation_subtype = "sideMilling"
		elif (self.wall_faces and not self.floor_faces):
			self.operation_subtype = "plainMilling"
		elif (self.floor_faces and not self.wall_faces):
			self.operation_subtype = "faceMilling"

		# -- Get data of configuration --
		# Stock values
		try:			
			use_floor_as_part = int(operation_builder.GetCustomizableItemBuilder("Use Final Floor Stock Same As Part").Value)
		except:
			nx_logger("INFO", "use_floor_as_part not available")
			use_floor_as_part = 0
		try:
			use_wall_as_part = int(operation_builder.GetCustomizableItemBuilder("Use Wall Stock Same As Part").Value)
		except:
			nx_logger("INFO", "use_wall_as_part not available")
			use_wall_as_part = 0

		try:
			self.floor_stock = self.part_stock if use_floor_as_part else self.floor_stock # use the value as configured
		except:
			nx_logger("ERROR", "floor_stock not available")
		try:
			if len(self.wall_faces) > 0: # operation has wall face
				self.wall_stock = self.part_stock if use_wall_as_part else self.wall_stock # use the value as configured
			else: # operation has no wall face and wall_stock makes no sense:
				self.wall_stock = None 
		except:
			nx_logger("ERROR", "wall_stock not available")


		# Check if there was already an operation on the floor face and wall face 
		wall_allowance = None
		floor_allowance = None 

		for foreign_ift_operation in ift_operations.ift_objects.values(): # loop through all operations in CAM-Setup
			foreign_operation = foreign_ift_operation.nx_object
			foreign_wall_faces, foreign_floor_faces = self.get_wall_and_floor_faces(foreign_ift_operation)	
			foreign_wall_ids = list(foreign_wall_faces.keys())
			foreign_floor_ids = list(foreign_floor_faces.keys())
			
			# nx_logger("self.floor_faces[0]", self.floor_faces[0])
			# nx_logger("foreign_floor_ids", foreign_floor_ids)
			# nx_logger("self.id", self.id)
			# nx_logger("JournalIdentifier", foreign_operation.JournalIdentifier)

			if (self.floor_faces[0] in foreign_floor_ids and self.id != foreign_operation.JournalIdentifier): 
				prior_operation = foreign_ift_operation
				if self.floor_faces[0] in foreign_floor_ids:
					floor_allowance = prior_operation.floor_stock
				else:
					floor_allowance = prior_operation.wall_stock

				# check wall face 
				has_wall_face = len(self.wall_faces) > 0 # bool: True if there is a wallface in the operation
				if has_wall_face:
					if (self.wall_faces[0] in foreign_floor_ids and self.id != foreign_operation.JournalIdentifier): 
						prior_operation = foreign_operation
						if self.wall_faces[0] in foreign_floor_ids:
							wall_allowance = prior_operation.floor_stock
						else:
							wall_allowance = prior_operation.wall_stock	
		

		has_multiple_layers = self.toolpath.number_layers > 1 # bool: True if there are multiple cutting levels
		number_cuts_per_layer = self.toolpath.number_cuts_per_layer
		has_multiple_cuts_per_layer = number_cuts_per_layer > 1
		

		# ===== Get cutting depth values for first layer =====		
		intersection_info = self.get_intersection_of_toolpath_and_ipw()
		first_layer = intersection_info[0] # info of first layer of cut
		for layer_number, cuts in intersection_info.items():
			if layer_number == 0:
				axial_cutting_depth = 0
				radial_cutting_depth = 0
				for cut in cuts:
					
					#acd = None # axial cutting depth
					#acc = None # acial cutting contact
					#rcd = None # radial cutting contact
					#rcc = None # radial cutting depth

					# == Contact lengths (this is equal for every cut) == 
					points_2d_intersect = cut["points_intersect"] # the intersecting points and points in toolpath volume
					points_2d_inside = cut["points_inside"] # only points within the toolpath volume
					points_2d = points_2d_intersect + points_2d_inside # combination of both

					#tol = 10**-3 # tolerance
					# description of used indices in the following lines: is = intersect, in = inside
					#print_nx(f"Points 2D: {points_2d}") # todo: delete 
					min_x = min(points_2d, key = lambda i : i[0])[0]
					max_x = max(points_2d, key = lambda i : i[0])[0]
					max_y = max(points_2d, key = lambda i : i[1])[1]
					min_y = min(points_2d, key = lambda i : i[1])[1]

					if abs(min_x - max_x) > radial_cutting_depth:
						radial_cutting_depth = abs(min_x - max_x)
					if abs(min_y - max_y) > axial_cutting_depth:
						axial_cutting_depth = abs(min_y - max_y)
				
				# depending on if its a facemilling or endmilling operation another value is stored
				self.radial_cutting_depth = radial_cutting_depth
				if has_multiple_layers: # axial cutting depth is defined by the operation builder
					self.axial_cutting_depth = round(operation_builder.DepthPerCut.Value,3)
				else: # take the value from the PMI
					self.axial_cutting_depth = axial_cutting_depth

		if self.store_data: # set true if you want to get points that can be plotted in scripts/plots_2d_points.py
			if IFTCore.storage_dir:
				target_dir = IFTCore.storage_dir
			else:
				path = os.path.dirname(__file__)
				target_dir = os.path.join(path, "build")
			counter = 0
			for i in first_layer:
				with open(target_dir + f"\\cut_number_{counter}.csv","w", newline = "") as f:
					spamwriter = csv.writer(f, delimiter=';')	
					counter +=1	
					all_intersect_points = i["points_intersect"]	
					all_inside_points = i["points_inside"]
					all_points = all_intersect_points + all_inside_points
					for point in all_points:
						spamwriter.writerow([point[0], point[1]])
				f.close()
			
	def get_operation_builder(self):
		'''
		This function finds the correct operation builder for the operation. The operation builder is more
		or less the menu, that you get when you create the operation. From here you can get the information 
		of how the user set up the operation and defined the paremeters.
		An inheritance diagram of the operation builder is available on 
		https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_net/a03053.html
		'''
		number_used_builder = 0  # to check if operation used various builder, because sometimes inherited operations are
		# also instances of another class.
		operation = self.nx_object
		# print_nx("operation:")
		# print_nx(operation)
		operation_collection = NXOpen.Session.GetSession().Parts.Work.CAMSetup.CAMOperationCollection
		
		# -- Creating the correct builder for NXOpen.CAM.MilOperation operation -- 
		if isinstance(operation, NXOpen.CAM.CavityMilling):  # operation -> mill_contour -> Cavity Mill
			operation_builder = operation_collection.CreateCavityMillingBuilder(operation)
			number_used_builder += 1
		elif isinstance(operation, NXOpen.CAM.FaceMilling):  
			operation_builder = operation_collection.CreateFaceMillingBuilder(operation)
			number_used_builder += 1
		elif isinstance(operation, NXOpen.CAM.SurfaceContour):  
			operation_builder = operation_collection.CreateSurfaceContourBuilder(operation)
			number_used_builder += 1
		elif isinstance(operation, NXOpen.CAM.FeatureMilling):
			nx_logger("ERROR", f"Setup for Operation {type(operation)} not defined")
			number_used_builder += 1
			operation_builder = None
		elif isinstance(operation, NXOpen.CAM.PlanarMilling):
			nx_logger("ERROR" f"Setup for Operation {type(operation)} not defined")
			number_used_builder += 1
			operation_builder = None
		elif isinstance(operation, NXOpen.CAM.PlungeMilling):
			nx_logger("ERROR" f"Setup for Operation {type(operation)} not defined")
			number_used_builder += 1
			operation_builder = None
		elif isinstance(operation, NXOpen.CAM.VariableZLevelMilling):
			nx_logger("ERROR" f"Setup for Operation {type(operation)} not defined")
			number_used_builder += 1
			operation_builder = None
		elif isinstance(operation, NXOpen.CAM.ZLevelMilling):
			nx_logger("ERROR" f"Setup for Operation {type(operation)} not defined")
			number_used_builder += 1
			operation_builder = None

		# -- Creating the correct builder for NXOpen.CylinderMilling operation 
		elif isinstance(operation, NXOpen.CAM.CylinderMilling):
			number_used_builder +=1
			operation_builder = operation_collection.CreateCylinderMillingBuilder(operation)


		# -- Creating the correct  builder for NXOpen.ChamferMilling operation --
		elif isinstance(operation, NXOpen.CAM.ChamferMilling):
			nx_logger("ERROR" f"Setup for Operation {type(operation)} not defined")
			number_used_builder += 1
			operation_builder = None

		# -- Creating the correct builder for NXOpen.CAM.HoleDrilling operation --
		elif isinstance(operation, NXOpen.CAM.HoleDrilling):
			operation_builder = operation_collection.CreateHoleDrillingBuilder(operation)
			number_used_builder += 1

		# -- Creating the correct builder for NXOpen.CAM.HoleMaking operation --
		elif isinstance(operation, NXOpen.CAM.HoleMaking):
			nx_logger("ERROR" f"Setup for Operation {type(operation)} not defined")
			number_used_builder += 1
			operation_builder = None

		# -- No Builder for this operation defined --	
		else:
			nx_logger("ERROR" f"Setup for Operation {type(operation)} not defined")
			operation_builder = None  # no operation builder exists
			
		if number_used_builder > 1:
			# If so, check the inheritance diagram and change the code, so that the operation builder
			# is unambigously defined
			nx_logger("ERROR", f"Operation type {type(operation)} has ambigious builder")

		return operation_builder
	
	def generate_toolpath(self):
		'''
		Checks if the toolpath exists and up-to-date. And generates or actualizes it if
		necessary. 
		'''
		operation = self.nx_object
		cam_setup = NXOpen.Session.GetSession().Parts.Work.CAMSetup
		# -- Check if toolpath exists --
		if not operation.AskPathExists():  # no toolpath existing
			nx_logger("ERROR", f"Operation {operation.Name} has no tool path" )
			obj = [NXOpen.CAM.CAMObject.Null] * 1
			obj[0] = operation
			cam_setup.GenerateToolPath(obj)
			nx_logger("INFO", f"toolpath for {operation.Name} was generated")
		else:
			toolpath_status = operation.GetStatus().value
			if int(toolpath_status) == 0:  # Object path has been output
				pass 
			elif int(toolpath_status) == 1:  # Object path must be post-processed
				nx_logger("WARNING", f"Operation toolpath for {operation.Name} must be post processed")
			elif int(toolpath_status) == 2:  # Object path must be regenerated
				obj = [NXOpen.CAM.CAMObject.Null] * 1
				obj[0] = operation 
				cam_setup.GenerateToolPath(obj)
				nx_logger("INFO",f"Operation toolpath for {operation.Name} was generated")
				nx_logger("WARNING", f"Operation toolpath for {operation.Name} must be post processed")

			elif int(toolpath_status) == 4:  # Object path has been approved as is 
				pass 
	
	def get_ude(self, operation_builder):
		'''
		Gets the user defined events of an operation. This includes events like turning on and turning off
		cooling of the machine. There are several possible UDEs (user defined events). Right now this 
		function only checks if the coolant is active
		'''
		ude_start_list = operation_builder.StartUdeSet.UdeList.GetContents()
		for ude in ude_start_list:
			for i in range(ude.NumberOfParameters):
				parameter = ude.GetParameter(i)
				# Set isCoolantActive as active if there is a active coolant mode
				if parameter.NameOfParameter == "coolant_mode":
					if parameter.ParameterActive:
						self.is_coolant_active = True 

	def get_intersection_of_toolpath_and_ipw(self):
		'''
		Gets all the locations where an edge of the IPW intersects with the toolpath volume and 
		calculates the distances from the floor face and left and right face with respect to the 
		cutting direction of every linear cutting motion as well as the describing line of the.
		To check the level of the motion there is also the level given.		

		Input: IFTOperation
		Output: dict
			{"cut0": {"path": IFTEdge, "tool_diameter": int "level": int, "floor": [], "left": [], "right": []}, ..., "cutX": ...}}
		'''
		if not self.has_intersection_points: # only calculate if not already done
			# Get the toolpath and the radius of the tool
			toolpath = self.toolpath

			# Get all ipw edges 
			ift_ipw = self.get_ipw_edges(toolpath, filter_type = 1, filter_length = 0.2)

			event_counter = -1
			#for cutting_event, toolpath_faces in zip(cutting_event_info, toolpath_faces_list):
			intersection_points = list()
			intersection_edges = list()
			result = dict()
			for cut in toolpath.cuts:
				event_counter +=1
				toolpath_faces = cut['faces']
				level = cut['level'] # level of the cutting motion
				if level not in result.keys():
					result[level] = [] # add list for cuts of new level
				start_point = cut['start_point'] # coordinate where cut motion starts
				end_point = cut['end_point'] # coordinate where cutr motion ends
				path = IFTEdge(start_point, end_point) # describing line of the motion 
				intersection_points = ift_ipw.cut_ipw(cut) 
				points_in_toolpath = ift_ipw.get_points_in_toolpath_volume(cut)
				
				#try:
				# Get the equations for the relevant planes
				bottom_plane = cut['faces'][8] # bottom plane
				right_plane = cut['faces'][0] # right plane
		
				# -- INTERSECTING POINTS --
				points_2d = list() # unique list of points intersecting the face of the toolpath
				for ip in intersection_points: # using the plane equation to calculate the absolute distances
					floor_distance = round(abs(bottom_plane.calc_point_distance(ip)),3)
					right_distance = round(abs(right_plane.calc_point_distance(ip)),3)
					point_2d = (right_distance, floor_distance)
					if point_2d not in points_2d:
						points_2d.append(point_2d)

				# -- POINTS WITHIN TOOLPATH --
				points_2d_inside = list() # unique list of points inside the toolpath
				for ip in points_in_toolpath:
					floor_distance = round(abs(bottom_plane.calc_point_distance(ip)),3)
					right_distance = round(abs(right_plane.calc_point_distance(ip)),3)
					point_2d = (right_distance, floor_distance)
					if point_2d not in points_2d_inside:
						points_2d_inside.append(point_2d)


				# add entry to existing level 
				result[level].append({"path":path, "event_number": event_counter, "tool_diameter": toolpath.tool_diameter,  
											"points_intersect":points_2d, "points_inside": points_2d_inside})
	
				#Store data into csv files in the build folder --> only if you want to plot and verify
				if self.store_data:
					points_of_interest = points_in_toolpath + intersection_points 
					self.store_ipw_points(ift_ipw.edges.values(), toolpath_faces, points_of_interest, event_counter)

			self.intersection_info = result 
			self.has_intersection_points = True
			return result
		else:
			return self.intersection_info
			
	def store_ipw_points(self, ipw_edges, toolpath_faces, points_of_interest, event_counter):
			''' 
			Store the data of the points 
			If more than one operation is executed, the last store data will be overridden.
			This should just help to plot the data. Unfortunaetly the matplotlib package does not work for me,
			due to an incompability of the tlc version.
			The data can then be plotted from outside NX with the package module plot_toolpath.py
			'''			
			target_dir = "C:\\repos\\IFTApi\\src\\IFT\\build\\"
			# Save all ipw points to csv
			with open(target_dir + f"\\points_of_ipw_{event_counter}.csv","w",newline='') as file:
				spamwriter = csv.writer(file, delimiter=';')
				edge_number = 0
				for edge in ipw_edges:	
					p0 = edge.points[0]
					p1 = edge.points[1]
					spamwriter.writerow([p0.x, p0.y, p0.z,[edge_number]])
					spamwriter.writerow([p1.x, p1.y, p1.z,[edge_number]])
					edge_number +=1
			file.close()

			# Save all toolpath points to csv 
			try:
				with open(target_dir + f"\\toolpath_points_{event_counter}.csv","w",newline='') as file:
					spamwriter = csv.writer(file, delimiter=';')
					for face in toolpath_faces:	
						for point in face.points:
							spamwriter.writerow([point.x, point.y, point.z, point.facet_id])
				file.close()

				# Save all toolpath points to csv 
				with open(target_dir + f"\\intersection_points_{event_counter}.csv","w",newline='') as file:
					spamwriter = csv.writer(file, delimiter=';')
					for point in points_of_interest:
						spamwriter.writerow([point.x, point.y, point.z, point.facet_id])
				file.close()
			except:
				nx_logger("ERROR", "Toolpath points could not be stored")

	def calc_material_removal(operation):
		"""
		This function calculates the material removal, and the material removal rate
		of a CAM-operation if possible. You cannot do this with every operation. 
		This is why it is skipped for certain operation types.
		""" 

		# -- Check if  UGII_CAM_WRITE_MRR variable is set correctly --
		mrr_variable = NXOpen.Session.GetSession().GetEnvironmentVariableValue("UGII_CAM_WRITE_MRR") 
		if len(mrr_variable) == 0:
			nx_logger("ERROR", "UGII_CAM_WRITE_MRR variable not defined")
		elif mrr_variable[-4:] != ".csv":
			nx_logger("ERRoR", "UGII_CAM_WRITE_MRR must end with .csv")
		else:
			try:
				os.remove(mrr_variable) # loesche vorhandenes .csv
			except:
				pass

		try:
			# -- Generate feeds optimize builder -- 
			if not isinstance(operation, NXOpen.CAM.HoleDrilling): # add here further operations that do not
				#have a FeedsOptimizeBuilder
				feeds_optimize_builder = NXOpen.Session.GetSession().Parts.Work.CAMSetup.CreateFeedsOptimizeBuilder(operation)
				feeds_optimize_builder.Commit()
			

				# -- Einlesen des files von mrr.csv -- 
				# Spalten: length, material removal rate, volume, length, feedrate, optimized feedrate
				with open(mrr_variable, "r") as file:
					data = csv.reader(file, delimiter=";")
					mrr_list = [] # liste aller Materialabtragsraten  (mrr)
					mrr_volume = 0 # gesamter Volumenabtrag der Operation
					for data_list in data:
						if data_list[0].replace(".","").isdecimal() or data_list[0].replace(",","").isdecimal():
							if "," in data_list[0]:  # Case: Value is defined with comma instead of point
								data_list[1] = data_list[1].replace(",",".")
								data_list[2] = data_list[2].replace(",",".")
								data_list[4] = data_list[4].replace(",",".")
								data_list[5] = data_list[5].replace(",",".")
							mrr_opt = float(data_list[1])
							feed_rate_optimized = float(data_list[4])
							feed_rate_original = float(data_list[5])
							mrr_original = mrr_opt * feed_rate_optimized / feed_rate_original
							mrr_list.append(mrr_original)
							mrr_volume += float(data_list[2])
					file.close()
							
					mrr_mean = round(statistics.mean(mrr_list),3)  # Mittelwert der Materialabtragsrate
					mrr_stdev = round(statistics.stdev(mrr_list),3)  # Standardabweichung der Materialabragsrate
					mrr_volume = round(mrr_volume,3)

				return mrr_volume, mrr_mean  # unit: [mm^3] and [mm^3/min] 
		except:
			nx_logger("ERROR", f"No material removal available for operation {operation.id}")
			return None, None

	def get_ipw_edges(self, ift_toolpath, filter_length = 2, filter_type = 1):
		'''
		Returns a list of all edges in the ipw as IFTEdge. In some cases the calculation
		would take too much time. To avoid this, there can be two filter set.

		filter_length: only edges with length greater than the set value will be considered
		filter_type:
			0 --> no filter
			1 --> only edges with point higher than the base of the tool axis 
		'''
		operation = self.nx_object
		uf_session = NXOpen.UF.UFSession.GetUFSession() 
		ipw = operation.GetInputIpw() # gets the ipw object of the actual operation
		ipw_tag = ipw.Tag  # tag of the ipw object
		num_facets = uf_session.Facet.AskNFacetsInModel(ipw_tag)  # number of triangular faces in ipw
		facet_id = NXOpen.UF.UFConstants.UF_FACET_NULL_FACET_ID  # starting id for the cycle
		facet_id_list = []  # list of the ids of all facets in the ipw
		for _ in range(num_facets):
			facet_id = uf_session.Facet.CycleFacets(ipw_tag, facet_id)
			facet_id_list.append(facet_id)

		edges = list()
		ift_ipw = IFTIPW()

		for i in range(len(facet_id_list)):
			facet_id =  facet_id_list[i]
			vertices = uf_session.Facet.AskVerticesOfFacet(ipw_tag, facet_id)[1]
			vertices.append(vertices[0])
			for i in range(3): # cycle through the points of every facet (every facet consits of three points)
				# Filter all edges with length smaller than filter_length
				if numpy.linalg.norm(numpy.array(vertices[i])-numpy.array(vertices[i+1])) > filter_length:
					edge_points = [vertices[i],vertices[i+1]]
			
					if (str(edge_points) not in edges and str(list(reversed(edge_points))) not in edges):
						if filter_type == 0: # no filter set
							edges.append(str(edge_points))
							ift_ipw.add_edge(IFTEdge(IFTPoint(edge_points[0]),IFTPoint(edge_points[1])))
						if filter_type == 1: # only if one of the two points is within the lowest cutting level
							if len(ift_toolpath.cuts) >= -10**-3:  # case if there is at least one cut
								lowest_point = ift_toolpath.cuts[-1]['faces'][0].points[0] 
								rotation_matrix = ift_toolpath.cuts[-1]['T_to_help'] # matrix to rotate points to helping system
								point0_in_helping_system = numpy.matmul(rotation_matrix,edge_points[0]) 
								point1_in_helping_system = numpy.matmul(rotation_matrix,edge_points[1]) 
								# check if one point is higher:
								if point0_in_helping_system[2] > lowest_point.z or point1_in_helping_system[2] > lowest_point.z:
									edges.append(str(edge_points))
									ift_ipw.add_edge(IFTEdge(IFTPoint(edge_points[0]),IFTPoint(edge_points[1])))

		return ift_ipw
	
	@classmethod
	def get_ipw_point_tags(cls, ipw):
		'''
		Returns a list of tags, that are used in get_ipw_coordinates. Every tag represents the identification tag of the 
		point within a faceted body. 
		'''
		uf_session = NXOpen.UF.UFSession.GetUFSession()
		tag = ipw.Tag
		num_facets = uf_session.Facet.AskNFacetsInModel(tag)
		facet_id = NXOpen.UF.UFConstants.UF_FACET_NULL_FACET_ID
		uf_session.Facet.AskNFacetsInModel(tag)
		facet_id_list = list()

		for i_facet in range(num_facets):
			facet_id = uf_session.Facet.CycleFacets(tag, facet_id)
			facet_id_list.append(facet_id)

		return facet_id_list		

	@classmethod
	def get_tool_axis(cls, event):
		tool_axis_list = list()
		tool_axis = event.ToolAxis
		# Finding acitve tool axis and check if it's unique			
		if tool_axis.X == 1:
			tool_axis_list.append("+x")
		elif tool_axis.Y == 1:
			tool_axis_list.append("+y")
		elif tool_axis.Z == 1:
			tool_axis_list.append("+z")
		if tool_axis.X == -1:
			tool_axis_list.append("-x")
		elif tool_axis.Y == -1:
			tool_axis_list.append("-y")
		elif tool_axis.Z == -1:
			tool_axis_list.append("-z")
		

		if len(tool_axis_list) == 0:
			nx_logger("ERROR", "No tool axis available")
		elif len(tool_axis_list) == 1:
			axis = tool_axis_list[0]
		elif len(tool_axis_list) > 1:
			nx_logger("ERROR", "Tool axis is amigous")
		
		return axis

	def set_data_attributes(self):
		self.cuts = list() # list of information of every cut
		self.wall_faces = None
		self.floor_faces = None 
		self.floor_stock = None
		self.tool_id = None
		self.cutting_time = None 
		self.cutting_length = None 
		self.toolpath_length = None 
		self.toolpath_time = None 
		self.method = None
		self.wall_stock = None
		self.material_removal_rate = None 
		self.mean_material_removal_rate = None 
		self.feed_rate = None 
		self.feed_rate_unit = None 			
		self.spindle_speed = None
		self.has_prior_floor_operation = False
		self.material_removal = None
		self.drilling_cycle_depths = None
		self.coolant_type_open = None
		self.coolant_type_closed = None
		self.cutting_depth_configured = None
		self.stepover = None
		self.floor_faces = list()
		self.wall_faces = list() 
		self.has_intersection_points = False 
		self.axial_cutting_depth = None
		self.radial_cutting_depth = None 
		self.operation_type = None 
		self.operation_subtype = None 
		self.drilling_cycle_depths = None 


class IFTToolpath:
	'''
	This class contains all information of the toolpath
	'''

	event_type_enum = ["Motion", "Ude", "System", "LevelMarker", "Marker"]
	motion_type_enum = ["Undefined", "Rapid", "Engage", "Cut", "Retract", "FirstCut", "Approach", "Stepover", "Departure",
							"Return", "Traversal", "SideCute", "From", "Gohome", "Cycle", "InternalLift"]
	motion_shape_enum = ["Undefined", "Linear", "Circular", "Helical", "Nurbs"]

	def __init__(self, nx_operation: NXOpen.CAM.Operation):
		self.nx_object = nx_operation.GetPath() # the toolpath as nx object
		self.areas = list() # a list of the rectangular areas including the toolpath
		# Get the tool geometry
		nx_tool = nx_operation.GetParent(NXOpen.CAM.CAMSetup.View.MachineTool) 
		tool_collection = IFTToolCollection()
		tool_index = list(tool_collection.nx_objects.values()).index(nx_tool)
		tool = IFTTool(tool_collection, tool_index)
		tool.get_data_attributes()
		self.tool_diameter = tool.tool_diameter
		self.tool_height = tool.flute_length
		self.tool_axis = None 

	def get_toolpath_volume(self):
		'''
		Gives back the toolpath as cuboid of triangular faces for each linear cut motion of the toolpath.
		It's is important to understand, that this only works properly for linear cutting motions and 
		cylindrical tools. 

		Limitations: This function right now works only for cylindrical tools with linear cutting motions!

		It sets the value self.cuts of the toolpath. This is a list containing dictionaries with the following
		keys:
		- faces: all faces of the cuboid of the actual cutting motion (in the global coordinate system)
			the normal of the plane looks in direction outside of the toolpath body 
		- level: the number of the toolpath level
		- number: the number of the cutting motion in the actual level
		- T_to_help: the transformation matrix to rotate points from the global into the helping coordinate system
		- T_to_global: the transformation matrix to rotate points form the helping to the global coordinate system.
		- direction: the normed direction of the cutting event as IFTPoint
		- length: the length of the cutting event
		- tool_diameter: diameter of tool 
		- tool_height: length of blades of tool
		'''
		# initialize variables
		tool_path = self.nx_object
		start_point = None 
		end_point = None 
		level = 0
		number = 0
		self.cuts = list()

		# get number of toolpath events
		number_events = tool_path.NumberOfToolpathEvents

		# cycle through all events
		for i in range(1, number_events+1):
			# get type of every event
			event_type = self.event_type_enum[tool_path.GetToolpathEventType(i).value]

			# get all motion events 
			if event_type == "Motion":
				_, motion_type, shape = tool_path.IsToolpathEventAMotion(i)
				motion_type = self.motion_type_enum[motion_type.value]
				motion_shape = self.motion_shape_enum[shape.value]

				if motion_shape == "Linear": 
					event = tool_path.GetLinearMotion(i)

				elif motion_shape == "Circular":
					event = tool_path.GetCircularMotion(i)
				else:
					nx_logger("ERROR", f"Motion shape {motion_shape} not considered, toolpath may be analysed wrongly")

				# Define start en endpoints of the motion
				start_point = end_point # the endpoint of the last motion will be the next startpoint
				end_point = IFTPoint(event.EndPoint)

				if (motion_type == "Cut" and motion_shape == "Linear"):
					# Get normed Vector of the direction of the toolpath
					dir_unnormed = end_point.vec - start_point.vec # unnormed direction
					tool_path_dir = IFTPoint(dir_unnormed/numpy.linalg.norm(dir_unnormed))
					# Get the length of the cut
					length = numpy.linalg.norm(dir_unnormed)
					# only add if length of toolpath is bigger than 0. Sometimes there are motions with length 0
					# these must be filtered out.
					if length > 0:
						if (start_point != None and end_point != None): 
							# Get transformation matrix to convert from global coordinates to helping coordinate system
							T = self.get_transformation_matrix(event, tool_path_dir)
							# Get transformation matrix to convert friom helping coordinate system to global coordinates
							try:
								T_inv = numpy.linalg.inv(T)
								is_invertible = True
							except: 
								# tool axis equals cut direction - this is the case for drilling operations
								T_inv = None
								is_invertible = False
							
							# Convert to help coordinate system
							trans_start_point = numpy.matmul(T,start_point.vec)
							trans_end_point = numpy.matmul(T,end_point.vec)
							if (level == 0 and number == 0): # first of all cuts
								trans_start_point_old = trans_start_point 
							if trans_start_point[2] != trans_start_point_old[2]:
								level +=1
								number = 0 # reset number
							trans_start_point_old = trans_start_point # set old start point for next level

						r = self.tool_diameter/2 # tool radius
						
						h = self.tool_height # flute length of tool

						if is_invertible: # cutting direction is not tool axis
							# Points of lower face of toolpath
							p0 = IFTPoint(numpy.matmul(T_inv,numpy.array([0,-r,0]))+ start_point.vec)
							p0.facet_id = [1,3,4]
							p1 = IFTPoint(numpy.matmul(T_inv,numpy.array([0,r,0]))+ start_point.vec)
							p1.facet_id = [0,2,5]
							p2 = IFTPoint(numpy.matmul(T_inv,numpy.array([length, r, 0])) + start_point.vec)
							p2.facet_id = [1,3,6]
							p3 = IFTPoint(numpy.matmul(T_inv,numpy.array([length, -r, 0])) + start_point.vec)			
							p3.facet_id = [0,2,7]

							# Points of lower face of toolpath
							p4 = IFTPoint(numpy.matmul(T_inv,numpy.array([0,-r,h])) + start_point.vec)
							p4.facet_id = [0,5,7]
							p5 = IFTPoint(numpy.matmul(T_inv,numpy.array([0,r,h])) + start_point.vec)
							p5.facet_id = [1,4,6]
							p6 = IFTPoint(numpy.matmul(T_inv,numpy.array([length, r, h])) + start_point.vec)	
							p6.facet_id = [2,5,7]
							p7 = IFTPoint(numpy.matmul(T_inv,numpy.array([length, -r, h])) + start_point.vec)	
							p7.facet_id = [3,4,6]

							# Define triangular faces of cuboid generated by tool
							f00 = IFTFace([p0,p4,p7])
							f01 = IFTFace([p0,p7,p3])
							f10 = IFTFace([p1,p5,p4])
							f11 = IFTFace([p1,p4,p0])
							f20 = IFTFace([p2,p6,p5])
							f21 = IFTFace([p2,p5,p1])
							f30 = IFTFace([p3,p7,p6])
							f31 = IFTFace([p3,p6,p2])
							f40 = IFTFace([p1,p0,p3])
							f41 = IFTFace([p1,p3,p2])
							f50 = IFTFace([p4,p5,p6])
							f51 = IFTFace([p4,p6,p7])
							faces = [f00, f01, f10, f11, f20, f21, f30, f31, f40, f41, f50, f51]

							self.cuts.append({'level':level, 'number':number, 'faces':faces,  'T_to_help':T, 'T_to_global': T_inv, 
											'direction':tool_path_dir, 'length': length, 'start_point': start_point,
											'end_point': end_point, "tool_diameter": self.tool_diameter, "tool_height": self.tool_height})
							number +=1 # rise number of cut by one

						else: 
							faces = None
							self.cuts.append({'faces':faces, 'level':level, 'number':number, 'T_to_help':T, 'T_to_global': T_inv, 
									'direction':tool_path_dir, 'length': length})
					
				
				elif (motion_type == "Cut" and motion_shape == "Circular"):
					nx_logger("ERROR", f"Circular cuts are not implemented yet")
					# TODO
				elif (motion_type == "Cut" and motion_shape == "Helical"):
					nx_logger("ERROR", f"Helical cuts are not implemented yet")
					# TODO

		self.number_layers = level+1 # set the number of layers
		self.number_cuts_per_layer = number # set number of cuts per layer

	
	def get_cutting_width(self):
		"""
		Returns double of the distance between two parallel toolpath cuts. For operations with multiple
		cuts per layer this is the cutting width. If not applicable for the toolpath, returns None.
		"""
		distances = list()	
		for cut in self.cuts:
			if cut['level'] == self.number_layers-1 and cut['number'] == 0: # find first cut of last layer
				first_edge = IFTEdge(cut['start_point'], cut['end_point']) # create IFTEdge of start- and endpoint of cutting motion
			elif cut['level'] == self.number_layers-1: # find all other cuts of first layer
				second_edge = IFTEdge(cut['start_point'], cut['end_point'])

				# Calculate distance of the paths if parallel
				is_parallel = first_edge.check_if_parallel(second_edge) 
				if is_parallel: # there are parallel cut paths
					distances.append(first_edge.get_minimum_distance(second_edge)) 
		
		if len(distances) > 0: # there are parallel cuts
			self.cutting_width = min(distances) # choose the distance with the smallest value
		else:
			self.cutting_width = None 
			nx_logger("ERROR", "Cutting width could not be calculated with toolpath")


	@classmethod
	def get_transformation_matrix(cls, event, toolpath_direction):
		'''
		Calculates the Transformation matrix to represent the points from the global active coordinate system 
		of the CAM-Setup into the auxilary-coordinate system of the toolpath
		'''
		# Get tool axis of the operation
		tool_axis = IFTPoint(event.ToolAxis)
		
		# Norm and calculate the base vectors of the coordinate system
		x = toolpath_direction.vec/numpy.linalg.norm(toolpath_direction.vec)
		z = tool_axis.vec/numpy.linalg.norm(tool_axis.vec)
		y = numpy.cross(z,x)

		# Transformation Matrix (a' = Ta)
		T = numpy.array([x,y,z])
		
		return T


class IFTPoint:

	def __init__(self, coordinate):
		if isinstance(coordinate, (NXOpen.Point3d, NXOpen.Vector3d)):
			self._x = float(round(coordinate.X,3))
			self._y = float(round(coordinate.Y,3))
			self._z = float(round(coordinate.Z,3))
		elif isinstance(coordinate, (list, numpy.ndarray)):
			self._x = round(coordinate[0],3)
			self._y = round(coordinate[1],3)
			self._z = round(coordinate[2],3)
		else:
			nx_logger("ERROR",f"Point could not be created for Object: {type(coordinate)}")   

		self._vec = numpy.array([self.x, self.y, self.z])
		self.normal = None # the normal direction of the face beloning to this point
		self.facet_id = None # the id of the facet belonging to this point
	
	@property 
	def x(self):
		return self._x 
	
	@x.setter
	def x(self, value):
		#try:
		self._x = round(float(value),3)
		self._vec[0] = self._x
		#except:
		#	nx_logger("ERROR","IFTPoint.x could not be set. Value must be numeric")

	@property 
	def y(self):
		return self._y 
	
	@y.setter
	def y(self, value):
		try:
			self._y = round(float(value),3)
			self._vec[1] = self._y
		except:
			nx_logger("ERROR", "IFTPoint.y could not be set. Value must be numeric")

	@property 
	def z(self):
		return self._z 
	
	@z.setter
	def z(self, value):
		try:
			self._z = round(float(value),3)
			self._vec[2] = self._z
		except:
			nx_logger("ERROR","IFTPoint.z could not be set. Value must be numeric")
   
	@property 
	def vec(self):
		return self._vec 
	
	@vec.setter
	def vec(self, value):
		if isinstance(value, (list, numpy.ndarray)):
			if len(value) == 3:
				self._vec = numpy.array(value)
				self._x = round(value[0],3)
				self._y = round(value[1],3)
				self._z = round(value[2],3)
			else:
				nx_logger("ERROR","IFTPoint.vec could not be set")
		else: 
			nx_logger("ERROR","IFTPoint.vec could not be set")


	def __str__(self):
		return f"X: {self._x}, Y: {self._y}, Z: {self._z}"

	def sum(self, point):
		self.vec = point._vec + self._vec

	def sub(self, point):
		self.vec = point._vec - self._vec

	def rotate(self, rot_mat):	
		# First rotation to coordinate System of cam setup
		coord_rot = numpy.matmul(rot_mat, self.vec)
		# Linear displacement of coordinate
		self.vec = coord_rot


class IFTFace:
	counter = 0
	def __init__(self, points:list):
		if len(points) < 3: # too little points to define face:
			print(">>>>> ERROR: Argument {points} needs at least 3 points")
		self.counter+=1
		self.points = points 
		self.intersection_points = list()
		self.intersection_edges = list()
		self.edges = None
		self.eq_coeffs = None
		self.set_edges()
		self.set_plane_equation()

	def set_edges(self):
		points = self.points
		edges = list()
		for i in range(len(points)):
			if i != len(points)-1:
				edge = IFTEdge(points[i],points[i+1])
			else:
				edge = IFTEdge(points[i], points[0])
			edges.append(edge)
			self.id = self.counter
		self.edges = edges

	def set_plane_equation(self):
		'''
		Sets the coefficients a, b, c and d of the of the plane a * x + b * y  + c * z + d = 0
		as eq_coeffs in the following form:
		[a, b, c, d]
		'''
		a = self.points[0]
		b = self.points[1]
		c= self.points[2]   
		ab = IFTPoint((b.vec - a.vec)/numpy.linalg.norm(b.vec - a.vec))
		ac = IFTPoint((c.vec - a.vec)/numpy.linalg.norm(c.vec - a.vec))
		normal_vec = IFTPoint(numpy.cross(ac.vec, ab.vec)/numpy.linalg.norm(numpy.cross(ac.vec, ab.vec)))
		self.normal = normal_vec
		a_coeff = normal_vec.x
		b_coeff = normal_vec.y 
		c_coeff = normal_vec.z 
		d_coeff = -(a_coeff*b.x + b_coeff*b.y + c_coeff*b.z)
		self.eq_coeffs = [a_coeff, b_coeff, c_coeff, d_coeff]

	def check_if_intersection_within_face(self, p:IFTPoint):
		'''
		This will be checked by the inside outside method, described in 
		https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-rendering-a-triangle/ray-triangle-intersection-geometric-solution.
		'''
		num_points = len(self.points)       
		if num_points == 3:
			[p0, p1, p2] = self.points
			n = self.normal.vec 
			n0 = numpy.cross(p.vec - p0.vec, p1.vec - p0.vec)
			n1 = numpy.cross(p.vec - p1.vec, p2.vec - p1.vec)
			n2 = numpy.cross(p.vec - p2.vec, p0.vec - p2.vec)
			dot0 = numpy.dot(n,n0)
			dot1 = numpy.dot(n,n1)
			dot2 = numpy.dot(n,n2)
			if (dot0 >= 0 and dot1 >= 0 and dot2 >= 0):
				return True
			else:
				return False

	def find_intersect_point(self, edge):
		'''
		Solves the equation of the edge and the face and finds the intersection point if there exists one

		this solves following equation system to t:
		x = t * a1 + b1
		y = t * a2 + b2
		z = t * a3 + b3
		a * x + b * y + c * z + d = 0

		if the resulting t is real, the edge and the face intersect.
		If there is a real t, you can get the intersection point from the edge equation
		'''
		intersection_point = None 
		[a, b, c, d] = self.eq_coeffs
		[[a1, b1],[a2, b2],[a3, b3]] = edge.eq_coeffs 
		A = a * b1 + b * b2 + c * b3 + d
		B = a * a1 + b * a2 + c * a3
		t = -A/B 
		dot_product = numpy.dot(self.normal.vec, edge.points[1].vec - edge.points[0].vec)
		if abs(dot_product) < 0.01: # line is (almost) parallel to plane and no intersection point exists
			# Edge does not intersect 
			pass
		else:
			if (t > 0 and t < 1): # intersection point lies within the two points of the edge
				intersection_point = edge.calc_point_on_edge(t)
				is_in_face = self.check_if_intersection_within_face(intersection_point) 
				if is_in_face:
					self.intersection_points.append(intersection_point)
					if edge not in self.intersection_edges:
						self.intersection_edges.append(edge)
				else: 
					intersection_point = None 

		return intersection_point, edge, self # returns the intersection point, the intersecting edge and face 

	def calc_point_distance(self, point):
		[a, b, c, d] = self.eq_coeffs 
		p = point.vec 
		distance = a * p[0] + b * p[1] + c * p[2] + d
		return distance 


class IFTIPW:
	"""
	The IFTIPW holds the information of the ipw body. Main element is the self.edges attribute, which
	is a dictionary of edges, where the id of the edge is the key. 
	"""
	def __init__(self):
		self.edges = {}
	
	def add_edge(self, edge):
		self.edges[edge.id] = edge 

	def remove_edge(self, edge_id):
		try:
			self.edges.pop(edge_id)
		except:
			pass

	def cut_ipw(self, toolpath_cut):
		"""
		This function calculates the intersecting points of an ipw and a toolpath cut volume.
		The intersecting edges are split at the point of intersection. After the cut the old 
		edges of the ipw are deleted if there was an intersection, as if the tool would have
		done a cutting of the ipw. 

		returns: intersection_points: list
		"""
		intersection_edge_ids = list() # list of the edge ids that intersected
		added_edges = list()
		intersection_points = list()
		for face in toolpath_cut['faces']:
			for edge in self.edges.values():
				intersection_point, intersection_edge, intersection_face = face.find_intersect_point(edge)
				if intersection_point: # add intersection point to list if not None
					intersection_points.append(intersection_point)
				if intersection_point:
					p0 = intersection_edge.points[0]
					p1 = intersection_edge.points[1]
					# create new edge outside of toolpath
					if face.calc_point_distance(p0) > 0:
						added_edges.append(IFTEdge(intersection_point, p0))
					elif face.calc_point_distance(p1) > 0: 
						added_edges.append(IFTEdge(intersection_point, p1))
				   
					# add the id of the intersecting edge, to later delete it
					if intersection_edge.id not in intersection_edge_ids:
						intersection_edge_ids.append(intersection_edge.id)
		# delete old edges
		for id in intersection_edge_ids:
			self.edges.pop(id)
		# add new edges
		for edge in added_edges:
			self.add_edge(edge)
		
		return intersection_points
		
	def get_points_in_toolpath_volume(self, toolpath_cut):
		"""
		DONT USE THIS FUNCTION BEFORE self.cut_ipw!

		Checks for every point of the ipw if point is within the enclosing volume of the
		toolpath volume
		This is done with the face equations. The toolpath body is a closed body modeled with triangle faces 
		with the normals of this faces pointing outside of the toolpath. If a point is inserted into the plane
		equation of a face, you get the distance of the point to the face. If the result is negativ, the point
		is located behind the face. If you do the same for all faces of the toolpath body, and all results are 
		negativ, the point is located within the toolpath.

		This function returns a list of all the points inside the volume and a list of ids of the edges, where
		both points of the edge where inside of the toolpath. These points are not detected by the intersection
		function, therefore this must be deleted later from the ipw.

		returns: points_in_toolpath: list
		"""
		points_in_toolpath = list()
		edge_ids_in_toolpath = list()
		for edge in self.edges.values():
			p1 = edge.points[0]
			p2 = edge.points[1]
			is_p1_in_toolpath = True 
			is_p2_in_toolpath = True 
			is_p1_on_face = False 
			is_p2_on_face = False
			# cycle through all faces of toolpath, if condition is violated one time, break
			d_p1 = numpy.array([])
			d_p2 = numpy.array([])
			
			for face in toolpath_cut['faces']:
				d_p1 = numpy.append(d_p1, face.calc_point_distance(p1))
				d_p2 = numpy.append(d_p2, face.calc_point_distance(p2))

			is_p1_in_toolpath = numpy.all(d_p1 < 0) # point 1 in toolpath
			is_p2_in_toolpath = numpy.all(d_p2 < 0) # point 2 in toolpath
			is_p1_on_face = numpy.any(d_p1 == 0) # point 1 on face
			is_p2_on_face = numpy.any(d_p2 == 0) # point 2 on face
			

			
			# add both points if one is in toolpath and the other on face
			if ((is_p1_in_toolpath and is_p2_on_face) or (is_p2_in_toolpath and is_p1_on_face)): # case: one point in toolpath the other on face
				points_in_toolpath.append(p1)
				points_in_toolpath.append(p2)
				edge_ids_in_toolpath.append(edge.id)
				if p1.z > 265:
					#print_nx(d_p1)
					#print_nx(is_p1_in_toolpath)
					pass

				
			elif is_p1_in_toolpath:
				points_in_toolpath.append(p1)
			elif is_p2_in_toolpath:
				points_in_toolpath.append(p2)
			elif is_p1_in_toolpath and is_p2_in_toolpath:
				points_in_toolpath.append(p1)
				points_in_toolpath.append(p2)
				edge_ids_in_toolpath.append(edge.id)

		# delete the edges in the toolpath
		for id in edge_ids_in_toolpath:
			self.remove_edge(id)
		
		return points_in_toolpath


class IFTEdge:
	counter = 0

	def __init__(self, point1, point2):
		self.id = IFTEdge.counter
		IFTEdge.counter += 1
		self.points = [point1, point2]
		self.eq_coeffs = None
		self.get_edge_function()
		self.length = numpy.linalg.norm(point1.vec-point2.vec)
		
	def get_edge_function(self):
		'''
		This returns the coefficients of the parametric expression of a line in R3

		x = t*(x2 - x1) + x1 --> x = t * a1 + b1
		y = t*(y2 - y1) + y1 --> y = t * a2 + b2
		z = t*(z2 - z1) + z1 --> z = t * a3 + b3

		It sets the equation coefficients like following:
		[[a1,b1],[a2,b2][a3,b3]]
		'''
		p1 = self.points[0] 
		p2 = self.points[1]
		x = [p2.x-p1.x, p1.x]
		y = [p2.y-p1.y, p1.y]
		z = [p2.z-p1.z, p1.z]
		self.eq_coeffs = [x, y, z]

	def calc_point_on_edge(self,t):
		coeffs = self.eq_coeffs
		c1 = coeffs[0]
		c2 = coeffs[1]
		c3 = coeffs[2]
		x = c1[0] * t + c1[1]
		y = c2[0] * t + c2[1]
		z = c3[0] * t + c3[1]
		return IFTPoint([x,y,z])

	def check_if_parallel(self, other):
		"""
		Checks if two lines are parallel and returns boolean.
		"""
		vec_1 = self.points[1].vec - self.points[0].vec
		vec_1_norm = vec_1/numpy.linalg.norm(vec_1)
		vec_2 = other.points[1].vec - other.points[0].vec 
		vec_2_norm = vec_2/numpy.linalg.norm(vec_2)
		tol = 1e-06 # tolerance value for numerical errors
		dot_product =numpy.dot(vec_1_norm, vec_2_norm)
		if abs(dot_product)-1 < tol:
			return True 
		else:
			return False 

	def check_if_normal(self, other):
		"""
		Checks if two lines are normal and returns boolean.
		"""
		vec_1 = self.points[1].vec - self.points[0].vec
		vec_1_norm = vec_1/numpy.linalg.norm(vec_1)
		vec_2 = other.points[1].vec - other.points[0].vec 
		vec_2_norm = vec_2/numpy.linalg.norm(vec_2)
		tol = 1e-06 # tolerance value for numerical errors
		dot_product =numpy.dot(vec_1_norm, vec_2_norm)
		if abs(dot_product) < tol:
			return True 
		else:
			return False 

	def get_minimum_distance(self, other):
		"""
		Calculates the minimum distance of two edges and returns the float value
		
		For parallel edges that works with the equation d = ||n x (p-q)||
		where p1 is a point on edge 1 and p2 a point on edge 2. 
		n is the direction vector of edge 1
		"""
		if self.check_if_parallel(other): #case lines are parallel
			p = self.points[0].vec
			q = other.points[0].vec 
			n = (self.points[0].vec - self.points[1].vec)/numpy.linalg.norm(self.points[0].vec - self.points[1].vec)

			distance = round(numpy.linalg.norm(numpy.cross(n, (q-p))),3)
		else:
			IFTCore.nx_logger("ERROR", "Distance for non parallel lines not implemented")
			distance = None 

		return distance 


if __name__ == '__main__':
	operations = IFTOperationCollection()
	
	if False:
		for i in range(operations.nx_counter):
			operation = IFTOperation(operations, i)
			operation.get_data_attributes()
			print_nx(operation.foreign_ids_dict)
			print_nx(operation.has_relations)
			print_nx(json.dumps(operation.get_data_dict(),indent = 2))

	if True:
		operation = IFTOperation(operations, 5, store_data = True)
		operation.get_data_attributes()
		