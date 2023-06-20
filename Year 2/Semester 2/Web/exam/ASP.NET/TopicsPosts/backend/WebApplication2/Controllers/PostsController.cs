using System.Diagnostics;
using System.Reflection.Metadata;
using Microsoft.AspNetCore.Mvc;
using WebApplication2.Models;
using WebApplication2.Repository;

namespace WebApplication2.Controllers;

public class PostsController : Controller
{
    private readonly ILogger<HomeController> _logger;
    private readonly PostsRepository _postsRepository;

    public PostsController(ILogger<HomeController> logger, PostsRepository postsRepository)
    {
        _logger = logger;
        _postsRepository = postsRepository;
    }

    [HttpGet]
    public IActionResult Index(int? id)
    {
        if (id != null)
        {
            var posts = _postsRepository.Posts.Where(e => e.id.Equals(id)).Single<Posts>();
            return Json(posts);
        }
        else
        {
            var posts = _postsRepository.Posts.ToList();
            return Json(posts);
        }
    }

    [HttpPost]
    public IActionResult Index([FromBody] Posts post)
    {
        _postsRepository.Add(post);
        _postsRepository.SaveChanges();
        return Ok();
    }

    [HttpPut]
    [ActionName("Index")]
    public IActionResult UpdateIndex(int? id, [FromBody] Posts edit_post)
    {
        Console.WriteLine("ID UPDATE" + id);
        Posts? post = _postsRepository.Find<Posts>(id);
        if (post == null)
        {
            return BadRequest();
        }

        //Topics? topic = _topicsRepository.Find<Topics>(edit_post.topicid); // we ll modify it later

        post.user = edit_post.user;
        post.topicid = edit_post.topicid;
        post.text = edit_post.text;
        post.date = edit_post.date;

        _postsRepository.SaveChanges();
        return Ok();
    }
    
    
    
    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}