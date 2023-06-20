package com.example.demo.controller;


import com.example.demo.model.Journals;
import com.example.demo.repository.JournalsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/journals")
public class JournalsController {

    @Autowired
    private JournalsRepository journalsRepository;

    @PostMapping(path = "/add")
    public String addNewJournal(@RequestParam String name){
        Journals journals = new Journals();
        journals.setName(name);
        journalsRepository.save(journals);
        return "Saved";
    }

    @PutMapping(path = "/update")
    public String updateJournal(@RequestBody Journals journals){
        journalsRepository.save(journals);
        return "Updated";
    }

    @DeleteMapping(path = "/delete")
    public String deleteJournal(@RequestParam Long id){
        journalsRepository.deleteById(id);
        return "Deleted";
    }

    @GetMapping(path = "/all")
    public Iterable<Journals> getAllJournals(){
        return journalsRepository.findAll();
    }
}
