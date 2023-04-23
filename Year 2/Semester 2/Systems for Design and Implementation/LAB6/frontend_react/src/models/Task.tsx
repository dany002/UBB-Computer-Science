import {Team} from "./Team";
import {Project} from "./Project";

export interface Task{
    id?: number;
    created: Date;
    nameOfTask: string;
    difficulty: number;
    team: Team;
    project: Project;
}