
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

	private global::Gtk.Entry companyEntry;

	private global::Gtk.Entry seatsEntry;

	private global::Gtk.Entry priceEntry;

	private global::Gtk.Entry departureEntry;

	private global::Gtk.Entry destinationEntry;

	private global::Gtk.Label label2;

	private global::Gtk.Label label3;

	private global::Gtk.Label label4;

	private global::Gtk.Label label5;

	private global::Gtk.Label label6;

	protected virtual void Build()
	{
		global::Stetic.Gui.Initialize(this);
		// Widget MainWindow
		this.Name = "MainWindow";
		this.Title = global::Mono.Unix.Catalog.GetString("MainWindow");
		this.WindowPosition = ((global::Gtk.WindowPosition)(4));
		// Container child MainWindow.Gtk.Container+ContainerChild
		this.fixed1 = new global::Gtk.Fixed();
		this.fixed1.Name = "fixed1";
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
		this.childTreeview.WidthRequest = 600;
		this.childTreeview.HeightRequest = 300;
		this.childTreeview.CanFocus = true;
		this.childTreeview.Name = "childTreeview";
		this.GtkScrolledWindow1.Add(this.childTreeview);
		this.fixed1.Add(this.GtkScrolledWindow1);
		global::Gtk.Fixed.FixedChild w8 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.GtkScrolledWindow1]));
		w8.X = 703;
		w8.Y = 91;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.companyEntry = new global::Gtk.Entry();
		this.companyEntry.CanFocus = true;
		this.companyEntry.Name = "companyEntry";
		this.companyEntry.IsEditable = true;
		this.companyEntry.InvisibleChar = '●';
		this.fixed1.Add(this.companyEntry);
		global::Gtk.Fixed.FixedChild w9 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.companyEntry]));
		w9.X = 868;
		w9.Y = 513;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.seatsEntry = new global::Gtk.Entry();
		this.seatsEntry.CanFocus = true;
		this.seatsEntry.Name = "seatsEntry";
		this.seatsEntry.IsEditable = true;
		this.seatsEntry.InvisibleChar = '●';
		this.fixed1.Add(this.seatsEntry);
		global::Gtk.Fixed.FixedChild w10 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.seatsEntry]));
		w10.X = 867;
		w10.Y = 562;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.priceEntry = new global::Gtk.Entry();
		this.priceEntry.CanFocus = true;
		this.priceEntry.Name = "priceEntry";
		this.priceEntry.IsEditable = true;
		this.priceEntry.InvisibleChar = '●';
		this.fixed1.Add(this.priceEntry);
		global::Gtk.Fixed.FixedChild w11 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.priceEntry]));
		w11.X = 867;
		w11.Y = 611;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.departureEntry = new global::Gtk.Entry();
		this.departureEntry.CanFocus = true;
		this.departureEntry.Name = "departureEntry";
		this.departureEntry.IsEditable = true;
		this.departureEntry.InvisibleChar = '●';
		this.fixed1.Add(this.departureEntry);
		global::Gtk.Fixed.FixedChild w12 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.departureEntry]));
		w12.X = 867;
		w12.Y = 657;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.destinationEntry = new global::Gtk.Entry();
		this.destinationEntry.CanFocus = true;
		this.destinationEntry.Name = "destinationEntry";
		this.destinationEntry.IsEditable = true;
		this.destinationEntry.InvisibleChar = '●';
		this.fixed1.Add(this.destinationEntry);
		global::Gtk.Fixed.FixedChild w13 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.destinationEntry]));
		w13.X = 867;
		w13.Y = 706;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.label2 = new global::Gtk.Label();
		this.label2.Name = "label2";
		this.label2.LabelProp = global::Mono.Unix.Catalog.GetString("Purchase");
		this.fixed1.Add(this.label2);
		global::Gtk.Fixed.FixedChild w14 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.label2]));
		w14.X = 729;
		w14.Y = 519;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.label3 = new global::Gtk.Label();
		this.label3.Name = "label3";
		this.label3.LabelProp = global::Mono.Unix.Catalog.GetString("Tracer");
		this.fixed1.Add(this.label3);
		global::Gtk.Fixed.FixedChild w15 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.label3]));
		w15.X = 736;
		w15.Y = 568;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.label4 = new global::Gtk.Label();
		this.label4.Name = "label4";
		this.label4.LabelProp = global::Mono.Unix.Catalog.GetString("Due");
		this.fixed1.Add(this.label4);
		global::Gtk.Fixed.FixedChild w16 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.label4]));
		w16.X = 736;
		w16.Y = 619;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.label5 = new global::Gtk.Label();
		this.label5.Name = "label5";
		this.label5.LabelProp = global::Mono.Unix.Catalog.GetString("Type");
		this.fixed1.Add(this.label5);
		global::Gtk.Fixed.FixedChild w17 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.label5]));
		w17.X = 737;
		w17.Y = 665;
		// Container child fixed1.Gtk.Fixed+FixedChild
		this.label6 = new global::Gtk.Label();
		this.label6.Name = "label6";
		this.label6.LabelProp = global::Mono.Unix.Catalog.GetString("Destination");
		this.fixed1.Add(this.label6);
		global::Gtk.Fixed.FixedChild w18 = ((global::Gtk.Fixed.FixedChild)(this.fixed1[this.label6]));
		w18.X = 737;
		w18.Y = 714;
		this.Add(this.fixed1);
		if ((this.Child != null))
		{
			this.Child.ShowAll();
		}
		this.DefaultWidth = 1447;
		this.DefaultHeight = 789;
		this.Show();
		this.DeleteEvent += new global::Gtk.DeleteEventHandler(this.OnDeleteEvent);
		this.connectButton.Clicked += new global::System.EventHandler(this.connectBtn);
		this.parentTreeView.RowActivated += new global::Gtk.RowActivatedHandler(this.rowActiveParentTree);
		this.deleteButton.Clicked += new global::System.EventHandler(this.deleteBtn);
		this.updateButton.Clicked += new global::System.EventHandler(this.updateBtn);
		this.addButton.Clicked += new global::System.EventHandler(this.addBtn);
		this.childTreeview.RowActivated += new global::Gtk.RowActivatedHandler(this.ChildActivated);
	}
}
