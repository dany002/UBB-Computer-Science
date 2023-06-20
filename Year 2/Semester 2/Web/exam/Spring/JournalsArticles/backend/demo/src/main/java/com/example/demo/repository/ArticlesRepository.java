package com.example.demo.repository;

import com.example.demo.model.Articles;
import com.example.demo.model.Journals;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface ArticlesRepository extends CrudRepository<Articles, Long> {
    Iterable<Articles> findByUserAndJournals(String user, Journals journals);
}
