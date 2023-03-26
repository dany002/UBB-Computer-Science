using System;
using Gtk;
using System.Data.SqlClient;
using System.Data;
using System.Collections.Generic;

public partial class MainWindow : Gtk.Window
{
    SqlConnection cs = new SqlConnection("Server=localhost;Database=TransportPublic;User Id=SA;Password=<daniel123456>;");
    //SqlConnection cs = new SqlConnection();
    //cs.ConnectionString = "Data source=sql1;" + "Initial Catalog=Transport" + "User  id=SA;" + "Password=<daniel123456>;";
    //http://172.17.0.2:1433/
    //SqlConnection cs = new SqlConnection( new SqlConnectionStringBuilder()
    //{
    //DataSource = "sql1",
    //InitialCatalog = "Transport",
    //UserID = "SA",
    //Password = "<daniel123456>"
    //}.ConnectionString
    //);
    //Console.WriteLine(cs.State);
    SqlDataAdapter da = new SqlDataAdapter();
    DataSet ds = new DataSet();
    DataSet ds1 = new DataSet();
    bool createdChild = false;


    public MainWindow() : base(Gtk.WindowType.Toplevel)
    {
        Build();
        //SqlConnection cs = new SqlConnection(connString);

        //dataGridView1.DataSource = ds.Tables[0];

    }

    protected void OnDeleteEvent(object sender, DeleteEventArgs a)
    {
        Application.Quit();
        a.RetVal = true;
    }



    protected void connectBtn(object sender, EventArgs e)
    {
        da.SelectCommand = new SqlCommand("SELECT * FROM Garage", cs);
        ds.Clear();

        da.Fill(ds);

        //Set the number of columns to type string 
        //(could use Row.DataType, but would require some work when adding values)

        DataTable table = ds.Tables[0];

        /*
        Console.WriteLine("ROWSSS");
        DataRowCollection row = ds.Tables["Garage"].Rows;
        Console.WriteLine(row[0]);
        Console.WriteLine("DONE");

        Label garage_id = new Label("Id");
        Label location = new Label("Location");
        Label number_of_trams = new Label("Number of trams");
        Label number_of_buses = new Label("Number of buses");
        Label capacity = new Label("Capacity");

        parentTable.Attach(garage_id, 0, 1, 0, 1);
        parentTable.Attach(location, 1, 2, 0, 1);
        parentTable.Attach(number_of_trams, 2, 3, 0, 1);
        parentTable.Attach(number_of_buses, 3, 4, 0, 1);
        parentTable.Attach(capacity, 4, 5, 0, 1);
        */

        TreeViewColumn garage_id = new TreeViewColumn();
        garage_id.Title = "ID";

        TreeViewColumn location = new TreeViewColumn();
        location.Title = "Location";

        TreeViewColumn number_of_trams = new TreeViewColumn();
        number_of_trams.Title = "Number of trams";

        TreeViewColumn number_of_buses = new TreeViewColumn();
        number_of_buses.Title = "Number of buses";

        TreeViewColumn capacity = new TreeViewColumn();
        capacity.Title = "Capacity";

        parentTreeView.AppendColumn(garage_id);
        parentTreeView.AppendColumn(location);
        parentTreeView.AppendColumn(number_of_trams);
        parentTreeView.AppendColumn(number_of_buses);
        parentTreeView.AppendColumn(capacity);


        CellRendererText idRenderer = new CellRendererText();
        CellRendererText locationRenderer = new CellRendererText();
        CellRendererText tramsRenderer = new CellRendererText();
        CellRendererText busesRenderer = new CellRendererText();
        CellRendererText capacityRenderer = new CellRendererText();


        // Add the CellRenderers to the columns
        garage_id.PackStart(idRenderer, true);
        location.PackStart(locationRenderer, true);
        number_of_trams.PackStart(tramsRenderer, true);
        number_of_buses.PackStart(busesRenderer, true);
        capacity.PackStart(capacityRenderer, true);



        // Set the attributes for the CellRenderers
        garage_id.AddAttribute(idRenderer, "text", 0);
        location.AddAttribute(locationRenderer, "text", 1);
        number_of_trams.AddAttribute(tramsRenderer, "text", 2);
        number_of_buses.AddAttribute(busesRenderer, "text", 3);
        capacity.AddAttribute(capacityRenderer, "text", 4);
        //Console.WriteLine(ds.Tables[0]);

        ListStore store = new ListStore(typeof(int), typeof(string), typeof(int), typeof(int), typeof(int));


        foreach (DataRow row in ds.Tables[0].Rows)
        {
            // Add a new node to the tree for each row in the DataSet
            TreeIter iter = store.AppendValues((int)row["garage_id"], row["location"].ToString(), (int)row["number_of_trams"], (int)row["number_of_buses"], (int)row["capacity"]);
        }


        parentTreeView.Model = store;


        /*
List<System.Type> colTypes = new List<System.Type>();
for (int col_it = 0; col_it < table.Columns.Count; col_it++)
{
    colTypes.Add(typeof(string));
}
ListStore resultListStore = new ListStore(colTypes.ToArray());

//Adding columns
for (int col_it = 0; col_it < table.Columns.Count; col_it++)
{
   parentTreeView.AppendColumn(table.Columns[col_it].ColumnName, new CellRendererText(), "text", col_it);
}

//Adding values
List<string> rowValues = new List<string>();
for (int row_it = 0; row_it < table.Rows.Count; row_it++)
{
    for (int col_it = 0; col_it < table.Columns.Count; col_it++)
    {
        rowValues.Add(table.Rows[row_it][col_it].ToString());
    }
    resultListStore.AppendValues(rowValues.ToArray());
    rowValues.Clear();
}
*/
        //updating model

        ShowAll();
    }

