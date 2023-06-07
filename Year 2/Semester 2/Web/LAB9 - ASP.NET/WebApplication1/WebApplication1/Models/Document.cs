namespace WebApplication1.Models;

public class Document
{
    public int id { get; set; }
    
    public String author { get; set; }
    
    public String title { get; set; }
    
    public int pages { get; set; }
    
    public String types { get; set; }
    
    public String format { get; set; }

    public Document()
    {
        author = "";
        title = "";
        pages = 0;
        types = "";
        format = "";
    }
}