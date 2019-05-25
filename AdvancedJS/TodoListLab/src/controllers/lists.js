const { Router } = require('express');

const Item = require('../models/Item');
const List = require('../models/List');

const router = Router();

// Create
router.post('', async (req, res) => {

  const { name } = req.body;

  const list = new List({ name });
  try {
    await list.save();
    res.send(list);
  } catch(err) {
    res.status(400).send(err.message);
  }
});

// Read
router.get('', async (req, res) => {

  const { name } = req.body;

  const list = await List.findOne({ name: name }).populate('items');

  if(list){
    res.send(list);
    return;
  } 

  res.status(400).send('couldn\'t find list');

});

// Update
router.patch('', async (req, res) => {

  const { oldName, newName } = req.body;

  const list = await List.findOne({ name: oldName });

  if(list){
    list.set({ name: newName});
    
    try {
      await list.save();
      res.send(list);
      return;
    } catch(err) {
      res.status(400).send(err.message);
    }
  } 

  res.status(400).send('failed to update list');

});

// Delete
router.delete('', async (req, res) => {

  const { name } = req.body;

  const list = await List.findOne({ name: name });

  if(list){
    const items = await Item.find({ list: list._id });

    items.forEach(async (item) => {
      await item.remove();
    });
    await list.remove();
  }

  res.send(`List: '${list.name}' deleted`);
  return;

});

module.exports = router;