package com.example.demo.controller;


import jakarta.servlet.http.HttpSession;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/login")
public class LoginController {

    @PostMapping
    public String login(HttpSession session, @RequestBody Map<String,String> requestPayload){
        String username = requestPayload.get("username");
        session.setAttribute("username", username);
        return "Welcome!";
    }
}
