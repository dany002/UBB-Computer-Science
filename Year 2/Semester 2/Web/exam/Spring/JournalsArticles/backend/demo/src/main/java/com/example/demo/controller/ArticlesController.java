package com.example.demo.controller;


import com.example.demo.model.Articles;
import com.example.demo.model.Journals;
import com.example.demo.repository.ArticlesRepository;
import com.example.demo.repository.JournalsRepository;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Date;
import java.util.Map;

@RestController
@RequestMapping("/articles")
public class ArticlesController {

    @Autowired
    private ArticlesRepository articlesRepository;

    @Autowired
    private JournalsRepository journalsRepository;

    @PostMapping(path = "/add")
    public String addNewArticle(HttpSession session, @RequestBody Map<String,String> requestPayload){
        String journalName = requestPayload.get("journalname");
        String summary = requestPayload.get("summary");
        Journals journal = journalsRepository.findByName(journalName);
        Long id;
        if(journal == null){
            Journals new_journal = new Journals();
            new_journal.setName(journalName);
            journalsRepository.save(new_journal);
            id = new_journal.getJournalid();
            journal = new_journal;
        }
        System.out.println(journal.toString());
        Articles articles = new Articles();
        articles.setJournals(journal);
        articles.setSummary(summary);
        articles.setUser((String) session.getAttribute("username"));
        articles.setDate(new Date());
        System.out.println(articles.toString());
        articlesRepository.save(articles);
        return "Saved";
    }

    @GetMapping("/all")
    public Iterable<Articles> getArticles(HttpSession session, @RequestParam("journalName") String journalName) {
        Journals journals = journalsRepository.findByName(journalName);
        if (journals == null) {
            return null;
        }
        System.out.println(journals.toString());
        System.out.println(session.getAttribute("username"));
        return articlesRepository.findByUserAndJournals((String) session.getAttribute("username"), journals);
    }



}
