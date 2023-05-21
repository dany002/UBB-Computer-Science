package com.lab.forum.Repository;

import com.lab.forum.Model.Comment;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ICommentRepository extends JpaRepository<Comment, Long> {
}
