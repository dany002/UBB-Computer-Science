using System;
using Gtk;
using System.Data.SqlClient;
using System.Data;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;

public partial class MainWindow : Gtk.Window
{
    //SqlConnection cs = new SqlConnection("Server=localhost;Database=TransportPublic;User Id=SA;Password=<daniel123456>;");
    SqlConnection cs = new SqlConnection(ConfigurationManager.ConnectionStrings["cs"].ConnectionString.ToString());
    SqlDataAdapter da = new SqlDataAdapter();
    DataSet ds = new DataSet();
    DataSet ds1 = new DataSet();
    bool createdChild = false;
    int firstFree = -1;

    List<Entry> entries = new List<Entry>();


    public MainWindow() : base(Gtk.WindowType.Toplevel)
    {
        Build();

    }

    protected void OnDeleteEvent(object sender, DeleteEventArgs a)
    {
        Application.Quit();
        a.RetVal = true;
    }

    protected void connectBtn(object sender, EventArgs e)
    {
        string selectParent = "SELECT * FROM " + ConfigurationManager.AppSettings["ParentTableName"];
        da.SelectCommand = new SqlCommand(selectParent, cs);
        ds.Clear();

        da.Fill(ds);

        List<string> ParentLabelNames = ConfigurationManager.AppSettings["ParentLabelNames"].Split(',').ToList();


        List<TreeViewColumn> columns = new List<TreeViewColumn>();
        int i = 0;

        for (i = 0; i < ParentLabelNames.Count; i++)
        {
            columns.Add(new TreeViewColumn());
            columns[i].Title = ParentLabelNames[i];
            parentTreeView.AppendColumn(columns[i]);
        }

        List<CellRendererText> cells = new List<CellRendererText>(ParentLabelNames.Count);
        for (i = 0; i < ParentLabelNames.Count; i++)
        {
            cells.Add(new CellRendererText());
            columns.ElementAt(i).PackStart(cells.ElementAt(i), true); // Add the CellRenderers to the columns
            columns.ElementAt(i).AddAttribute(cells.ElementAt(i), "text", i); // Set the attrivutes for columns.
        }
        List<string> list_of_types = ConfigurationManager.AppSettings["ParentTypes"].Split(',').ToList();


        Type[] types = new Type[list_of_types.Count];

        i = 0;

        foreach (string type in list_of_types)
        {
            if (type.Equals("int"))
            {
                types[i] = typeof(int);
            }
            else if (type.Equals("string"))
            {
                types[i] = typeof(string);
            }
            else if (type.Equals("float"))
            {
                types[i] = typeof(double);
            }
            else if (type.Equals("short"))
            {
                types[i] = typeof(Int16);
            }
            i++;
        }

        ListStore store = new ListStore(types);


        foreach (DataRow row in ds.Tables[0].Rows)
        {
            // Add a new node to the tree for each row in the DataSet
            store.AppendValues(row["garage_id"], row["location"], row["number_of_trams"], row["number_of_buses"], row["capacity"]);

        }


        parentTreeView.Model = store;
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
        }
        if (id != -1)
        {
            string sqlCommand = "SELECT * FROM " + ConfigurationManager.AppSettings["ChildTableName"] + " WHERE " + ConfigurationManager.AppSettings["ParentLabelNames"].Split(',').ToList()[0] + "=@id";
            //da.SelectCommand = new SqlCommand("SELECT * FROM Bus WHERE garage_id=@id", cs);
            da.SelectCommand = new SqlCommand(sqlCommand, cs);
            da.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;
            ds1.Clear();
            ds1.Clear();
            da.Fill(ds1);


            if (createdChild == false)
            {

                List<string> ChildLabelNames = ConfigurationManager.AppSettings["ChildLabelNames"].Split(',').ToList();
                ChildLabelNames.RemoveAt(ChildLabelNames.Count - 1);

                List<TreeViewColumn> columns = new List<TreeViewColumn>();
                int i = 0;

                for (i = 0; i < ChildLabelNames.Count; i++)
                {
                    columns.Add(new TreeViewColumn());
                    columns[i].Title = ChildLabelNames[i];
                    childTreeview.AppendColumn(columns[i]);
                }

                List<CellRendererText> cells = new List<CellRendererText>(ChildLabelNames.Count);
                for (i = 0; i < ChildLabelNames.Count; i++)
                {
                    cells.Add(new CellRendererText());
                    columns.ElementAt(i).PackStart(cells.ElementAt(i), true); // Add the CellRenderers to the columns
                    columns.ElementAt(i).AddAttribute(cells.ElementAt(i), "text", i); // Set the attrivutes for columns.
                }


                List<string> list_of_types = ConfigurationManager.AppSettings["ChildTypes"].Split(',').ToList();
                list_of_types.RemoveAt(list_of_types.Count - 1);

                Type[] types = new Type[list_of_types.Count];

                i = 0;

                foreach (string type in list_of_types)
                {
                    if (type.Equals("int"))
                    {
                        types[i] = typeof(int);
                    }
                    else if (type.Equals("string"))
                    {
                        types[i] = typeof(string);
                    }
                    else if (type.Equals("float"))
                    {
                        types[i] = typeof(double);
                    }
                    else if (type.Equals("short"))
                    {
                        types[i] = typeof(Int16);
                    }
                    i++;
                }

                ListStore storee = new ListStore(types);


                foreach (DataRow row in ds1.Tables[0].Rows)
                {
                    // Add a new node to the tree for each row in the DataSet
                    TreeIter iters = storee.AppendValues((int)row["bus_id"], row["company"].ToString(), (int)row["number_of_seats"], (double)row["price"], row["departure"].ToString(), row["destination"].ToString());

                }

                childTreeview.Model = storee;

                createdChild = true;
            }
            else
            {
                List<string> list_of_types = ConfigurationManager.AppSettings["ChildTypes"].Split(',').ToList();
                list_of_types.RemoveAt(list_of_types.Count - 1);

                Type[] types = new Type[list_of_types.Count];

                int i = 0;

                foreach (string type in list_of_types)
                {
                    if (type.Equals("int"))
                    {
                        types[i] = typeof(int);
                    }
                    else if (type.Equals("string"))
                    {
                        types[i] = typeof(string);
                    }
                    else if (type.Equals("float"))
                    {
                        types[i] = typeof(double);
                    }
                    else if (type.Equals("short"))
                    {
                        types[i] = typeof(Int16);
                    }
                    i++;
                }

                ListStore storee = new ListStore(types);


                foreach (DataRow row in ds1.Tables[0].Rows)
                {
                    // Add a new node to the tree for each row in the DataSet
                    TreeIter iters = storee.AppendValues((int)row["bus_id"], row["company"].ToString(), (int)row["number_of_seats"], (double)row["price"], row["departure"].ToString(), row["destination"].ToString());

                }

                childTreeview.Model = storee;

            }
        }
    }

    protected void addBtn(object sender, EventArgs e)
    {
        if (firstFree == -1)
        {
            string helpCommand = "SELECT * FROM " + ConfigurationManager.AppSettings["ChildTableName"];
            da.SelectCommand = new SqlCommand(helpCommand, cs);
            DataSet helpData = new DataSet();
            helpData.Clear();
            da.Fill(helpData);
            string id = ConfigurationManager.AppSettings["ChildLabelNames"].Split(',').ToList()[0];
            foreach (DataRow row in helpData.Tables[0].Rows)
            {
                firstFree = (int)row[id];
            }
        }

        try
        {
            foreach(Entry entry in entries)
            {
                if(entry.Text.Length == 0)
                {
                    MessageDialog md = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "One of the fields is empty!");
                    md.Run();
                    md.Destroy();
                }
            }
            string build_insert = "INSERT INTO " + ConfigurationManager.AppSettings["ChildTableName"] + "(" + ConfigurationManager.AppSettings["ChildLabelNames"] + ") VALUES(";
            List<string> add_at_before_variables = ConfigurationManager.AppSettings["ChildLabelNames"].Split(',').ToList();

            for (int j = 0; j < add_at_before_variables.Count - 1; j++)
                add_at_before_variables[j] = "@" + add_at_before_variables[j] + ", ";

            add_at_before_variables[add_at_before_variables.Count - 1] = "@" + add_at_before_variables[add_at_before_variables.Count - 1];

            foreach(string variable in add_at_before_variables)
            {
                build_insert += variable;
            }

            build_insert += ")";
            List<string> childLabelNames = ConfigurationManager.AppSettings["ChildLabelNames"].Split(',').ToList();

            da.InsertCommand = new SqlCommand(build_insert, cs);
            firstFree++;

            da.InsertCommand.Parameters.Add("@" + childLabelNames[0], SqlDbType.Int).Value = firstFree;

            childLabelNames.RemoveAt(0);

            List<string> types = ConfigurationManager.AppSettings["ChildTypes"].Split(',').ToList();
            types.RemoveAt(0);


            List<SqlDbType> dbTypes = new List<SqlDbType>();
            int i = 0;
            foreach(string type in types)
            {
                if (type.Equals("int"))
                {
                    dbTypes.Add(new SqlDbType());
                    dbTypes[i] = SqlDbType.Int;
                }
                else if(type.Equals("string"))
                {
                    dbTypes.Add(new SqlDbType());
                    dbTypes[i] = SqlDbType.VarChar;
                }
                else if (type.Equals("float"))
                {
                    dbTypes.Add(new SqlDbType());
                    dbTypes[i] = SqlDbType.Float;
                }
                else if(type.Equals("short"))
                {
                    dbTypes.Add(new SqlDbType());
                    dbTypes[i] = SqlDbType.SmallInt;
                }
                i++;
            }

            for (i = 0; i < types.Count - 1; i++)
            {
                if(dbTypes[i] == SqlDbType.Int)
                {
                    da.InsertCommand.Parameters.Add("@" + childLabelNames[i], dbTypes[i]).Value = int.Parse(entries[i].Text);
                }
                else if(dbTypes[i] == SqlDbType.VarChar)
                {
                    da.InsertCommand.Parameters.Add("@" + childLabelNames[i], dbTypes[i]).Value = entries[i].Text.Trim();
                }
                else if(dbTypes[i] == SqlDbType.Float)
                {
                    da.InsertCommand.Parameters.Add("@" + childLabelNames[i], dbTypes[i]).Value = double.Parse(entries[i].Text);
                }
                else if(dbTypes[i] == SqlDbType.SmallInt)
                {
                    da.InsertCommand.Parameters.Add("@" + childLabelNames[i], dbTypes[i]).Value = short.Parse(entries[i].Text);

                }
            }

            TreeSelection selection = parentTreeView.Selection;
            int id = -1;
            if (selection.GetSelected(out TreeModel model, out TreeIter iter))
            {
                // Access the data in the active row
                id = (int)model.GetValue(iter, 0); // Assuming column 0 contains the data you want to access
            }

            da.InsertCommand.Parameters.Add("@" + childLabelNames[childLabelNames.Count - 1], SqlDbType.Int).Value = id;
            cs.Open();
            da.InsertCommand.ExecuteNonQuery();
            MessageDialog mds = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "Inserted succesfully to the Database");
            mds.Run();
            mds.Destroy();
            cs.Close();
        }
        catch (Exception)
        {
            MessageDialog mds1 = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "There was an error.");
            mds1.Run();
            mds1.Destroy();
            cs.Close();
        }
    }

    protected void deleteBtn(object sender, EventArgs e)
    {
        try
        {
            da.DeleteCommand = new SqlCommand("DELETE FROM Bus WHERE bus_id=@id", cs);

            TreeSelection selection = childTreeview.Selection;
            int id = -1;
            if (selection.GetSelected(out TreeModel model, out TreeIter iter))
            {
                // Access the data in the active row
                id = (int)model.GetValue(iter, 0); // Assuming column 0 contains the data you want to access
            }
            if (id == -1)
            {
                MessageDialog mds = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "Yooo! Select a bus first..");
                mds.Run();
                mds.Destroy();
                throw new Exception("error");
            }
            da.DeleteCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;
            cs.Open();
            da.DeleteCommand.ExecuteNonQuery();
            MessageDialog md = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "Deleted successfully!");
            md.Run();
            md.Destroy();
            cs.Close();

        }
        catch (Exception)
        {
            MessageDialog mds1 = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "There was an error.");
            mds1.Run();
            mds1.Destroy();
            cs.Close();
        }
    }
    protected void updateBtn(object sender, EventArgs e)
    {
        try
        {
            /*
            if (companyEntry.Text.Length == 0 || seatsEntry.Text.Length == 0 || priceEntry.Text.Length == 0 || departureEntry.Text.Length == 0 || destinationEntry.Text.Length == 0)
            {
                MessageDialog md = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "One of the fields is empty!");
                md.Run();
                md.Destroy();
            }
            da.UpdateCommand = new SqlCommand("UPDATE Bus SET company=@company,number_of_seats=@number_of_seats, price=@price, departure=@departure, destination=@destination WHERE bus_id=@bus_id", cs);
            da.UpdateCommand.Parameters.Add("@company", SqlDbType.VarChar).Value = companyEntry.Text.Trim();
            da.UpdateCommand.Parameters.Add("@number_of_seats", SqlDbType.Int).Value = int.Parse(seatsEntry.Text);
            da.UpdateCommand.Parameters.Add("@price", SqlDbType.Float).Value = Double.Parse(priceEntry.Text);
            da.UpdateCommand.Parameters.Add("@departure", SqlDbType.VarChar).Value = departureEntry.Text.Trim();
            da.UpdateCommand.Parameters.Add("@destination", SqlDbType.VarChar).Value = destinationEntry.Text.Trim();
            */
            TreeSelection selection = childTreeview.Selection;
            int id = -1;
            if (selection.GetSelected(out TreeModel model, out TreeIter iter))
            {
                // Access the data in the active row
                id = (int)model.GetValue(iter, 0); // Assuming column 0 contains the data you want to access
            }
            if (id == -1)
            {
                MessageDialog mdss = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "Yooo! Select a bus first..");
                mdss.Run();
                mdss.Destroy();
                throw new Exception("error");
            }
            da.UpdateCommand.Parameters.Add("@bus_id", SqlDbType.Int).Value = id;
            Console.WriteLine("bus_id: ");
            Console.WriteLine(id);
            cs.Open();
            Console.WriteLine("HI");
            da.UpdateCommand.ExecuteNonQuery();
            Console.WriteLine("WOW");
            MessageDialog mds = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "Updated succesfully to the Database");
            mds.Run();
            mds.Destroy();
            cs.Close();

        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.ToString());
            MessageDialog mds1 = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "There was an error.");
            mds1.Run();
            mds1.Destroy();
            cs.Close();
        }
    }

    protected void ChildActivated(object o, RowActivatedArgs args)
    {
        TreeSelection selection = childTreeview.Selection;
        if (selection.GetSelected(out TreeModel model, out TreeIter iter))
        {
            /*
            // Access the data in the active row
            companyEntry.Text = model.GetValue(iter, 1).ToString();
            seatsEntry.Text = model.GetValue(iter, 2).ToString();
            priceEntry.Text = model.GetValue(iter, 3).ToString();
            departureEntry.Text = model.GetValue(iter, 4).ToString();
            destinationEntry.Text = model.GetValue(iter, 5).ToString();
            */
            return;
        }
    }

    protected void populateFrame(object sender, EventArgs e)
    {

        List<string> childColumns = ConfigurationManager.AppSettings["ChildLabelNames"].Split(',').ToList();
        childColumns.RemoveAt(childColumns.Count - 1);
        childColumns.RemoveAt(0);



        Widget childWidget = entriesFrame.Child;
        if (childWidget != null)
        {
            entriesFrame.Remove(childWidget);
        }

        Table table = new Table((uint)childColumns.Count, 2, false);

        int i = 0;

        for (uint row = 0; row < childColumns.Count; row++)
        {
            entries.Add(new Entry());
            Label label = new Label(childColumns[i]);
            table.Attach(entries[i], 1, 2, row, row + 1, AttachOptions.Fill, AttachOptions.Fill, 0, 0);
            table.Attach(label, 0, 1, row, row + 1, AttachOptions.Fill, AttachOptions.Fill, 0, 0);
            i++;
        }


        // Add the table to the frame
        entriesFrame.Add(table);

        ShowAll();
    }


}