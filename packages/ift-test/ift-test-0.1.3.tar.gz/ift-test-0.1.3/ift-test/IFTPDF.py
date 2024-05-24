# nx: threaded
import NXOpen
import NXOpen.CAM
import NXOpen.TDP
import os
from pymongo import MongoClient
import gridfs

from IFT.IFTBase import IFTCore 
from IFT.IFTTool import IFTToolCollection, IFTTool
from IFT.IFTMachiningPart import IFTMachiningPartCollection, IFTMachiningPart
print_nx = IFTCore.print_nx


class IFTPDF:

	@classmethod
	def export_cam_pdf(cls, tool_collection:IFTToolCollection, storage_dir = None):
		'''
		This function exports a PDF of the CAM Setup. It should be possible to see the mounting situation
		Inputs:
			tools: list - List containing IFTTool objects
			storage_dir: str - storage directory of the pdf

		Output: 
			filedir: str - directory of the pdf file inclusive filename and .pdf

		'''
		# -- Get data of the used machine -- 
		session = NXOpen.Session.GetSession()
		work_part = session.Parts.Work
		cam_setup = work_part.CAMSetup
		try:
			kinematic_configurator = work_part.KinematicConfigurator
			machine_library_builder = kinematic_configurator.CreateMachineLibraryBuilder()
			machine_lib_ref = cam_setup.GetMachineLibref()
			control = machine_library_builder.GetValue(machine_lib_ref, "Control")
			description = machine_library_builder.GetValue(machine_lib_ref, "Description")
		except:
			IFTCore.nx_logger("ERROR", f"No machine library and control set. Fields in PDF skipped")
			control = "Nicht definiert"
			description = "Nicht definiert"
			machine_lib_ref = "Nicht definiert"

		theTDPManager = NXOpen.TDP.Manager.GetManager(NXOpen.Session.GetSession())    
		publisher_builder = theTDPManager.CreateTdpPublisherBuilder(work_part)  
		publisher_builder.ViewSelection = NXOpen.TDP.PublisherBuilder.ViewSelectionType.AllViews 

		# -- Get Template PDF -- 
		module_path = os.path.dirname(os.path.abspath(__file__))  # directory of this python module
		template_dir = module_path + "\\static\\A4_template_cam_setup.prt"  # directory of the template pdf

		# -- Set file dir -- 
		if storage_dir:
			#os.mkdir(storage_dir)
			file_dir = storage_dir
		else:
			file_dir = os.path.join(module_path, f"{work_part.Name}.pdf")
		publisher_builder.OutputFilename = file_dir
		

		# -- Set values of fields in PDF -- 
		publisher_builder.SetWorkTemplateFile(template_dir)  # set the template 
		publisher_builder.SetTextValueOfLabel("BibRef", machine_lib_ref)
		publisher_builder.SetTextValueOfLabel("Beschreibung", description)  
		publisher_builder.SetTextValueOfLabel("Steuerung", control)  
		
		# -- Generate tool mounting table -- 
		tools = list(tool_collection.ift_objects.values())
		output_1 = IFTPDF.generate_tool_info_strings(tools)
		output_2 = [""]
		IFTPDF.create_tool_table(template_dir, theTDPManager, output_1, output_2)

		# -- Publish PDF --
		publisher_builder.Publish()
		publisher_builder.Destroy()
		IFTCore.nx_logger("INFO", f"File was stored as {file_dir}")
		NXOpen.Session.GetSession().CleanUpFacetedFacesAndEdges()
		return file_dir 
		 
	@staticmethod
	def generate_tool_info_strings(tools):
		output_1 = list()
		columns = ["Pot. Nr.","Name", "Beschreibung", "Bibref", "Katalognummer", "Auskraglänge", "Gesamtlänge"]
		space = ":    "
		for tool in tools:
			output_1.append(f"{columns[1]}:    {tool.nx_object.Name}")
			output_1.append(f"{columns[2]}:    {tool.tool_description}")
			output_1.append(f"{columns[3]}:    {tool.bib_ref}")
			output_1.append(f"{columns[4]}:    {tool.catalog_number}")
			output_1.append(f"{columns[5]}:    {tool.cantilever_length}")
			output_1.append(f"{columns[6]}:    {tool.total_length}")
			output_1.append(" ")


		return output_1

	@staticmethod
	def create_tool_table(template_dir, theTDPManager, output_1, output_2):
		'''
		This function bundles and publishes the information of the tool mounting including the
		pot number of the tool, tool name, description of tool, bibliotec reference, catalog number,
		cantilever length of the tool, total length

		This helps the user to setup the machine before manufacturing
		'''

		# -- Open template part -- 
		try:
			part2, _ = NXOpen.Session.GetSession().Parts.Open(template_dir)

		except: # Part already opened
			part2 = NXOpen.Session.GetSession().Parts.FindObject("A4_template")

		genericNote1 = part2.FindObject("HANDLE R-61147")
		templateNoteBuilder1 = theTDPManager.CreateTemplateNoteBuilder(part2, genericNote1);

		# -- First Column of table tool list --
		templateNoteBuilder1.Text.TextBlock.CustomSymbolScale = 1.0
		templateNoteBuilder1.Origin.SetInferRelativeToGeometry(True)
		templateNoteBuilder1.Origin.SetInferRelativeToGeometry(True)
		templateNoteBuilder1.Origin.SetInferRelativeToGeometry(False)          
		templateNoteBuilder1.Origin.SetInferRelativeToGeometry(False)

		leaderData1 = part2.Annotations.CreateLeaderData()
		leaderData1.StubSize = 5.0
		leaderData1.Arrowhead = NXOpen.Annotations.LeaderData.ArrowheadType.FilledArrow
		leaderData1.VerticalAttachment = NXOpen.Annotations.LeaderVerticalAttachment.Center
		templateNoteBuilder1.Leader.Leaders.Append(leaderData1)
		leaderData1.StubSide = NXOpen.Annotations.LeaderSide.Inferred

		symbolscale1 = templateNoteBuilder1.Text.TextBlock.SymbolScale
		symbolaspectratio1 = templateNoteBuilder1.Text.TextBlock.SymbolAspectRatio
		
		templateNoteBuilder1.Style.LetteringStyle.GeneralTextColor = part2.Colors.Find("Black")
		templateNoteBuilder1.Style.LetteringStyle.GeneralTextFont = 1
		templateNoteBuilder1.Style.LetteringStyle.GeneralTextItalicized = False
		templateNoteBuilder1.Style.LetteringStyle.GeneralTextLineWidth = NXOpen.Annotations.LineWidth.Thin
		templateNoteBuilder1.Style.LetteringStyle.GeneralTextSize = 2.0
		templateNoteBuilder1.Style.LetteringStyle.HorizontalTextJustification = NXOpen.Annotations.TextJustification.Left
		templateNoteBuilder1.Origin.SetInferRelativeToGeometry(False)
		templateNoteBuilder1.Origin.SetInferRelativeToGeometry(False)
		templateNoteBuilder1.Origin.SetInferRelativeToGeometry(False)
		
		templateNoteBuilder1.Text.TextBlock.SetText(output_1)
		templateNoteBuilder1.Style.LetteringStyle.GeneralTextSize = 2.0
		templateNoteBuilder1.Commit()
		templateNoteBuilder1.Destroy()

		# -- Second column of table tool list --
		genericNote2 = part2.FindObject("ENTITY 25 1 1")
		templateNoteBuilder2 = theTDPManager.CreateTemplateNoteBuilder(part2, genericNote2)

		templateNoteBuilder2.Text.TextBlock.CustomSymbolScale = 1.0
		templateNoteBuilder2.Origin.SetInferRelativeToGeometry(True)
		templateNoteBuilder2.Origin.SetInferRelativeToGeometry(False)
		templateNoteBuilder2.Origin.SetInferRelativeToGeometry(False)
		templateNoteBuilder2.Origin.SetInferRelativeToGeometry(False)

		leaderData2 = part2.Annotations.CreateLeaderData()
		leaderData2.StubSize = 5.0
		leaderData2.Arrowhead = NXOpen.Annotations.LeaderData.ArrowheadType.FilledArrow
		leaderData2.VerticalAttachment = NXOpen.Annotations.LeaderVerticalAttachment.Center
		templateNoteBuilder2.Leader.Leaders.Append(leaderData2)
		leaderData2.StubSide = NXOpen.Annotations.LeaderSide.Inferred

		symbolscale2 = templateNoteBuilder2.Text.TextBlock.SymbolScale
		symbolaspectratio2 = templateNoteBuilder2.Text.TextBlock.SymbolAspectRatio

		templateNoteBuilder2.Style.LetteringStyle.GeneralTextColor = part2.Colors.Find("Black")
		templateNoteBuilder2.Style.LetteringStyle.GeneralTextFont = 1
		templateNoteBuilder2.Style.LetteringStyle.GeneralTextItalicized = False
		templateNoteBuilder2.Style.LetteringStyle.GeneralTextLineWidth = NXOpen.Annotations.LineWidth.Thin
		templateNoteBuilder2.Style.LetteringStyle.GeneralTextSize = 2.0
		templateNoteBuilder2.Style.LetteringStyle.HorizontalTextJustification = NXOpen.Annotations.TextJustification.Left
		templateNoteBuilder2.Origin.SetInferRelativeToGeometry(False)
		templateNoteBuilder2.Origin.SetInferRelativeToGeometry(False)
		templateNoteBuilder2.Origin.SetInferRelativeToGeometry(False)

		templateNoteBuilder2.Text.TextBlock.SetText(output_2)
		templateNoteBuilder2.Style.LetteringStyle.GeneralTextSize = 2.0
		templateNoteBuilder2.Commit()
		templateNoteBuilder2.Destroy()
		   


if __name__ == '__main__':
	print_nx = IFTCore.print_nx
	tool_collection = IFTToolCollection()
	# -- GENERATE TOOL INSTANCES -- 
	tools = list()
	for i in range(tool_collection.nx_counter):
		tool = IFTTool(tool_collection, i)
		tool.get_data_attributes()

	IFTPDF.export_cam_pdf(tool_collection)



