package com.lab.forum.Model;


import jakarta.persistence.*;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.ArrayList;
import java.util.List;

@Entity
@NoArgsConstructor
@Table(name = "TOPIC")
public class Topic {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long topicId;

    @Column(name="TOPIC_NAME", nullable = false)
    private String name;

    @OneToMany(mappedBy = "topic", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Comment> comments = new ArrayList<>();

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @Autowired
    public Topic(Long topicId, String name, User user) {
        this.topicId = topicId;
        this.name = name;
        this.user = user;
    }

    public Long getTopicId() {
        return topicId;
    }

    public void setTopicId(Long topicId) {
        this.topicId = topicId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public List<Comment> getComments() {
        return comments;
    }

    public void setComments(List<Comment> comments) {
        this.comments = comments;
    }

    public void addComment(Comment comment) {
        comments.add(comment);
        comment.setTopic(this);
    }

    public void removeComment(Comment comment) {
        comments.remove(comment);
        comment.setTopic(null);
    }

    @Override
    public String toString() {
        return "Topic{" +
                "topicId=" + topicId +
                ", name='" + name + '\'' +
                ", user=" + user +
                '}';
    }
}
