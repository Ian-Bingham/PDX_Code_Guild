const bcrypt = require('bcrypt');
const passport = require('passport');
const jwt = require('jsonwebtoken');
const { Router } = require('express');
const { check, validationResult } = require('express-validator/check');

const User = require('../models/User');

const router = Router();

router.post('/sign-up', [
  check(['email', 'password', 'passwordConfirm']).exists(),
], async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(422).send({ errors: errors.array() });
  }

  const { email, password, passwordConfirm } = req.body;

  if(password !== passwordConfirm) {
    res.status(400).send({error: 'passwords do not match'});
    return;
  }

  const passwordHash = bcrypt.hashSync(password, 10);

  const user = new User({
    email,
    passwordHash,
  });

  try {
    await user.save();
    res.send({
      ...user._doc,
      passwordHash: undefined,
    });
  } catch(error) {
    res.status(400).send(error.message);
  }
});


router.post('/login', 
  passport.authenticate('local', { session: false }),
  (req, res) => {
    const token = jwt.sign(
      {
        _id: req.user._id,
        email: req.user.email,
      }, 
      'CHANGEMEPLEASE!',
      {
        expiresIn: "2 days",
      }
    );
    res.send({ token, expiresIn: "2 days" });
  }
);

router.get('/profile',
  passport.authenticate('jwt', { session: false }),
  (req, res) => {
    res.send({
      _id: req.user._id,
      email: req.user.email,
    });    
  }
);

module.exports = router;