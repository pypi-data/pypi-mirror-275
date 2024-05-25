# nx: threaded
import json
import NXOpen
import NXOpen.CAM
import sys 

from ift-dbms.IFTBase import IFTCore, IFTObject, IFTCollection
print_nx = IFTCore.print_nx


class IFTToolCollection(IFTCollection):
	"""
	Collection class for IFTTool instances
	"""

	def __init__(self):
		super().__init__()
		
		nx_group_collection = NXOpen.Session.GetSession().Parts.Work.CAMSetup.CAMGroupCollection
		for group in nx_group_collection:
			if isinstance(group, NXOpen.CAM.Tool):
				self.nx_objects[self.nx_counter] = group 
				self.nx_counter +=1


class IFTTool(IFTObject):
	"""
	Class to handle and store data of NXOpen.CAM.Tool objects
	"""

	relation_name_single = "toolId"
	relation_name_plural = "toolIds"
	tool_mat_map = None  # contains data of the tool material library
	tool_type_map = {0:"Mill", 1:"Drill", 2:"Turn", 3:"Groove", 4:"Thread", 5:"Wedm", 6:"Barrel", 7:"Tcutter", 8:"Form", 
				9:"DrillSpcGroove", 10:"Solid", 11:"MillForm", 12:"Laser", 13:"Soft"}  # is used to get tool type 
	tool_subtype_map = subtype_enum = {
					0:"MillSpherical", 1:"Mill5", 2:"Mill7", 3:"Mill10", 4:"MillBall", 5:"DrillStandard",
					6:"DrillCenterBell", 7:"DrillCounterSink", 8:"DrillSpotFace", 9:"DrillSpotDrill",
					10:"DrillBore", 11:"DrillReam", 12:"DrillCounterbore", 13:"DrillTap", 14:"DrillBurnishing", 
					15:"DrillThreadMill", 16:"DrillBackSpotFace", 17:"DrillStep", 18:"TurnStandard", 19:"TurnButton",
					20:"TurnBoringBar", 21:"GrooveStandard", 22:"GrooveRing", 23:"GrooveFullNoseRadius",
					24:"GrooveUserDefined", 25:"ThreadStandard", 26:"ThreadButress", 27:"ThreadAcme",
					28:"ThreadTrapezoidal", 29:"Generic", 30:"Probe", 31:"MillChamfer", 32:"DrillCore", 33:"Laser",
					34:"DrillBackCountersink", 35:"CoaxialLaser", 36:"DrillBoringBar", 37:"DrillChamferBoringBar"}
					# is used to get tool subtype
	 
	
	def __init__(self, tool_collection:IFTToolCollection, idx:str):
		super().__init__(tool_collection, idx)

	def get_data_attributes(self):
		if not self.has_data_attributes:
			# -- Get Tool Material Database -- 
			if not self.tool_mat_map:  # data of material library is not available
				self.get_tool_material_dat()

			tool_builder = self.get_tool_builder()
			if tool_builder:
				# ==== Get Information of Methods and Attributes from ToolBuilder class ==== 

				# -- General information --
				self.material_id = tool_builder.GetMaterial()  # Tool material
				try:
					self.material = self.tool_mat_map[self.material_id]
				except:
					IFTCore.nx_logger("ERROR", f"Chosen tool material of {self.id} is not in tool material library.")
				
				self.bib_ref = tool_builder.TlLibref
				self.catalog_number = tool_builder.TlCtlgNum
				self.pot_nr = tool_builder.TlNumberBuilder.Value  # Position of Tool



				# -- holder geometry information --
				holder_length = 0
				for i in range(0,tool_builder.HolderSectionBuilder.NumberOfSections):
					holder_section = tool_builder.HolderSectionBuilder.GetSection(i)
					(diameter, section_length, taper_angle, corner_radius)= tool_builder.HolderSectionBuilder.Get(holder_section)
					holder_length += section_length
				holder_offset = tool_builder.HolderSectionBuilder.TlHolderOffsetBuilder.Value
				
				# == tool geometry information ==
				# for the different tool builders refer to https://docs.plm.automation.siemens.com/data_services/resources/nx/1847/nx_api/custom/en_US/nxopen_net/a03056.html
				
				# NXOpen.CAM.MillingToolBuilder
				if isinstance(tool_builder, NXOpen.CAM.MillingToolBuilder):
					if tool_builder.UseTaperedShank:
						self.shank_length = tool_builder.TaperedShankLengthBuilder.Value  # shank length of tool
					else:
						self.shank_length = 0  # shank length of tool
					self.tool_length = tool_builder.TlHeightBuilder.Value  # length of tool itself
					self.tool_diameter = tool_builder.TlDiameterBuilder.Value  # diameter of tool
					self.cantilever_length = self.tool_length + self.shank_length - holder_offset  #
					self.total_length = self.cantilever_length + holder_length
					self.flutes = tool_builder.TlNumFlutesBuilder.Value
					self.tool_description = tool_builder.TlDescription
					self.tool_taper_angle =tool_builder.TlTaperAngBuilder.Value

					# NXOpen.CAM.MillToolBuilder
					if isinstance(tool_builder, NXOpen.CAM.MillToolBuilder):
						self.flute_length = tool_builder.TlFluteLnBuilder.Value
						self.corner_radius = tool_builder.TlCor1RadBuilder.Value
						self.tip_angle = tool_builder.TlTipAngBuilder.Value
						self.taper_angle = tool_builder.TlTaperAngBuilder.Value
						chamfer_length = tool_builder.ChamferLengthBuilder.Value
						if chamfer_length != 0:
							self.chamfer_length = chamfer_length
						relief_diameter = tool_builder.ReliefDiameterBuilder.Value
						if (relief_diameter != self.tool_diameter and relief_diameter != 0):
							self.relief_diameter = tool_builder.ReliefDiameterBuilder.Value
							self.relief_length = tool_builder.ReliefLengthBuilder.Value

					# NXOpen.CAM.BarrelToolBuilder
					elif isinstance(tool_builder, NXOpen.CAM.BarrelToolBuilder):
						IFTCore.nx_logger("ERROR", "Data export for NXOpen.CAM.BarrelToolBuilder not implemented.")
					
					# NXOpen.CAM.DrillToolBuilder
					elif isinstance(tool_builder, NXOpen.CAM.DrillToolBuilder):
						self.corner_radius = tool_builder.TlCor1RadBuilder.Value
						self.flute_length = tool_builder.TlFluteLnBuilder.Value

					# NXOpen.CAM.MillFormToolBuilder
					elif isinstance(tool_builder, NXOpen.CAM.MillFormToolBuilder):
						IFTCore.nx_logger("ERROR", "Data export for NXOpen.CAM.MillFormToolBuilder not implemented.")

					# NXOpen.CAM.TToolBuilder
					elif isinstance(tool_builder, NXOpen.CAM.TToolBuilder):
						IFTCore.nx_logger("ERROR", "Data export for NXOpen.CAM.TToolBuilder not implemented.")
				
				else:
					IFTCore.nx_logger("ERROR", f"Data export for {type(tool_builder)} not implemented.")


				tool_builder.Destroy()
				self.has_data_attributes = True  # set boolean value to true

	def get_data_dict(self):
		self.data_dict = {
					"toolId": self.id,
					"type": self.type,
					"subtype": self.subtype,
					"materialId":self.material_id,
					"materialName": self.material,
					"cantileverLength": self.cantilever_length,
					"cornerRadius": self.corner_radius,
					"chamferLength": self.chamfer_length,
					"toolDiameter": self.tool_diameter,
					"fluteLength": self.flute_length,
					"pointAngle": self.point_angle,
					"reliefDiameter": self.relief_diameter,
					"reliefLength": self.relief_length,
					"taperAngle": self.taper_angle,
					"tipAngle": self.tip_angle,
					"NumberOfTeeth": self.flutes,
					"toolLength": self.tool_length,			
					}

		return self.data_dict

	def set_data_attributes(self):
		"""Here the IFTTool attributes are initialized"""
		self.type = None 
		self.chamfer_length = None 
		self.corner_radius = None
		self.point_angle = None 
		self.relief_diameter = None
		self.relief_length = None 
		self.taper_angle = None  
		self.subtype = None 
		self.tip_angle = None 
		self.tool_diameter = None
		self.tool_length = None 
		self.cantilever_length = None 
		self.total_length = None 
		self.flute_length = None 
		self.flutes = None 
		self.material = None 
		self.material_id = None 

	def get_tool_material_dat(cls):
		"""
		Reads the file tool_materials.dat in the active UGII_CAM_LIBRARY_FEEDS_SPEEDS_ASCII_DIR directory and 
		gets a dictionary that maps the material used in the NXOpen.CAM.Tool instance to the material database.
		This allows to get addition values tool material values like hardness.
		"""
		tool_library_dir = NXOpen.Session.GetSession().GetEnvironmentVariableValue("UGII_CAM_LIBRARY_FEEDS_SPEEDS_ASCII_DIR")
		cls.tool_mat_map = {}
		with open (tool_library_dir + "tool_materials.dat", "r") as file:
			for line in file:
				if line[0:4] == "DATA":
					mat_data = line.split("|")
					cls.tool_mat_map[mat_data[1]] = mat_data[2]
		file.close()
	
	def get_relations_to_operation(self):
		"""
		Finds the relations of the Tool and storeds it in the self.foreign_ids_dict of the IFTTool instance.
		"""
		members = self.nx_object.GetMembers()
		for member in members:
			if isinstance(member, NXOpen.CAM.Operation):
				self.foreign_ids_dict["operations":]
	
	def get_tool_type_and_subtype(self):
		"""
		Maps and gets the typ and subtype of the tool from the integer value of the enumeration to the 
		string value
		"""
		self.type = self.tool_type_map[self.nx_object.GetTypeAndSubtype()[0].value]
		self.subtype = self.tool_subtype_map[self.nx_object.GetTypeAndSubtype()[1].value]

	def get_tool_builder(self):
		"""
		Returns the NXOpen.Builder class for the tool depending on its type. Be sure to destroy the
		tool builder after using it with tool_builder.Destroy()
		"""

		# == Create Toolbuilder for Tool Type and Subtype ==
		self.get_tool_type_and_subtype()
		cam_group_collection = NXOpen.Session.GetSession().Parts.Work.CAMSetup.CAMGroupCollection
		if self.type == "Mill":
			# INFO - other subtypes that use the MillToolBuilder:
			# Mill5","Mill7","Mill10","MillBall","MillChamfer","MillSpherical"
			tool_builder = cam_group_collection.CreateMillToolBuilder(self.nx_object)
		elif self.subtype == "DrillStandard":
			tool_builder = cam_group_collection.CreateDrillStdToolBuilder(self.nx_object)
		elif self.subtype == "DrillBackSpotFace":
			tool_builder = cam_group_collection.CreateDrillBackSpotfacingToolBuilder(self.nx_object)
		elif self.subtype == "DrillBore":
			tool_builder = cam_group_collection.CreateDrillBoreToolBuilder(self.nx_object)
		elif self.subtype == "DrillBurnishing":
			tool_builder = cam_group_collection.CreateDrillBurnishingToolBuilder(self.nx_object)
		elif self.subtype == "DrillCenterBell":
			tool_builder = cam_group_collection.CreateDrillCenterBellToolBuilder(self.nx_object)
		elif self.subtype == "DrillCore":
			tool_builder = cam_group_collection.CreateDrillCioreToolBuilder(self.nx_object)
		elif self.subtype == "DrillCounterbore":
			tool_builder = cam_group_collection.CreateDrillCounterboreToolBuilder(self.nx_object)
		elif self.subtype == "DrillCountersink":
			tool_builder = cam_group_collection.CreateDrillCtskToolBuilder(self.nx_object)
		elif self.subtype == "DrillReam":
			tool_builder = cam_group_collection.CreateDrillReamerToolBuilder(self.nx_object)
		elif self.subtype == "DrillSpotDrill":
			tool_builder = cam_group_collection.CreateDrillSpotdrillToolBuilder(self.nx_object)
		elif self.subtype == "DrillSpotFace":
			tool_builder = cam_group_collection.CreateDrillSpotfaceBuilder(self.nx_object)
		elif self.subtype == "DrillStep":
			tool_builder = cam_group_collection.CreateDrillStepToolBuilder(self.nx_object)
		elif self.subtype == "DrillTap":
			tool_builder = cam_group_collection.CreateDrillTapToolBuilder(self.nx_object)
		elif self.subtype == "DrillThreadMill":
			tool_builder = cam_group_collection.CreateDrillThreadMillToolBuilder(self.nx_object)
		elif self.type == "Barrel":
			tool_builder = cam_group_collection.CreateBarrelToolBuilder(self.nx_object)
		elif self.type == "MillForm":
			tool_builder = cam_group_collection.CreateMillFormToolBuilder(self.nx_object)
		elif self.type == "Tcutter":
			tool_builder = cam_group_collection.CreateTToolBuilder(self.nx_object)
		else:
			IFTCore.nx_logger("ERROR", f"Tool builder for Tooltype {self.type} is not implemented <<<<<")
			tool_builder = None 
		return tool_builder 






