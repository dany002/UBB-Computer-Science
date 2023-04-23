import {Team} from "./Team";
import {Task} from "./Task";

export interface Project{
    id?: number;
    created?: Date;
    nameOfProject: string;
    clientName: string;
    budget: number;
    description: string;
    status: string;
    projectTask?: Task[];
}