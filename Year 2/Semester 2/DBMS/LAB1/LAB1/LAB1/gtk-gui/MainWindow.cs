
// This file has been generated by the GUI designer. Do not modify.

public partial class MainWindow
{
	private global::Gtk.Fixed fixed1;

	private global::Gtk.Button connectButton;

	private global::Gtk.ScrolledWindow GtkScrolledWindow;

	private global::Gtk.TreeView parentTreeView;

	private global::Gtk.Button deleteButton;

	private global::Gtk.Button updateButton;

	private global::Gtk.Button addButton;

	private global::Gtk.ScrolledWindow GtkScrolledWindow1;

	private global::Gtk.TreeView childTreeview;

	protected virtual void Build()
	{
		global::Stetic.Gui.Initialize(this);
		// Widget MainWindow
		this.Name = "MainWindow";
		this.Title = global::Mono.Unix.Catalog.GetString("MainWindow");
		this.WindowPosition = ((global::Gtk.WindowPosition)(4));
		// Container child MainWindow.Gtk.Container+ContainerChild
		this.fixed1 = new global::Gtk.Fixed();
		this.fixed1.HasWindow = false;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.connectButton = new global::Gtk.Button();
		this.connectButton.CanFocus = true;
		this.connectButton.Name = "connectButton";
		this.connectButton.UseUnderline = true;
		this.connectButton.Label = global::Mono.Unix.Catalog.GetString("Connect");
		this.fixed1.Add(this.connectButton);
		global::Gtk.Fixed.FixedChild w1 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.connectButton]));
		w1.X = 126;
		w1.Y = 33;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.GtkScrolledWindow = new global::Gtk.ScrolledWindow();
		this.GtkScrolledWindow.Name = "GtkScrolledWindow";
		this.GtkScrolledWindow.ShadowType = ((global::Gtk.ShadowType)(1));
		// Container child GtkScrolledWindow.Gtk.Container+ContainerChild
		this.parentTreeView = new global::Gtk.TreeView();
		this.parentTreeView.WidthRequest = 500;
		this.parentTreeView.HeightRequest = 300;
		this.parentTreeView.CanFocus = true;
		this.parentTreeView.Name = "parentTreeView";
		this.GtkScrolledWindow.Add(this.parentTreeView);
		this.fixed1.Add(this.GtkScrolledWindow);
		global::Gtk.Fixed.FixedChild w3 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.GtkScrolledWindow]));
		w3.X = 32;
		w3.Y = 95;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.deleteButton = new global::Gtk.Button();
		this.deleteButton.WidthRequest = 100;
		this.deleteButton.CanFocus = true;
		this.deleteButton.Name = "deleteButton";
		this.deleteButton.UseUnderline = true;
		this.deleteButton.Label = global::Mono.Unix.Catalog.GetString("Delete");
		this.fixed1.Add(this.deleteButton);
		global::Gtk.Fixed.FixedChild w4 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.deleteButton]));
		w4.X = 988;
		w4.Y = 456;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.updateButton = new global::Gtk.Button();
		this.updateButton.WidthRequest = 100;
		this.updateButton.CanFocus = true;
		this.updateButton.Name = "updateButton";
		this.updateButton.UseUnderline = true;
		this.updateButton.Label = global::Mono.Unix.Catalog.GetString("Update");
		this.fixed1.Add(this.updateButton);
		global::Gtk.Fixed.FixedChild w5 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.updateButton]));
		w5.X = 844;
		w5.Y = 454;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.addButton = new global::Gtk.Button();
		this.addButton.WidthRequest = 100;
		this.addButton.CanFocus = true;
		this.addButton.Name = "addButton";
		this.addButton.UseUnderline = true;
		this.addButton.Label = global::Mono.Unix.Catalog.GetString("Add");
		this.fixed1.Add(this.addButton);
		global::Gtk.Fixed.FixedChild w6 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.addButton]));
		w6.X = 687;
		w6.Y = 456;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.GtkScrolledWindow1 = new global::Gtk.ScrolledWindow();
		this.GtkScrolledWindow1.Name = "GtkScrolledWindow1";
		this.GtkScrolledWindow1.ShadowType = ((global::Gtk.ShadowType)(1));
		// Container child GtkScrolledWindow1.Gtk.Container+ContainerChild
		this.childTreeview = new global::Gtk.TreeView();
		this.childTreeview.WidthRequest = 500;
		this.childTreeview.HeightRequest = 300;
		this.childTreeview.CanFocus = true;
		this.childTreeview.Name = "childTreeview";
		this.GtkScrolledWindow1.Add(this.childTreeview);
		this.fixed1.Add(this.GtkScrolledWindow1);
		global::Gtk.Fixed.FixedChild w8 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.GtkScrolledWindow1]));
		w8.X = 703;
		w8.Y = 91;
		this.Add(this.fixed1);
		if ((this.Child != null))
		{
			this.Child.ShowAll();
		}
		this.DefaultWidth = 1447;
		this.DefaultHeight = 723;
		this.Show();
		this.DeleteEvent += new global::Gtk.DeleteEventHandler(this.OnDeleteEvent);
		this.connectButton.Clicked += new global::System.EventHandler(this.connectBtn);
		this.parentTreeView.RowActivated += new global::Gtk.RowActivatedHandler(this.rowActiveParentTree);
	}
}