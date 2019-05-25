const { Router } = require('express');

const Item = require('../models/Item');
const List = require('../models/List');

const router = Router();

router.post('', async (req, res) => {

  const { description } = req.body;

  const list = await List.findOne({});

  if(list){
    const item = new Item({ description, list });
  
    try {
      await item.save();
      res.send({
        ...item._doc
      });
      return;
    } catch(err) {
      res.status(400).send(err.message);
    }
  }

  res.status(500).send('could not find list to add item to');

});

module.exports = router;