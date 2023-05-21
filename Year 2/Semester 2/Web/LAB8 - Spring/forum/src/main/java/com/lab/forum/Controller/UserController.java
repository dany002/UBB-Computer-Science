package com.lab.forum.Controller;


import com.lab.forum.Model.User;
import com.lab.forum.Service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/users")
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class UserController {
    @Autowired
    UserService userService;

    @GetMapping("")
    public List<User> getAllUsers(){
        System.out.println("ALOHA");
        return this.userService.getAllUsers();
    }

    @GetMapping("/{userId}")
    public User getUser(@PathVariable("userId") Long userId){
        return this.userService.getUser(userId);
    }

    @DeleteMapping("/{userId}")
    public void deleteUser(@PathVariable("userId") Long userId){
        this.userService.deleteUser(userId);
    }

    @PostMapping("")
    public Long addUser(@RequestBody User user){
        this.userService.saveOrUpdate(user);
        return user.getUserId();
    }

    @PutMapping("")
    public User updateUser(@RequestBody User user){
        this.userService.saveOrUpdate(user);
        return user;
    }
}
