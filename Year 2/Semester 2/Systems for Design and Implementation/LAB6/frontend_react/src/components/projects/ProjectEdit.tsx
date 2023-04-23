import {Link, useNavigate, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import {Project} from "../../models/Project";
import axios from "axios";
import {BACKEND_API_URL} from "../../constants";
import {Container} from "@mui/system";
import {Button, Card, CardActions, CardContent, IconButton, TextField} from "@mui/material";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import {makeStyles} from "@mui/styles";


const useStyles = makeStyles({
    container: {
        padding: '4em',
    },
    card: {
        display: "inline-block",
        minWidth: 100,
        maxWidth: 500,
        overflow: "hidden",
    },

    second_card: {
        display: "inline-block",
    },

    p: {
        paddingLeft: "3%",
    }
});


export const ProjectEdit = () => {

    const navigate = useNavigate();

    const { projectId } = useParams();
    const [project, setProject] = useState<Project>({
        nameOfProject: "",
        clientName: "",
        budget: 0,
        description: "",
        status: ""
    });

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

    const updateProject = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        try {
            setProject(project);
            const response = await axios.put(`${BACKEND_API_URL}/projects/${projectId}/`, project);
            navigate("/projects");
        } catch (error) {
            console.log(error);
        }
    };



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
                </CardContent>
            </Card>
            <Card className={classes.card}>
                <CardContent>
                    <form onSubmit={updateProject}>
                        <TextField
                            id="nameOfProject"
                            label="Name"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setProject({ ...project, nameOfProject: event.target.value })}
                        />
                        <TextField
                            id="clientName"
                            label="clientName"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setProject({ ...project, clientName: event.target.value })}
                        />
                        <TextField
                            id="budget"
                            label="budget"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setProject({ ...project, budget: parseInt(event.target.value)})}
                        />
                        <TextField
                            id="description"
                            label="description"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setProject({ ...project, description: event.target.value })}
                        />
                        <TextField
                            id="status"
                            label="status"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setProject({ ...project, status: event.target.value })}
                        />

                        <Button type="submit">Update Project</Button>
                    </form>
                </CardContent>
            </Card>
        </Container>
    );
};
