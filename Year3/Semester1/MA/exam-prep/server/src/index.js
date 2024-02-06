var koa = require('koa');
var app = module.exports = new koa();
const server = require('http').createServer(app.callback());
const WebSocket = require('ws');
const wss = new WebSocket.Server({ server });
const Router = require('koa-router');
const cors = require('@koa/cors');
const bodyParser = require('koa-bodyparser');

app.use(bodyParser());

app.use(cors());

app.use(middleware);

function middleware(ctx, next) {
    const start = new Date();
    return next().then(() => {
        const ms = new Date() - start;
        console.log(`${start.toLocaleTimeString()} ${ctx.response.status} ${ctx.request.method} ${ctx.request.url} - ${ms}ms`);
    });
}

const cars = [
    { id: 1, name: "Toyota Camry", supplier: "Toyota Motors", details: "Sedan with advanced safety features", status: "available", quantity: 10, type: "sedan" },
    { id: 2, name: "Honda CR-V", supplier: "Honda Motor Co.", details: "Compact SUV with spacious interior", status: "pending", quantity: 5, type: "SUV" },
    { id: 3, name: "Ford F-150", supplier: "Ford Motor Company", details: "Full-size pickup truck for versatile use", status: "available", quantity: 8, type: "truck" },
    { id: 4, name: "Chevrolet Malibu", supplier: "Chevrolet Motors", details: "Midsize sedan with fuel efficiency", status: "sold", quantity: 0, type: "sedan" },
    { id: 5, name: "Jeep Wrangler", supplier: "Fiat Chrysler Automobiles", details: "Off-road SUV for adventure seekers", status: "available", quantity: 3, type: "SUV" },
    { id: 6, name: "Nissan Titan", supplier: "Nissan Motors", details: "Full-size pickup truck with towing capabilities", status: "available", quantity: 12, type: "truck" },
    { id: 7, name: "BMW 3 Series", supplier: "BMW AG", details: "Luxury sedan with cutting-edge technology", status: "pending", quantity: 2, type: "sedan" },
    { id: 8, name: "Mercedes-Benz GLE", supplier: "Daimler AG", details: "Premium SUV with advanced safety and comfort features", status: "available", quantity: 6, type: "SUV" },
    { id: 9, name: "Ram 1500", supplier: "Stellantis", details: "Light-duty pickup truck with stylish design", status: "available", quantity: 15, type: "truck" },
    { id: 10, name: "Audi A6", supplier: "Audi AG", details: "Executive sedan with a blend of performance and luxury", status: "pending", quantity: 1, type: "sedan" },
    { id: 11, name: "Mazda CX-5", supplier: "Mazda Motor Corporation", details: "Compact SUV with sleek design", status: "available", quantity: 7, type: "SUV" },
    { id: 12, name: "Chevrolet Silverado", supplier: "Chevrolet Motors", details: "Heavy-duty pickup truck for tough jobs", status: "pending", quantity: 0, type: "truck" },
    { id: 13, name: "Lexus ES", supplier: "Toyota Motors", details: "Luxury sedan with refined interiors", status: "available", quantity: 4, type: "sedan" },
    { id: 14, name: "Subaru Outback", supplier: "Subaru Corporation", details: "Midsize SUV with all-wheel-drive capability", status: "available", quantity: 9, type: "SUV" },
    { id: 15, name: "Ford Ranger", supplier: "Ford Motor Company", details: "Compact pickup truck with off-road capabilities", status: "pending", quantity: 0, type: "truck" },
];


const router = new Router();

router.get('/cars', ctx => {
    ctx.response.body = cars;
    ctx.response.status = 200;
});

router.get('/carstypes', ctx => {
    ctx.response.body = cars.filter(entry => entry.status != "sold");
    ctx.response.status = 200;
});

router.get('/carorders', ctx => {
    ctx.response.body = cars.filter(entry => entry.status == "pending");
    ctx.response.status = 200;
});

router.get('/car/:id', ctx => {
    // console.log("ctx: " + JSON.stringify(ctx));
    const headers = ctx.params;
    // console.log("body: " + JSON.stringify(headers));
    const id = headers.id;
    if (typeof id !== 'undefined') {
        const index = cars.findIndex(entry => entry.id == id);
        if (index === -1) {
            const msg = "No entity with id: " + id;
            console.log(msg);
            ctx.response.body = { text: msg };
            ctx.response.status = 404;
        } else {
            let entry = cars[index];
            ctx.response.body = entry;
            ctx.response.status = 200;
        }
    } else {
        ctx.response.body = { text: 'Id missing or invalid' };
        ctx.response.status = 404;
    }
});

const broadcast = (data) =>
    wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(data));
        }
    });

router.post('/car', ctx => {
    // console.log("ctx: " + JSON.stringify(ctx));
    const headers = ctx.request.body;
    // console.log("body: " + JSON.stringify(headers));
    const name = headers.name;
    const supplier = headers.supplier;
    const details = headers.details;
    const status = headers.status;
    const quantity = headers.quantity;
    const type = headers.type;
    if (typeof name !== 'undefined'
        && typeof supplier !== 'undefined'
        && typeof details !== 'undefined'
        && typeof status !== 'undefined'
        && typeof quantity !== 'undefined'
        && typeof type !== 'undefined') {
        const index = cars.findIndex(entry => entry.name == name && entry.supplier == supplier);
        if (index !== -1) {
            const msg = "The entity already exists!";
            console.log(msg);
            ctx.response.body = { text: msg };
            ctx.response.status = 404;
        } else {
            let maxId = Math.max.apply(Math, cars.map(entry => entry.id)) + 1;
            let entry = {
                id: maxId,
                name,
                supplier,
                details,
                status,
                quantity,
                type
            };
            cars.push(entry);
            broadcast(entry);
            ctx.response.body = entry;
            ctx.response.status = 200;
        }
    } else {
        const msg = "Missing or invalid name: " + name + " supplier: " + supplier + " details: " + details
            + " status: " + status + " quantity: " + quantity + " type: " + type;
        console.log(msg);
        ctx.response.body = { text: msg };
        ctx.response.status = 404;
    }
});

router.put('/requestcar/:type', ctx => {
    const headers = ctx.params;
    const type = headers.type;
    if (typeof type !== 'undefined') {
        const index = cars.findIndex(entry => entry.type == type);
        if (index === -1) {
            //create new entry
            const msg = "No entity with type: " + type;
            console.log(msg);
            ctx.response.body = { text: msg };
            ctx.response.status = 404;
        } else {
            let entry = cars[index];
            entry.quantity++;
            ctx.response.body = entry;
            ctx.response.status = 200;
        }
    } else {
        const msg = "Type missing or invalid. type: " + type;
        console.log(msg);
        ctx.response.body = { text: msg };
        ctx.response.status = 404;
    }
});

app.use(router.routes());
app.use(router.allowedMethods());

const port = 2406;

server.listen(port, () => {
    console.log(`🚀 Server listening on ${port} ... 🚀`);
});