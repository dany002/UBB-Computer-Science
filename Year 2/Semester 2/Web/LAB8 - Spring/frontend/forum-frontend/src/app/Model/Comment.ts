import {UserWithNameDTO} from "./User";

export interface Comment{
  content: string;
  created_by: UserWithNameDTO;
}
