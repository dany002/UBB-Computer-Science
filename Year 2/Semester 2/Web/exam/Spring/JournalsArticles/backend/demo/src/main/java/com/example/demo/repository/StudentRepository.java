package com.example.demo.repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import com.example.demo.model.Student;

// This will be AUTO IMPLEMENTED by Spring into a Bean called StudentRepository
@Repository
public interface StudentRepository extends CrudRepository<Student, Integer> {

}

