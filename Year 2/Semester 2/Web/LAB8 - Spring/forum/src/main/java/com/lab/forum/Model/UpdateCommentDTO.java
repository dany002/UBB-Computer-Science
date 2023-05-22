package com.lab.forum.Model;

public class UpdateCommentDTO {
    String content;

    String created_by;

    public UpdateCommentDTO(String content, String created_by) {
        this.content = content;
        this.created_by = created_by;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getCreated_by() {
        return created_by;
    }

    public void setCreated_by(String created_by) {
        this.created_by = created_by;
    }

}
