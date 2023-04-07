import {
    TableContainer,
    Paper,
    Table,
    TableHead,
    TableRow,
    TableCell,
    TableBody,
    CircularProgress,
    Container,
    IconButton,
    Tooltip, Button
} from "@mui/material";


import React, {useEffect, useState} from "react";
import {Team} from "../../models/Team";
import {BACKEND_API_URL} from "../../constants";
import axios from "axios";

interface TeamWithAvgWage extends Team {
    avg_wage: number;
}
export const TeamsByAvgWage = () => {
    const [loading, setLoading] = useState(false);
    const [data, setData] = useState<TeamWithAvgWage[]>([]);


    useEffect(() => {
        const url = `${BACKEND_API_URL}/teams/by-avg-wage/`;
        const axiosTeam = async () => {
            setLoading(true);
            await axios.get<TeamWithAvgWage[]>(url)
                .then(response => {
                    setData(response.data)
                    setLoading(false);
                }, error => {
                    console.log(error);
                });
        };
        axiosTeam();
    }, []);


    return (
        <Container sx={{maxWidth:"xl", padding: '4em'}}>

            <h1>Teams by average wage of employees</h1>

            {loading && <CircularProgress />}
            {!loading && data.length === 0 && <p>No teams found</p>}
            {!loading && data.length > 0 && (
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 650 }}  aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>#</TableCell>
                                <TableCell align="center">Name</TableCell>
                                <TableCell align="center">Created</TableCell>
                                <TableCell align="center">Free places</TableCell>
                                <TableCell align="center">Purpose</TableCell>
                                <TableCell align="center">Admin</TableCell>
                                <TableCell align="center">Rating</TableCell>
                                <TableCell align="center">Average wage</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {data.map((team, index) => (
                                <TableRow key={index}>
                                    <TableCell component="th" scope="row">
                                        {index + 1}
                                    </TableCell>
                                    <TableCell align="center">{team.nameOfTeam}</TableCell>
                                    <TableCell align="center">{team?.created?.toString()}</TableCell>
                                    <TableCell align="center">{team.freePlaces}</TableCell>
                                    <TableCell align="center">{team.purpose}</TableCell>
                                    <TableCell align="center">{team.admin}</TableCell>
                                    <TableCell align="center">{team.rating}</TableCell>
                                    <TableCell align="center">{team?.avg_wage}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            )}
        </Container>
    );
};