using Microsoft.EntityFrameworkCore;
using WebApplication2.Models;

namespace WebApplication2.Repository;

public class PostsRepository : DbContext
{
    public DbSet<Posts> Posts { get; set; }
    public DbSet<Topics> Topics { get; set; }

    private readonly IConfiguration _configuration;

    public PostsRepository(IConfiguration configuration)
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
        modelBuilder.Entity<Posts>(entity =>
        {
            entity.HasKey(e => e.id);
            entity.Property(e => e.id).IsRequired();
            entity.Property(e => e.user).IsRequired();
            entity.Property(e => e.date).IsRequired();
            entity.Property(e => e.text).IsRequired();
            entity.Property(e => e.topicid).IsRequired();
        });
        
        modelBuilder.Entity<Topics>(entity =>
        {
            entity.HasKey(e => e.id);
            entity.Property(e => e.id).IsRequired();
            entity.Property(e => e.topicname).IsRequired();
        });
    }
}