import { Button, Card, CardActions, CardContent, IconButton, TextField } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import {Project} from "../../models/Project";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";

export const ProjectAdd = () => {
    const navigate = useNavigate();

    const [project, setProject] = useState<Project>({
        nameOfProject: "",
        clientName: "",
        budget: 0,
        description: "",
        status: ""
    });

    const addProject = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        try {
            await axios.post(`${BACKEND_API_URL}/projects/`, project);
            navigate("/projects");
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <Container>
            <Card>
                <CardContent>
                    <IconButton component={Link} sx={{ mr: 3 }} to={`/projects`}>
                        <ArrowBackIcon />
                    </IconButton>{" "}
                    <form onSubmit={addProject}>
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

                        <Button type="submit">Add Project</Button>
                    </form>
                </CardContent>
                <CardActions></CardActions>
            </Card>
        </Container>
    );
};
