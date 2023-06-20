package com.example.demo.repository;

import com.example.demo.model.Journals;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface JournalsRepository extends CrudRepository<Journals, Long> {
    Journals findByName(String name);
}
