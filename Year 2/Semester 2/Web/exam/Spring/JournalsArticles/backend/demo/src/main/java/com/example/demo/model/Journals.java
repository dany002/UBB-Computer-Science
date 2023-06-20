package com.example.demo.model;


import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Journals {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long journalid;

    private String name;


    public Long getJournalid() {
        return journalid;
    }

    public void setJournalid(Long journalid) {
        this.journalid = journalid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Journals{" +
                "journalid=" + journalid +
                ", name='" + name + '\'' +
                '}';
    }
}
