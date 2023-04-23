import {Card, CardActions, CardContent, IconButton} from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Project } from "../../models/Project";
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

export const ProjectDetails = () => {
    const { projectId } = useParams();
    const [project, setProject] = useState<Project>();
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const url = `${BACKEND_API_URL}/projects/${projectId}`
        const axiosProject = async () => {
            setLoading(true);
            await axios.get(url)
                .then(response => {
                    const project = response.data;
                    setProject(project);
                    setLoading(false);
                }, error => {
                    console.log(error);
                });
        };
        axiosProject();

    }, [projectId]);


    const classes = useStyles();

    return (
        <Container className={classes.container}>
            <Card className={classes.card}>
                <CardContent>
                    <IconButton component={Link} sx={{ mr: 3 }} to={`/projects`}>
                        <ArrowBackIcon />
                    </IconButton>{" "}
                    <h1>Project Details</h1>
                    <p>Project created: {project?.created?.toString()}</p>
                    <p>Project name: {project?.nameOfProject}</p>
                    <p>Project client name: {project?.clientName}</p>
                    <p>Project budget: {project?.budget}</p>
                    <p>Project description: {project?.description}</p>
                    <p>Project status: {project?.status}</p>
                    <p>Team projects with tasks:</p>
                    <ul>
                        {project?.projectTask?.map((task, index) => (
                            <CardContent key={task.id}>
                                <li>Task details</li>
                                <p className={classes.p}>Created : {task?.created?.toString()}</p>
                                <p className={classes.p}>Name of task : {task?.nameOfTask}</p>
                                <p className={classes.p}>Difficulty : {task?.difficulty}</p>
                                <li>Team details :</li>
                                <p className={classes.p}>Created : {task?.team.created?.toString()}</p>
                                <p className={classes.p}>Name of team : {task?.team.nameOfTeam}</p>
                                <p className={classes.p}>Free places : {task?.team.freePlaces}</p>
                                <p className={classes.p}>Purpose : {task?.team.purpose}</p>
                                <p className={classes.p}>Admin : {task?.team.admin}</p>
                                <p className={classes.p}>Rating : {task?.team.rating}</p>
                                <hr/>
                            </CardContent>
                        ))}
                    </ul>
                </CardContent>
                <CardActions>
                    <IconButton component={Link} sx={{ mr: 3 }} to={`/projects/${projectId}/edit`}>
                        <EditIcon />
                    </IconButton>

                    <IconButton component={Link} sx={{ mr: 3 }} to={`/projects/${projectId}/delete`}>
                        <DeleteForeverIcon sx={{ color: "red" }} />
                    </IconButton>
                </CardActions>
            </Card>
        </Container>
    );
};