if __name__ == '__main__':
	if False:
		ift_tools = IFTToolCollection()
		for i in range(ift_tools.number):
			tool = IFTTool(ift_tools, i)
			print_nx(tool.id)
			print_nx(tool.nx_object.GetTypeAndSubtype()[0])
			print_nx(tool.nx_object.GetTypeAndSubtype()[1])
			tool_type = tool.nx_object.GetTypeAndSubtype()[0]
			tool_subtype = tool.nx_object.GetTypeAndSubtype()[0]
			#print_nx(tool_type == NXOpen.CAM.Tool.Types.Mill)
			#print_nx(f"Type: {tool.nx_object.GetTypeAndSubtype()[0]}, Subtype: {tool.nx_object.GetTypeAndSubtype()[1]}")
			print_nx(json.dumps(IFTTool(ift_tools, i).get_dict(), indent = 2))

	if False:
		tool_collection = IFTToolCollection() 
		for i in range(tool_collection.nx_counter):
			tool_temp = IFTTool(tool_collection, i)
			tool_temp.get_data_attributes()
			data_dict = tool_temp.get_data_dict()
			print_nx(json.dumps(data_dict, indent = 2))


	if True: 
		tool_collection = IFTToolCollection()
		tool_3 = IFTTool(tool_collection, 4)
		tool_3.get_data_attributes()
		data_tool_3 = tool_3.get_data_dict()
		IFTCore.print_nx(json.dumps(data_tool_3, indent = 2))
