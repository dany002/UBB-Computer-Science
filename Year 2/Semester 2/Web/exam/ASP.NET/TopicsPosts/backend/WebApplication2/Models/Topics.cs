namespace WebApplication2.Models;

public class Topics
{
    public int id { get; set; }
    
    public String topicname { get; set; }
    
    public List<Posts> posts { get; set; }
}