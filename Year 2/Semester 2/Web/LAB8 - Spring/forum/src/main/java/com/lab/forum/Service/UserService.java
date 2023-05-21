package com.lab.forum.Service;


import com.lab.forum.Model.User;
import com.lab.forum.Repository.IUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class UserService {

    @Autowired
    IUserRepository userRepository;

    public List<User> getAllUsers(){
        return new ArrayList<>(userRepository.findAll());
    }

    public User getUser(Long id){
        return userRepository.findById(id).get();
    }

    public void saveOrUpdate(User user){
        this.userRepository.save(user);
    }

    public void deleteUser(Long id){
        this.userRepository.deleteById(id);
    }

    public void update(User user, Long id){
        this.userRepository.save(user);
    }
}

