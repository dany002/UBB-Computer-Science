import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { useState } from "react";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import * as React from "react";
import { AppBar, Toolbar, IconButton, Typography, Button } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppHome } from "./components/AppHome";
import { AppMenu } from "./components/AppMenu";
import {AllTeams} from "./components/teams/AllTeams";
import {TeamDetails} from "./components/teams/TeamDetail";
import {TeamDelete} from "./components/teams/TeamDelete";
import {TeamAdd} from "./components/teams/TeamAdd";
import {TeamEdit} from "./components/teams/TeamEdit";
import {TeamsByAvgWage} from "./components/teams/TeamsByAvgWage";
import {AllProjects} from "./components/projects/AllProjects";
import {ProjectDetails} from "./components/projects/ProjectDetail";
import {ProjectEdit} from "./components/projects/ProjectEdit";
import {ProjectDelete} from "./components/projects/ProjectDelete";
import {ProjectAdd} from "./components/projects/ProjectAdd";

function App() {
    return (
        <React.Fragment>
            <Router>
                <AppMenu />
                <Routes>
                    <Route path="/" element={<AppHome />} />
                    <Route path="/teams/:teamId/details" element={<TeamDetails />} />
                    <Route path="/teams/:teamId/edit" element={<TeamEdit />} />
                    <Route path="/teams/:teamId/delete" element={<TeamDelete />} />
                    <Route path="/teams/add" element={<TeamAdd />} />
                    <Route path="/teams/by-avg-wage/" element={<TeamsByAvgWage />}/>
                    <Route path="/projects" element={<AllProjects />} />
                    <Route path="/projects/:projectId/details" element={<ProjectDetails />} />
                    <Route path="/projects/:projectId/edit" element={<ProjectEdit />} />
                    <Route path="/projects/:projectId/delete" element={<ProjectDelete />} />
                    <Route path="/projects/add" element={<ProjectAdd />} />
                    <Route path="/teams/page/:page" element={<AllTeams />} />
                </Routes>
            </Router>
        </React.Fragment>
    );
}

export default App
