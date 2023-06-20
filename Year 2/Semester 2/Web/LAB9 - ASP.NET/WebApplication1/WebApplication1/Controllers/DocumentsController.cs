using System.Diagnostics;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;
using WebApplication1.Models;
using WebApplication1.Repository;

namespace WebApplication1.Controllers;

public class DocumentsController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly DocumentsRepository _documentsRepository;

    public DocumentsController(ILogger<HomeController> logger, DocumentsRepository documentsRepository)
    {
        _logger = logger;
        _documentsRepository = documentsRepository;
    }
    
    [HttpGet]
    public IActionResult Index(int? id)
    {
        Console.WriteLine("HMM");
        string token = Request.Headers["Authorization"];

        // Validate and process the token
        var tokenHandler = new JwtSecurityTokenHandler();
        var validationParameters = new TokenValidationParameters
        {
            // Set the issuer, audience, signing key, etc., for token validation
            // You need to configure these parameters based on your token setup
            // ...

            // Example: Validate the token and extract its claims
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = "your_issuer",
            ValidAudience = "your_audience",
            IssuerSigningKey = your_signing_key
        };

        try
        {
            // Validate the token and extract its claims
            var principal = tokenHandler.ValidateToken(token, validationParameters, out _);

            // Example: Access the user's identity and claims
            var userId = principal.FindFirstValue("sub");
            var username = principal.FindFirstValue("username");

            // Further processing with the token claims...
        }
        catch (SecurityTokenException ex)
        {
            // Token validation failed, handle the exception
            // ...
            return Unauthorized();
        }
        Console.WriteLine(token);
        Console.WriteLine("ETC");
        if (id != null)
        {
            var document = _documentsRepository.Document.Where(e => e.id.Equals(id)).Single<Document>();
            return Json(document);
        }
        else
        {
            var documents = _documentsRepository.Document.ToList();
            return Json(documents);
        }
    }
    
    
    [Authorize]
    [HttpPost]
    public IActionResult Index([FromBody] Document document)
    {
        _documentsRepository.Add(document);
        _documentsRepository.SaveChanges();
        return Ok();
    }

    [Authorize]
    [HttpPut]
    [ActionName("Index")]
    public IActionResult UpdateIndex(int? id, [FromBody] Document edit_document)
    {
        Console.WriteLine("ID UPDATE" + id);
        Document? document = _documentsRepository.Find<Document>(id);
        if (document == null)
        {
            return BadRequest();
        }

        document.author = edit_document.author;
        document.title = edit_document.title;
        document.pages = edit_document.pages;
        document.types = edit_document.types;
        document.format = edit_document.format;

        _documentsRepository.SaveChanges();
        return Ok();
    }
    
    [Authorize]
    [HttpDelete]
    [ActionName("Index")]
    public IActionResult Delete(int? id)
    {
        Console.WriteLine("IDD" + id);
        Document? document = _documentsRepository.Find<Document>(id);

        if (document == null)
        {
            return BadRequest();
        }

        _documentsRepository.Remove<Document>(document);
        _documentsRepository.SaveChanges();
        return NoContent();
    }
    
    
    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}





















