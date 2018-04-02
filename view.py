import wx
import wx.xrc
import wx.grid as gridlib

OUTPUT_FILE = "output.txt"

class MainFrame(wx.Frame):

	def __init__(self, parent, title):

		wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size(500, 408), style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )
		panel = wx.Panel(self)

		sizer = wx.BoxSizer(wx.VERTICAL)

		# Variable Grid
		var_Grid = gridlib.Grid(panel)
		var_Grid.CreateGrid(7, 4)
		var_Grid.SetColLabelValue(0, "Name")
		var_Grid.SetColLabelValue(1, "Variance")
		var_Grid.SetColLabelValue(2, "Mean")
		var_Grid.SetColLabelValue(3, "Type of Distribution")

		var_Grid.AutoSizeColumn(3)

		self.var_Grid = var_Grid
		sizer.Add(self.var_Grid, 1, wx.EXPAND)

		# Equation Grid
		eql_grid = gridlib.Grid(panel)
		eql_grid.CreateGrid(6, 1)
		eql_grid.SetColLabelValue(0, "Equation Input")
		eql_grid.SetColSize(0, 350)

		eql_grid.CanDragColSize(True)
		eql_grid.EnableDragColSize(True)

		self.eql_grid = eql_grid
		sizer.Add(self.eql_grid, 1, wx.EXPAND)
		
		button = wx.Button(panel, id=wx.ID_ANY, label="Save", style=wx.TE_CENTER)
		button.Bind(wx.EVT_BUTTON, self.save)
		sizer.Add(button)

		panel.SetSizer(sizer)

	def save(self, event):

		with open(OUTPUT_FILE, 'w') as f:
			f.writelines("---------- Variables ---------- \n")
			for i in range(0, self.var_Grid.GetNumberRows()):
				f.write("Var{}: ".format(str(i)))
				for j in range(0, self.var_Grid.GetNumberCols()):
					f.write("{} ".format(str(self.var_Grid.GetCellValue(i, j))))
				f.writelines("\n")

			f.writelines("----- End of Variables ----- \n")

			f.writelines("\n---------- Equations ---------- \n")
			for i in range(0, self.eql_grid.GetNumberRows()):
				f.write("Eqn{}: ".format(str(i)))
				for j in range(0, self.eql_grid.GetNumberCols()):
					f.write("{} ".format(str(self.eql_grid.GetCellValue(i, j))))
				f.writelines("\n")

			f.writelines("----- End of Equations -----\n")

			f.writelines("End Input\n")

		print("Finish Writing to " + OUTPUT_FILE)

		self.Close()

if __name__ == '__main__':
	app = wx.App()
	frame = MainFrame(None, "GUI")
	frame.Show(True)
	app.MainLoop()


