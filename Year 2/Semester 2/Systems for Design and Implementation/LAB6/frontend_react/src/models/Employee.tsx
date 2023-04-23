import {Team} from "./Team";

export interface Employee{
    id?: number;
    created?: Date;
    firstName: string;
    lastName: string;
    employmentDate: Date;
    phoneNumber: string;
    email: string;
    wage: number;
    team: Team;
}