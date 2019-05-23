const mongoose = require('mongoose');

const personSchema = mongoose.Schema({
  firstname: {
    type: String,
    minlength: 2,
    maxlength: 24,
    required: true,
  },
  lastname: {
    type: String,
    minlength: 2,
    maxlength: 24,
    required: true,
  },
  username: {
    type: String,
    minlength: 5,
    maxlength: 15,
    required: true,
    unique: true,
  },
  age: {
    type: Number,
    required: true,
  },
}, {
  timestamps: true
});

const Person = mongoose.model('Person', personSchema);

module.exports = Person;