using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
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

    [HttpPost]
    public IActionResult Index([FromBody] Document document)
    {
        _documentsRepository.Add(document);
        _documentsRepository.SaveChanges();
        return Ok();
    }

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





















