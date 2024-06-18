package com.example.springboot_hello_word.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping
    public String welcome() {
        return "Welcome !";
    }

    @GetMapping("/hello")
    public String hello() {
        return "Hello World";
    }
}
