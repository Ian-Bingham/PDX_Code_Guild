const { Router } = require('express');

const List = require('../models/List');

const router = Router();

router.post('', async (req, res) => {

  const { name } = req.body;

  const list = new List({ name });
  try {
    await list.save();
    res.send({
      ...list._doc,
    });
  } catch(err) {
    res.status(400).send(err.message);
  }
});

module.exports = router;