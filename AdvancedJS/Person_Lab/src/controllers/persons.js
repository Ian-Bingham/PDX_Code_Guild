const { check, validationResult } = require('express-validator/check');
const Person = require('../models/Person');
const { Router } = require('express');

const router = Router();

router.post('/create', [
  check(['firstname', 'lastname', 'username', 'age']).exists(),
], async (req, res) => {
  const errors = validationResult(req);
  if(!errors.isEmpty()) {
    return res.status(422).send({ errors: errors.array() });
  }

  const { firstname, lastname, username, age } = req.body;

  const person = new Person({
    firstname,
    lastname,
    username,
    age
  });

  try {
    await person.save();
    res.send({
      ...person._doc,
    });
  } catch(error) {
    res.status(400).send(error.message);
  }
});

router.post('/update', [
  check(['firstname', 'lastname', 'username', 'age']).exists(),
], async (req, res) => {
  const errors = validationResult(req);
  if(!errors.isEmpty()) {
    return res.status(422).send({ errors: errors.array() });
  }

  const { userToUpdate, firstname, lastname, username, age } = req.body;

  const person = await Person.findOne({ username: userToUpdate });

  if(person){
    person.set(  
      {
        firstname,
        lastname,
        username,
        age
      }
    );
    person.save();

    res.send(`${username} updated`);
    return;
  }

  res.status(422).send('could not find user');

});

router.post('/delete', [
  check(['username']).exists(),
], async (req, res) => {
  const errors = validationResult(req);
  if(!errors.isEmpty()) {
    return res.status(422).send({ errors: errors.array() });
  }

  const { username } = req.body;

  const person = await Person.findOne({ username: username });

  if(person){
    person.remove();
    res.send(`${username} deleted`);
    return;
  }

  res.status(422).send('could not find user');
  
});

router.post('/show', [
  check(['username']).exists(),
], async (req, res) => {
  const errors = validationResult(req);
  if(!errors.isEmpty()) {
    return res.status(422).send({ errors: errors.array() });
  }

  const { username } = req.body;

  const person = await Person.findOne({ username: username });

  if(person){
    res.send(person);
    return;
  }

  res.status(422).send('could not find user');
  
});

module.exports = router;