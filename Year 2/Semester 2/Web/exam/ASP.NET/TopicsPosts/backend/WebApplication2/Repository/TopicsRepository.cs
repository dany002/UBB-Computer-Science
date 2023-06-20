using Microsoft.EntityFrameworkCore;
using WebApplication2.Models;

namespace WebApplication2.Repository;

public class TopicsRepository : DbContext
{
    private readonly IConfiguration _configuration;

    public TopicsRepository(IConfiguration configuration)
    {
        _configuration = configuration;
    }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseMySQL(_configuration["ConnectionStrings:DatabaseURL"]);
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

    }
}