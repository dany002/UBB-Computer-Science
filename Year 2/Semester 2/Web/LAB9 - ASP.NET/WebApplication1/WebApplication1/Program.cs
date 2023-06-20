using System.Configuration;
using System.Text;
using Microsoft.IdentityModel.Tokens;
using WebApplication1.Controllers;
using System.IdentityModel.Tokens.Jwt;
using Microsoft.AspNetCore.Authentication.JwtBearer;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(builder =>
    {
        builder.AllowAnyOrigin()
            .AllowAnyMethod()
            .AllowAnyHeader();
    });
});


// Add services to the container.
builder.Services.AddControllersWithViews();
IConfiguration configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("appsettings.json")
    .Build();
builder.Services.AddSingleton(configuration);
builder.Services.AddDbContext<WebApplication1.Repository.DocumentsRepository>();
builder.Services.AddDbContext<WebApplication1.Repository.UserRepository>();
builder.Services.AddSingleton<UserController>();


// Configure JWT authentication
var secretKey = Encoding.ASCII.GetBytes("ejroigjeoifgjsroigfkapwdofwefawdfwaegeafwdfwd");

builder.Services.AddAuthentication(options =>
    {
        options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
        options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
    })
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuerSigningKey = true,
            IssuerSigningKey = new SymmetricSecurityKey(secretKey),
            ValidateIssuer = false,
            ValidateAudience = false
        };
    });



var app = builder.Build();

// Configure the HTTP request pipeline.


//app.UseHttpsRedirection();
app.UseStaticFiles();


app.UseRouting();



app.UseCors();

app.UseAuthentication();
app.UseAuthorization();


app.UseEndpoints(endpoints =>
{
    endpoints.MapControllerRoute(
        name: "default",
        pattern: "{controller=Home}/{action=Index}/{id?}");
    endpoints.MapControllerRoute(
        name: "documents",
        pattern: "Documents/{id?}",
        defaults: new { controller = "Documents", action = "Index" });
    endpoints.MapControllerRoute(
        name: "signin",
        pattern: "auth/signin",
        defaults: new { controller = "User", action = "SignIn" });
    endpoints.MapControllerRoute(
        name: "signup",
        pattern: "auth/signup",
        defaults: new { controller = "User", action = "SignUp" });
});


app.Run();
