import {Link, useNavigate, useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import {Team} from "../../models/Team";
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


export const TeamEdit = () => {

    const navigate = useNavigate();

    const { teamId } = useParams();
    const [team, setTeam] = useState<Team>({
        nameOfTeam: "",
        freePlaces: 0,
        purpose: "",
        admin: "",
        rating: 0
    });

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

    const updateTeam = async (event: { preventDefault: () => void }) => {
        event.preventDefault();
        try {
            setTeam(team);
            const response = await axios.put(`${BACKEND_API_URL}/teams/${teamId}/`, team);
            navigate("/teams");
        } catch (error) {
            console.log(error);
        }
    };



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
                </CardContent>
            </Card>
            <Card className={classes.card}>
                <CardContent>
                    <p>{team?.id}</p>
                    <form onSubmit={updateTeam}>
                        <TextField
                            id="nameOfTeam"
                            label="name"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setTeam({ ...team, nameOfTeam: event.target.value })}
                        />
                        <TextField
                            id="freePlaces"
                            label="freePlaces"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setTeam({ ...team, freePlaces: parseInt(event.target.value) })}
                        />

                        <TextField
                            id="purpose"
                            label="purpose"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setTeam({ ...team, purpose: event.target.value })}
                        />

                        <TextField
                            id="admin"
                            label="admin"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setTeam({ ...team, admin: event.target.value })}
                        />

                        <TextField
                            id="rating"
                            label="rating"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            onChange={(event) => setTeam({ ...team, rating: parseInt(event.target.value) })}
                        />
                        <Button type="submit">Update team</Button>
                    </form>
                </CardContent>
            </Card>
        </Container>
    );
};
