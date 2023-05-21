package com.lab.forum.Controller;

import com.lab.forum.Model.AddCommentDTO;
import com.lab.forum.Model.Comment;
import com.lab.forum.Model.Topic;
import com.lab.forum.Model.User;
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
        System.out.println(topic);
        System.out.println("COMMENTS" + topic.getComments());
        return topic.getComments();
    }

    @GetMapping("/{commentId}")
    public Comment getComment(@PathVariable("commentId") Long commentId){
        return this.commentService.getComment(commentId);
    }

    @DeleteMapping("/{commentId}")
    public void deleteComment(@PathVariable("commentId") Long commentId){
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

    @PutMapping("")
    public Comment updateComment(@RequestBody Comment comment){
        this.commentService.saveOrUpdate(comment);
        return comment;
    }
}
