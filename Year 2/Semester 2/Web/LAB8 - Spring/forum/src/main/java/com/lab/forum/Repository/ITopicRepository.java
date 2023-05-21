package com.lab.forum.Repository;

import com.lab.forum.Model.Topic;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ITopicRepository extends JpaRepository<Topic,Long> {
}
