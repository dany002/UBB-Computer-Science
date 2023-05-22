package com.lab.forum.Controller;

import com.lab.forum.Model.*;
import com.lab.forum.Repository.IUserRepository;
import com.lab.forum.Service.CommentService;
import com.lab.forum.Service.TopicService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/topics/{topicId}/comments")
public class CommentController {

    @Autowired
    CommentService commentService;

    @Autowired
    IUserRepository userRepository;

    @Autowired
    TopicService topicService;

    @GetMapping("")
    public List<Comment> getAllComments(@PathVariable("topicId") Long topicId){
        Topic topic = this.topicService.getTopic(topicId);
        return topic.getComments();
    }

    @GetMapping("/{commentId}")
    public Comment getComment(@PathVariable("commentId") Long commentId){
        return this.commentService.getComment(commentId);
    }

    @DeleteMapping("/{commentId}")
    public void deleteComment(@PathVariable("commentId") Long commentId){
        Comment comment = this.commentService.getComment(commentId);
        Topic topic = comment.getTopic();
        topic.removeComment(comment); // Remove the comment from the topic's comments collection

        this.commentService.deleteComment(commentId);
    }

    @PostMapping("")
    public Long addComment(@RequestBody AddCommentDTO commentDTO, @PathVariable("topicId") Long topicId){
        Comment comment = new Comment();
        Topic topic = topicService.getTopic(topicId);

        comment.setTopic(topic);
        comment.setContent(commentDTO.getContent());

        Optional<User> userOptional = userRepository.findByUsername(commentDTO.getCreated_by());
        User user = userOptional.orElseThrow(() -> new RuntimeException("User not found"));

        comment.setUser(user);
        commentService.saveOrUpdate(comment);
        return comment.getCommentId();
    }

    @PutMapping("/{commentId}")
    public Comment updateComment(@RequestBody UpdateCommentDTO comment, @PathVariable("topicId") Long topicId, @PathVariable("commentId") Long commentId){
        Comment new_comment = new Comment();
        new_comment.setContent(comment.getContent());

        Optional<User> userOptional = userRepository.findByUsername(comment.getCreated_by());
        User user = userOptional.orElseThrow(() -> new RuntimeException("User not found"));

        new_comment.setUser(user);

        Topic topic = topicService.getTopic(topicId);

        new_comment.setTopic(topic);
        new_comment.setCommentId(commentId);

        this.commentService.saveOrUpdate(new_comment);
        return new_comment;
    }
}
