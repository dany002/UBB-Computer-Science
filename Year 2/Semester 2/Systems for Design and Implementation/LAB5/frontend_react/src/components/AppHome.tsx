import { CssBaseline, Container, Typography } from "@mui/material";
import React from "react";

export const AppHome = () => {
    return (
        <React.Fragment>
            <CssBaseline />

            <Container maxWidth="xl">
                <Typography variant="h3" component="h3" gutterBottom>
                    Welcome to the app! Use the menu above to navigate.
                </Typography>
            </Container>
        </React.Fragment>
    );
};