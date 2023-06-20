using System.Diagnostics;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;
using WebApplication1.Models;
using WebApplication1.Repository;



namespace WebApplication1.Controllers;

[Route("auth")]
public class UserController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly UserRepository _usersRepository;
    
    
    private bool IsValidUser(string username, string password)
    {
        // Retrieve user from the database based on the username
        var user = _usersRepository.User.Where(e => e.username.Equals(username)).Single<User>();
        
        if (user != null)
        {
            Console.WriteLine("IS VALID USER" + password + user.password);
            // Compare the provided password with the stored password using a suitable comparison method
            // For example, if passwords are stored as hashed and salted values:
            bool passwordMatches = VerifyPassword(password, user.password);
            return passwordMatches;
        }

        return false;
    }

    private bool VerifyPassword(string password, string storedPasswordHash)
    {
        // Implement the logic to verify the provided password against the stored password hash and salt
        // For example, using a hashing algorithm like bcrypt:
        var hashedPassword = HashPassword(password);
        
        Console.WriteLine("password mathces? " + hashedPassword + "\n" + storedPasswordHash + "\n");

        return storedPasswordHash == hashedPassword;
    }

    private string HashPassword(string password)
    {
        // Implement the logic to hash the password using a suitable hashing algorithm, such as bcrypt
        // For example:
        var saltedPassword = $"{password}";
        var hashedPassword = BCrypt.Net.BCrypt.HashPassword(saltedPassword);

        return hashedPassword;
    }

    

    public UserController(ILogger<HomeController> logger, UserRepository userRepository)
    {
        _logger = logger;
        _usersRepository = userRepository;
    }
    
    public string GenerateJwtToken(string userId, string username, string secretKey)
    {
        var tokenHandler = new JwtSecurityTokenHandler();
        var key = Encoding.ASCII.GetBytes(secretKey);
        var tokenDescriptor = new SecurityTokenDescriptor
        {
            Subject = new ClaimsIdentity(new[]
            {
                new Claim(ClaimTypes.NameIdentifier, userId),
                new Claim(ClaimTypes.Name, username)
                // Add additional claims as needed
            }),
            Expires = DateTime.UtcNow.AddHours(1), // Token expiration time
            SigningCredentials = new SigningCredentials(new SymmetricSecurityKey(key), SecurityAlgorithms.HmacSha256Signature)
        };
        var token = tokenHandler.CreateToken(tokenDescriptor);
        return tokenHandler.WriteToken(token);
    }
    
    [HttpPost("signin")]
    public IActionResult SignIn([FromBody] SignInDTO model)
    {   
        
        var user = _usersRepository.User.SingleOrDefault(e => e.username.Equals(model.username));
        if (user != null)
        {
            
            // Validate user credentials
            //if (IsValidUser(user.username, model.password))
            Console.WriteLine(user.password);
            Console.WriteLine(HashPassword(model.password));
            Console.WriteLine("finish");
            if(BCrypt.Net.BCrypt.Verify(model.password, user.password))
            {
                Console.WriteLine("WOW");
                var secretKey = "ejroigjeoifgjsroigfkapwdofwefawdfwaegeafwdfwd";
                var token = GenerateJwtToken(user.id.ToString(), user.username, secretKey);
                return Ok(new { Token = token });
            }
            else
            {
                return Unauthorized();
            }
        }
        else
        {
            return NoContent();
        }
    }

    [HttpPost("signup")]
    public IActionResult SignUp([FromBody] SignUpDTO model)
    {
        

        // Check if the user already exists
        if (_usersRepository.User.Where(e => e.username.Equals(model.username)).SingleOrDefault<User>() != null)
        {
            return BadRequest("User already exists");
        }
        // Create the user account (e.g., store in the database)
        Console.WriteLine("HI");
        
        var newUser = new User 
        {
            username = model.username,
            password = HashPassword(model.password),
            name = model.name
            // Set other properties as needed
        };
        
        _usersRepository.Add(newUser);
        _usersRepository.SaveChanges();
        // Optionally, you can automatically sign in the user after successful sign-up
        //var token = GenerateJwtToken(userId, model.username, secretKey);
        //return Ok(new { Token = token });
        return Ok();
    }
    
    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}