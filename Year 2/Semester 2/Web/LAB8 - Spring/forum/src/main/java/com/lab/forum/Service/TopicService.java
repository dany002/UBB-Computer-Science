package com.lab.forum.Service;


import com.lab.forum.Model.Topic;
import com.lab.forum.Repository.ITopicRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class TopicService {

    @Autowired
    ITopicRepository topicRepository;

    public List<Topic> getAllTopics(){
        return new ArrayList<>(topicRepository.findAll());
    }

    public Topic getTopic(Long id){
        return topicRepository.findById(id).get();
    }

    public void saveOrUpdate(Topic topic){
        topicRepository.save(topic);
    }

    public void deleteTopic(Long id){
        topicRepository.deleteById(id);
    }

}
