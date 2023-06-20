namespace WebApplication2.Models;

public class Posts
{
    public int id { get; set; }
    
    public String user { get; set; }
    
    public int topicid { get; set; }
    
    public Topics Topics { get; set; }
    
    public String text { get; set; }
    
    public DateTime date { get; set; }
    
}