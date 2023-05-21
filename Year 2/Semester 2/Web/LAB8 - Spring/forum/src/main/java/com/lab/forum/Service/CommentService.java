package com.lab.forum.Service;

import com.lab.forum.Model.Comment;
import com.lab.forum.Model.Topic;
import com.lab.forum.Repository.ICommentRepository;
import com.lab.forum.Repository.ITopicRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;


@Service
public class CommentService {

    @Autowired
    ICommentRepository commentRepository;

    public List<Comment> getAllComments(){
        return new ArrayList<>(commentRepository.findAll());
    }

    public Comment getComment(Long id) {
        return commentRepository.findById(id).get();
    }

    public void saveOrUpdate(Comment comment) {
        commentRepository.save(comment);
    }

    public void deleteComment(Long id) {
        commentRepository.deleteById(id);
    }
}
