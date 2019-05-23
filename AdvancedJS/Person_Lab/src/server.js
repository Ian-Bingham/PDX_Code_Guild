const bodyParser = require('body-parser');
const { connectDatabase } = require('./database');
const express = require('express');
const personsController = require('./controllers/persons');

connectDatabase();
const app = express();
const port = 1234;

app.use(bodyParser.json());

app.use('/persons', personsController);

app.get('/', (req, res) => {
    res.send({test: 'test'});
});

app.listen(port, () => {
    console.log(`Listening at localhost:${port}...`);
});
