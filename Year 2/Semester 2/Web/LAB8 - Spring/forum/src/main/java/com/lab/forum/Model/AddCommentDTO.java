package com.lab.forum.Model;

public class AddCommentDTO {
    String content;

    String created_by;

    Long topicId;

    public AddCommentDTO(String content, String created_by, Long topicId) {
        this.content = content;
        this.created_by = created_by;
        this.topicId = topicId;
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

    public Long getTopicId() {
        return topicId;
    }

    public void setTopicId(Long topicId) {
        this.topicId = topicId;
    }
}
