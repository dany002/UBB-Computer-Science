import {UserWithNameDTO} from "./User";
import {Topic} from "./Topic";

export interface Comment{
  content: string;
  created_by: UserWithNameDTO;
}

export interface CommentUpdateDTO{
  content: string;
  created_by: string;
}
