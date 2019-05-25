const { Router } = require('express');

const Item = require('../models/Item');
const List = require('../models/List');

const router = Router();

// Create
router.post('', async (req, res) => {

  const { description } = req.body;

  const list = await List.findOne({});

  if(list){
    const item = new Item({ description, list });
  
    try {
      await item.save();
      res.send(item);
      return;
    } catch(err) {
      res.status(400).send(err.message);
    }
  }

  res.status(500).send('couldn\'t find list to add item to');

});

// Read
router.get('', async (req, res) => {

  const { description } = req.body;

  const item = await Item.findOne({ description: description });

  if(item){
    res.send(item);
    return;
  } 

  res.status(400).send('couldn\'t find item');

});

// Update
router.patch('', async (req, res) => {

  const { oldDescription, newDescription } = req.body;

  const item = await Item.findOne({ description: oldDescription });

  if(item){
    item.set({ description: newDescription});
    
    try {
      await item.save();
      res.send(item);
      return;
    } catch(err) {
      res.status(400).send(err.message);
    }
  } 

  res.status(400).send('failed to update item');

});

// Delete
router.delete('', async (req, res) => {

  const { description } = req.body;

  const item = await Item.findOne({ description: description });

  if(item){
    await item.remove();
    res.send(`item: ${item.description} deleted`);
    return;
  } 

  res.status(400).send('failed to delete item');

});

module.exports = router;