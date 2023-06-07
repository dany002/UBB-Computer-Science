using WebApplication1.Models;
using Microsoft.EntityFrameworkCore;
using Pomelo.EntityFrameworkCore.MySql;

namespace WebApplication1.Repository
{
    public class DocumentsRepository: DbContext
    {
        public DbSet<Document> Document { get; set; }
        private readonly IConfiguration _configuration;

        public DocumentsRepository(IConfiguration configuration)
        {
            this._configuration = configuration;
        }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseMySql(_configuration["ConnectionStrings:DatabaseURL"], ServerVersion.AutoDetect(_configuration["ConnectionStrings:DatabaseURL"]));
            //optionsBuilder.UseMySQL(_configuration["ConnectionStrings:DatabaseURL"]);
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
            modelBuilder.Entity<Document>(entity =>
            {
                entity.HasKey(e => e.id);
                entity.Property(e => e.id).IsRequired();
                entity.Property(e => e.author).IsRequired();
                entity.Property(e => e.format).IsRequired();
                entity.Property(e => e.types).IsRequired();
                entity.Property(e => e.pages).IsRequired();
                entity.Property(e => e.title).IsRequired();
            });
        }

    } 
}
