package com.lab.forum.Model;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Setter
@Getter
@Entity
@NoArgsConstructor
@Table(name = "ROLES")
public class Role {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(name = "ROLE_NAME",length = 60)
    private String name;

    public Role(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Role{" +
                "name='" + name + '\'' +
                '}';
    }
}