const express = require('express');
const bodyParser = require('body-parser');

const { connectDatabase } = require('./database');
const itemsController = require('./controllers/items');
const listsController = require('./controllers/lists');

connectDatabase();
const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use('/lists', listsController);
app.use('/items', itemsController);

app.get('/', (req, res) => {
  res.send({test: 'test'});
});

app.listen(port, () => {
  console.log(`Listening at localhost:${port}...`);
});
