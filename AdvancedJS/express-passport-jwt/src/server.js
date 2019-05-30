const express = require('express');
const passport = require('passport');

const { connectDatabase } = require('./database');

const AuthController = require('./controllers/auth');

connectDatabase();

const app = express();
require('./passport');

app.use(express.json());
app.use(passport.initialize());

app.use('/auth', AuthController);

app.listen(4000, () => {
  console.log('Listening at localhost:4000...');
});