    protected void rowActiveParentTree(object o, RowActivatedArgs args)
    {

        TreeSelection selection = parentTreeView.Selection;
        int id = -1;
        if (selection.GetSelected(out TreeModel model, out TreeIter iter))
        {
            // Access the data in the active row
            id = (int)model.GetValue(iter, 0); // Assuming column 0 contains the data you want to access
            Console.WriteLine(id);
        }
        if(id != -1)
        {
            da.SelectCommand = new SqlCommand("SELECT * FROM Bus WHERE garage_id=@id", cs);
            da.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;
            ds1.Clear();
            ds1.Clear();
            da.Fill(ds1);
            /// ClientTreeView
            //clientDataGrid.DataSource = ds1.Tables[0];


            if (createdChild == false)
            {
                TreeViewColumn bus_id = new TreeViewColumn();
                bus_id.Title = "ID";

                TreeViewColumn company = new TreeViewColumn();
                company.Title = "Company";

                TreeViewColumn number_of_seats = new TreeViewColumn();
                number_of_seats.Title = "Number of seats";

                TreeViewColumn price = new TreeViewColumn();
                price.Title = "Price";

                TreeViewColumn departure = new TreeViewColumn();
                departure.Title = "Departure";

                TreeViewColumn destination = new TreeViewColumn();
                destination.Title = "Destination";

                TreeViewColumn garagee_id = new TreeViewColumn();
                garagee_id.Title = "Garage id";


                childTreeview.AppendColumn(bus_id);
                childTreeview.AppendColumn(company);
                childTreeview.AppendColumn(number_of_seats);
                childTreeview.AppendColumn(price);
                childTreeview.AppendColumn(departure);
                childTreeview.AppendColumn(destination);
                childTreeview.AppendColumn(garagee_id);


                CellRendererText bus_idRenderer = new CellRendererText();
                CellRendererText companyRenderer = new CellRendererText();
                CellRendererText seatsRenderer = new CellRendererText();
                CellRendererText priceRenderer = new CellRendererText();
                CellRendererText departureRenderer = new CellRendererText();
                CellRendererText destinationRenderer = new CellRendererText();
                CellRendererText garageRenderer = new CellRendererText();

                // Add the CellRenderers to the columns
                bus_id.PackStart(bus_idRenderer, true);
                company.PackStart(companyRenderer, true);
                number_of_seats.PackStart(seatsRenderer, true);
                price.PackStart(priceRenderer, true);
                departure.PackStart(departureRenderer, true);
                destination.PackStart(destinationRenderer, true);
                garagee_id.PackStart(garageRenderer, true);


                // Set the attributes for the CellRenderers
                bus_id.AddAttribute(bus_idRenderer, "text", 0);
                company.AddAttribute(companyRenderer, "text", 1);
                number_of_seats.AddAttribute(seatsRenderer, "text", 2);
                price.AddAttribute(priceRenderer, "text", 3);
                departure.AddAttribute(departureRenderer, "text", 4);
                destination.AddAttribute(destinationRenderer, "text", 5);
                garagee_id.AddAttribute(garageRenderer, "text", 6);
                //Console.WriteLine(ds.Tables[0]);

                ListStore storee = new ListStore(typeof(int), typeof(string), typeof(int), typeof(double), typeof(string), typeof(string), typeof(int));

                foreach (DataRow row in ds1.Tables[0].Rows)
                {
                    //Console.WriteLine(row["bus_id"].ToString() + row["company"].ToString() + row["number_of_seats"].ToString() + row["price"].ToString() + row["departure"].ToString() + row["destination"].ToString() + row["garage_id"].ToString());
                    Console.WriteLine(row["price"].GetType());
                }



                foreach (DataRow row in ds1.Tables[0].Rows)
                {
                    // Add a new node to the tree for each row in the DataSet
                    TreeIter iters = storee.AppendValues((int)row["bus_id"], row["company"].ToString(), (int)row["number_of_seats"], (double)row["price"], row["departure"].ToString(), row["destination"].ToString(), (int)row["garage_id"]);
                }


                childTreeview.Model = storee;
                createdChild = true;
            }
            else
            {
                ListStore storee = new ListStore(typeof(int), typeof(string), typeof(int), typeof(double), typeof(string), typeof(string), typeof(int));

                foreach (DataRow row in ds1.Tables[0].Rows)
                {
                    // Add a new node to the tree for each row in the DataSet
                    TreeIter iters = storee.AppendValues((int)row["bus_id"], row["company"].ToString(), (int)row["number_of_seats"], (double)row["price"], row["departure"].ToString(), row["destination"].ToString(), (int)row["garage_id"]);
                }
                childTreeview.Model = storee;

            }
        }
    }
}
