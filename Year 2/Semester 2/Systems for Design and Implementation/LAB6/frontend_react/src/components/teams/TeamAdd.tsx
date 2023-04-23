import { Button, Card, CardActions, CardContent, IconButton, TextField } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Team } from "../../models/Team";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";

export const TeamAdd = () => {
    const navigate = useNavigate();

    const [team, setTeam] = useState<Team>({
        nameOfTeam: "",
        freePlaces: 0,
        purpose: "",
        admin: "",
        rating: 0
    });

    const addTeam = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        try {
            await axios.post(`${BACKEND_API_URL}/teams/`, team);
            navigate("/teams");
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <Container>
            <Card>
                <CardContent>
                    <IconButton component={Link} sx={{ mr: 3 }} to={`/teams`}>
                        <ArrowBackIcon />
                    </IconButton>{" "}
                    <form onSubmit={addTeam}>
                        <TextField
                            id="nameOfTeam"
                            label="Name"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setTeam({ ...team, nameOfTeam: event.target.value })}
                        />
                        <TextField
                            id="purpose"
                            label="Purpose"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setTeam({ ...team, purpose: event.target.value })}
                        />
                        <TextField
                            id="freePlaces"
                            label="Free places"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setTeam({ ...team, freePlaces: parseInt(event.target.value)})}
                        />
                        <TextField
                            id="admin"
                            label="Admin"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setTeam({ ...team, admin: event.target.value })}
                        />
                        <TextField
                            id="rating"
                            label="Rating"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setTeam({ ...team, rating: parseInt(event.target.value)})}
                        />
                        <Button type="submit">Add Team</Button>
                    </form>
                </CardContent>
                <CardActions></CardActions>
            </Card>
        </Container>
    );
};
