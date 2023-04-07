import {Card, CardActions, CardContent, IconButton} from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Team } from "../../models/Team";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import { makeStyles } from "@mui/styles";

const useStyles = makeStyles({
    container: {
        padding: '4em',
    },
    card: {
        display: "inline-block",
        minWidth: 100,
        maxWidth: 1000,
        overflow: "hidden",
    },

    second_card: {
        display: "inline-block",
    },

    p: {
        paddingLeft: "3%",
    }
});

export const TeamDetails = () => {
    const { teamId } = useParams();
    const [team, setTeam] = useState<Team>();
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const url = `${BACKEND_API_URL}/teams/${teamId}`
        const axiosTeam = async () => {
            setLoading(true);
            await axios.get(url)
                .then(response => {
                    const team = response.data;
                    setTeam(team);
                    setLoading(false);
                }, error => {
                    console.log(error);
                });
        };
        axiosTeam();

        //fetchTeam();
    }, [teamId]);


    const classes = useStyles();

    return (
        <Container className={classes.container}>
            <Card className={classes.card}>
                <CardContent>
                <IconButton component={Link} sx={{ mr: 3 }} to={`/teams`}>
                    <ArrowBackIcon />
                </IconButton>{" "}
                <h1>Team Details</h1>
                <p>Team created: {team?.created?.toString()}</p>
                <p>Team name: {team?.nameOfTeam}</p>
                <p>Team freePlaces: {team?.freePlaces}</p>
                <p>Team purpose: {team?.purpose}</p>
                <p>Team admin: {team?.admin}</p>
                <p>Team rating: {team?.rating}</p>
                <p>Team projects with tasks:</p>
                <ul>
                    {team?.teamTask?.map((task, index) => (
                        <CardContent key={task.id}>
                            <li>Task details</li>
                            <p className={classes.p}>Created : {task?.created?.toString()}</p>
                            <p className={classes.p}>Name of task : {task?.nameOfTask}</p>
                            <p className={classes.p}>Difficulty : {task?.difficulty}</p>
                            <li>Project details :</li>
                            <p className={classes.p}>Created : {task?.project.created?.toString()}</p>
                            <p className={classes.p}>Name of project : {task?.project.nameOfProject}</p>
                            <p className={classes.p}>Client name : {task?.project.clientName}</p>
                            <p className={classes.p}>Budget : {task?.project.budget}</p>
                            <p className={classes.p}>Description : {task?.project.description}</p>
                            <p className={classes.p}>Status : {task?.project.status}</p>
                            <hr/>
                        </CardContent>
                    ))}
                </ul>
                    <p>Team members:</p>
                    <ul>
                        {team?.teamEmployee?.map((employee, index) => (
                            <CardContent key={employee.id}>
                                <li>Employee details</li>
                                <p className={classes.p}>Created : {employee?.created?.toString()}</p>
                                <p className={classes.p}>First Name : {employee?.firstName}</p>
                                <p className={classes.p}>Last Name : {employee?.lastName}</p>
                                <p className={classes.p}>Employment Date : {employee?.employmentDate?.toString()}</p>
                                <p className={classes.p}>Phone number : {employee?.phoneNumber}</p>
                                <p className={classes.p}>Email : {employee?.email}</p>
                                <p className={classes.p}>Wage : {employee?.wage}</p>
                                <hr/>
                            </CardContent>
                        ))}
                    </ul>
                </CardContent>
                <CardActions>
                    <IconButton component={Link} sx={{ mr: 3 }} to={`/teams/${teamId}/edit`}>
                        <EditIcon />
                    </IconButton>

                    <IconButton component={Link} sx={{ mr: 3 }} to={`/teams/${teamId}/delete`}>
                        <DeleteForeverIcon sx={{ color: "red" }} />
                    </IconButton>
                </CardActions>
            </Card>
        </Container>
    );
};
