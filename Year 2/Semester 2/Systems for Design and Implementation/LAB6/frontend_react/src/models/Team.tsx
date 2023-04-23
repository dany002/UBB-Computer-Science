import {Project} from "./Project";
import {Task} from "./Task";
import {Employee} from "./Employee";

export interface Team{
    id?: number;
    created?: Date;
    nameOfTeam: string;
    freePlaces: number;
    purpose: string;
    admin: string;
    rating: number;
    teamTask?: Task[];
    //task?: Task;
    teamEmployee?: Employee[];
}