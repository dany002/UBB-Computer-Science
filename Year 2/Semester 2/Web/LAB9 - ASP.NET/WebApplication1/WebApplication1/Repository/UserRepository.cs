using Microsoft.EntityFrameworkCore;
using WebApplication1.Models;


namespace WebApplication1.Repository
{
    public class UserRepository: DbContext
    {
        public DbSet<User> User { get; set; }
        private readonly IConfiguration _configuration;

        public UserRepository(IConfiguration configuration)
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
            modelBuilder.Entity<User>(entity =>
            {
                entity.HasKey(e => e.id);
                entity.Property(e => e.id).IsRequired();
                entity.Property(e => e.username).IsRequired();
                entity.Property(e => e.password).IsRequired();
            });
        }
    }
}