const mongoose = require('mongoose');

const connectDatabase = () => {
  mongoose.connect('mongodb://localhost:27017/express-passport-jwt', {
    useCreateIndex: true,
    useNewUrlParser: true,
    useFindAndModify: false,
  });

  console.log('Connected to database...');

  mongoose.connection.on('error', (err) => {
    console.error(err);
    process.exit(-1);
  });
};

module.exports = {
  connectDatabase,
};