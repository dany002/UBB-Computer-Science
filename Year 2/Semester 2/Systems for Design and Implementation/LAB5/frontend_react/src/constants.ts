//const DEV_BACKEND_API_URL = "http://ec2-18-192-105-217.eu-central-1.compute.amazonaws.com/api";
const PROD_BACKEND_API_URL = "/api";
const DEV_BACKEND_API_URL = "http://127.0.0.1:8000/api";

export const BACKEND_API_URL =

    process.env.NODE_ENV === "development" ? DEV_BACKEND_API_URL : PROD_BACKEND_API_URL;