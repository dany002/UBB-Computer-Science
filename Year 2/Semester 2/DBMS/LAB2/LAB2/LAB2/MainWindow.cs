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

    private string getParentTableNameAsString()
    {
        return ConfigurationManager.AppSettings["ParentTableName"];
    }

    private List<string> getParentLabelNamesAsList()
    {
        return ConfigurationManager.AppSettings["ParentLabelNames"].Split(',').ToList();
    }

    private List<string> getParentTypesAsList()
    {
        return ConfigurationManager.AppSettings["ParentTypes"].Split(',').ToList();
    }

    protected void connectBtn(object sender, EventArgs e)
    {
        string selectParent = "SELECT * FROM " + getParentTableNameAsString();
        da.SelectCommand = new SqlCommand(selectParent, cs);
        ds.Clear();

        da.Fill(ds);

        List<string> ParentLabelNames = getParentLabelNamesAsList();


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
        List<string> list_of_types = getParentTypesAsList();


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


        object[] data = new object[getParentLabelNamesAsList().Count];

        foreach (DataRow row in ds.Tables[0].Rows)
        {
            // Add a new node to the tree for each row in the DataSet
            for (int j = 0; j < data.Length; j++)
                data[j] = row[j];
            store.AppendValues(data);

        }


        parentTreeView.Model = store;
        //updating model

        ShowAll();
    }

    private string getChildTableNameAsString()
    {
        return ConfigurationManager.AppSettings["ChildTableName"];
    }

    private List<string> getChildLabelNamesAsList()
    {
        return ConfigurationManager.AppSettings["ChildLabelNames"].Split(',').ToList();
    }

    private List<string> getChildTypesAsList()
    {
        return ConfigurationManager.AppSettings["ChildTypes"].Split(',').ToList();
    }

    private void makeEntriesEmpty()
    {
        foreach(Entry entry in entries)
        {
            entry.Text = "";
        }
    }

    private void reloadChildTreeView()
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
            string sqlCommand = "SELECT * FROM " + getChildTableNameAsString() + " WHERE " + getParentLabelNamesAsList()[0] + "=@id";
            //da.SelectCommand = new SqlCommand("SELECT * FROM Bus WHERE garage_id=@id", cs);
            da.SelectCommand = new SqlCommand(sqlCommand, cs);
            da.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;
            ds1.Clear();
            ds1.Clear();
            da.Fill(ds1);

            List<string> list_of_types = getChildTypesAsList();
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

            object[] data = new object[getChildLabelNamesAsList().Count];

            foreach (DataRow row in ds1.Tables[0].Rows)
            {
                // Add a new node to the tree for each row in the DataSet
                for (int j = 0; j < data.Length; j++)
                    data[j] = row[j];
                storee.AppendValues(data);

            }

            childTreeview.Model = storee;
        }
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
            string sqlCommand = "SELECT * FROM " + getChildTableNameAsString() + " WHERE " + getParentLabelNamesAsList()[0] + "=@id";
            //da.SelectCommand = new SqlCommand("SELECT * FROM Bus WHERE garage_id=@id", cs);
            da.SelectCommand = new SqlCommand(sqlCommand, cs);
            da.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;
            ds1.Clear();
            ds1.Clear();
            da.Fill(ds1);


            if (createdChild == false)
            {

                List<string> ChildLabelNames = getChildLabelNamesAsList();
                ChildLabelNames.RemoveAt(ChildLabelNames.Count - 1); // we dont need foreign key to parent.

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


                List<string> list_of_types = getChildTypesAsList();
                list_of_types.RemoveAt(list_of_types.Count - 1); // we dont need foreign key type to parent.

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


                object[] data = new object[getChildLabelNamesAsList().Count];

                foreach (DataRow row in ds1.Tables[0].Rows)
                {
                    // Add a new node to the tree for each row in the DataSet
                    for (int j = 0; j < data.Length; j++)
                        data[j] = row[j];
                    storee.AppendValues(data);

                }


                childTreeview.Model = storee;

                createdChild = true;
            }
            else
            {
                reloadChildTreeView();

            }
        }
    }

    private bool checkEmptyEntries()
    {
        foreach (Entry entry in entries)
        {
            if (entry.Text.Length == 0)
                return false;
        }
        return true;
    }

    private string getChildLabelNamesAsString()
    {
        return ConfigurationManager.AppSettings["ChildLabelNames"];
    }

    private List<SqlDbType> getSqlDbTypesAsList(List<string> types)
    {

        List<SqlDbType> dbTypes = new List<SqlDbType>();
        int i = 0;
        foreach (string type in types)
        {
            if (type.Equals("int"))
            {
                dbTypes.Add(new SqlDbType());
                dbTypes[i] = SqlDbType.Int;
            }
            else if (type.Equals("string"))
            {
                dbTypes.Add(new SqlDbType());
                dbTypes[i] = SqlDbType.VarChar;
            }
            else if (type.Equals("float"))
            {
                dbTypes.Add(new SqlDbType());
                dbTypes[i] = SqlDbType.Float;
            }
            else if (type.Equals("short"))
            {
                dbTypes.Add(new SqlDbType());
                dbTypes[i] = SqlDbType.SmallInt;
            }
            i++;
        }
        return dbTypes;
    }

    protected void addBtn(object sender, EventArgs e)
    {
        if (firstFree == -1)
        {
            string helpCommand = "SELECT * FROM " + getChildTableNameAsString();
            da.SelectCommand = new SqlCommand(helpCommand, cs);
            DataSet helpData = new DataSet();
            helpData.Clear();
            da.Fill(helpData);
            string id = getChildLabelNamesAsList()[0];
            foreach (DataRow row in helpData.Tables[0].Rows)
            {
                firstFree = (int)row[id];
            }
        }

        try
        {

            if(checkEmptyEntries() == false)
            {
                MessageDialog md = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "One of the fields is empty!");
                md.Run();
                md.Destroy();
            }

            string build_insert = "INSERT INTO " + getChildTableNameAsString() + "(" + getChildLabelNamesAsString() + ") VALUES(";
            List<string> add_at_before_variables = getChildLabelNamesAsList();

            for (int j = 0; j < add_at_before_variables.Count - 1; j++)
                add_at_before_variables[j] = "@" + add_at_before_variables[j] + ", ";

            add_at_before_variables[add_at_before_variables.Count - 1] = "@" + add_at_before_variables[add_at_before_variables.Count - 1];

            foreach(string variable in add_at_before_variables)
            {
                build_insert += variable;
            }

            build_insert += ")";
            List<string> childLabelNames = getChildLabelNamesAsList();

            da.InsertCommand = new SqlCommand(build_insert, cs);
            firstFree++;

            da.InsertCommand.Parameters.Add("@" + childLabelNames[0], SqlDbType.Int).Value = firstFree;

            childLabelNames.RemoveAt(0);

            List<string> types = getChildTypesAsList();
            types.RemoveAt(0); // remove primary key.


            List<SqlDbType> dbTypes = getSqlDbTypesAsList(types);

            int i;
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
            reloadChildTreeView();
            makeEntriesEmpty();

        }
        catch (Exception ex)
        {
            MessageDialog mds1 = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, ex.ToString());
            mds1.Run();
            mds1.Destroy();
            cs.Close();
        }
    }

    protected void deleteBtn(object sender, EventArgs e)
    {
        try
        {
            string helpCommand = "DELETE FROM " + getChildTableNameAsString() + " WHERE ";
            List<string> ChildLabelNames = getChildLabelNamesAsList();
            helpCommand += ChildLabelNames.ElementAt(0) + "=@id";
            da.DeleteCommand = new SqlCommand(helpCommand, cs);

            TreeSelection selection = childTreeview.Selection;
            int id = -1;
            if (selection.GetSelected(out TreeModel model, out TreeIter iter))
            {
                // Access the data in the active row
                id = (int)model.GetValue(iter, 0); // Assuming column 0 contains the data you want to access
            }
            if (id == -1)
            {
                MessageDialog mds = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "Yooo! Select the child first..");
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
            reloadChildTreeView();
            makeEntriesEmpty();

        }
        catch (Exception ex)
        {
            MessageDialog mds1 = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, ex.ToString());
            mds1.Run();
            mds1.Destroy();
            cs.Close();
        }
    }
    protected void updateBtn(object sender, EventArgs e)
    {
        try
        {
            if(checkEmptyEntries() == false)
            {
                MessageDialog md = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "One of the fields is empty!");
                md.Run();
                md.Destroy();
            }

            string helpCommand = "UPDATE " + getChildTableNameAsString() + " SET ";
            List<string> childLabelNamesWithoutFK = getChildLabelNamesAsList();
            childLabelNamesWithoutFK.RemoveAt(childLabelNamesWithoutFK.Count - 1); // remove foreign key to parent.

            int i;
            for (i = 1; i < childLabelNamesWithoutFK.Count; i++)
            {
                if (i != childLabelNamesWithoutFK.Count - 1)
                    helpCommand += childLabelNamesWithoutFK[i] + "=@" + childLabelNamesWithoutFK[i] + ", ";
                else
                    helpCommand += childLabelNamesWithoutFK[i] + "=@" + childLabelNamesWithoutFK[i];
            }
            helpCommand += " WHERE " + childLabelNamesWithoutFK[0] + "=@" + childLabelNamesWithoutFK[0];

            Console.WriteLine(helpCommand);


            da.UpdateCommand = new SqlCommand(helpCommand, cs);


            List<string> types = getChildTypesAsList();
            types.RemoveAt(0); // remove primary key
            types.RemoveAt(types.Count - 1); // remove foreign key

            List<SqlDbType> dbTypes = getSqlDbTypesAsList(types);


            for (i = 0; i < types.Count; i++)
            {

                if (dbTypes[i] == SqlDbType.Int)
                {
                    da.UpdateCommand.Parameters.Add("@" + childLabelNamesWithoutFK[i+1], dbTypes[i]).Value = int.Parse(entries[i].Text);
                }
                else if (dbTypes[i] == SqlDbType.VarChar)
                {
                    da.UpdateCommand.Parameters.Add("@" + childLabelNamesWithoutFK[i+1], dbTypes[i]).Value = entries[i].Text.Trim();
                }
                else if (dbTypes[i] == SqlDbType.Float)
                {
                    da.UpdateCommand.Parameters.Add("@" + childLabelNamesWithoutFK[i+1], dbTypes[i]).Value = double.Parse(entries[i].Text);
                }
                else if (dbTypes[i] == SqlDbType.SmallInt)
                {
                    da.UpdateCommand.Parameters.Add("@" + childLabelNamesWithoutFK[i+1], dbTypes[i]).Value = short.Parse(entries[i].Text);
                }
            }
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
            da.UpdateCommand.Parameters.Add("@" + childLabelNamesWithoutFK[0], SqlDbType.Int).Value = id;

            cs.Open();
            da.UpdateCommand.ExecuteNonQuery();
            MessageDialog mds = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, "Updated succesfully to the Database");
            mds.Run();
            mds.Destroy();
            cs.Close();
            reloadChildTreeView();
            makeEntriesEmpty();

        }
        catch (Exception ex)
        {
            MessageDialog mds1 = new MessageDialog(null, DialogFlags.DestroyWithParent, MessageType.Error, ButtonsType.Ok, ex.ToString());
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
            for (int i = 0; i < entries.Count; i++)
                entries[i].Text = model.GetValue(iter, i + 1).ToString();
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