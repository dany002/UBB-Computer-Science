package com.lab.forum.Controller;

import com.lab.forum.Model.AddTopicDTO;
import com.lab.forum.Model.Topic;
import com.lab.forum.Model.User;
import com.lab.forum.Repository.IUserRepository;
import com.lab.forum.Service.TopicService;
import com.lab.forum.Service.UserService;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/topics")
public class TopicController {

    @Autowired
    TopicService topicService;

    @Autowired
    IUserRepository userRepository;

    @Autowired
    private HttpServletRequest request;


    @GetMapping("")
    public List<Topic> getAllTopics() {
        return this.topicService.getAllTopics();
    }


    @GetMapping("/{topicId}")
    public Topic getTopic(@PathVariable("topicId") Long topicId){
        return this.topicService.getTopic(topicId);
    }

    @DeleteMapping("/{topicId}")
    public void deleteTopic(@PathVariable("topicId") Long topicId){
        this.topicService.deleteTopic(topicId);
    }

    @PostMapping("")
    public Long addTopic(@RequestBody AddTopicDTO topicDTO){
//        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
//        System.out.println("1");
//        String username = authentication.getName();
//        System.out.println("2");
//        System.out.println("USERNAME" + username + '\n');
//        System.out.println("SECOND USERNAME" + request.getSession().getAttribute("username"));
//        // Fetch the user information using the username (e.g., from your UserRepository)
//        String usernamee = request.getUserPrincipal().getName();
//        System.out.println("THIRD USERNAME " + usernamee);
//
//        User user = userRepository.findByUsername(username)
//                .orElseThrow(() -> new RuntimeException("User not found"));
//        System.out.println("3");
//        topic.setUser(user);
        Topic topic = new Topic();
        topic.setName(topicDTO.getName());
        Optional<User> userOptional = userRepository.findByUsername(topicDTO.getCreated_by());
        User user = userOptional.orElseThrow(() -> new RuntimeException("User not found"));
        topic.setUser(user);
        topicService.saveOrUpdate(topic);
        return topic.getTopicId();
    }

    @PutMapping("")
    public Topic updateTopic(@RequestBody Topic topic){
        this.topicService.saveOrUpdate(topic);
        return topic;
    }
}
