import {User, UserWithNameDTO} from "./User";
import {Comment} from "./Comment";

export interface Topic{
  id: string;
  name: string;
  user: UserWithNameDTO;
}

export interface AddTopicDTO{
  name: string;
  created_by: string;
}

export interface TopicWithCommentsDTO{
  name: string;
  created_by: string;
  comments: Comment[];
}
