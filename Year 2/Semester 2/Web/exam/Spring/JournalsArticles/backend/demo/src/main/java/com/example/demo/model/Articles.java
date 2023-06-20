package com.example.demo.model;


import jakarta.persistence.*;

import java.util.Date;

@Entity
public class Articles {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long articleid;

    private String user;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "journalid")
    private Journals journals;

    private String summary;

    private Date date;


    public Long getArticleid() {
        return articleid;
    }

    public void setArticleid(Long articleid) {
        this.articleid = articleid;
    }

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public Journals getJournals() {
        return journals;
    }

    public void setJournals(Journals journals) {
        this.journals = journals;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    @Override
    public String toString() {
        return "Articles{" +
                "articleid=" + articleid +
                ", user='" + user + '\'' +
                ", journals=" + journals +
                ", summary='" + summary + '\'' +
                ", date=" + date +
                '}';
    }
}
