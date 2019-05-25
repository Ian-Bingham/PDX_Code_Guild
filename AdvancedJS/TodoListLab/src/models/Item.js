const mongoose = require('mongoose');
const { ObjectId } = mongoose.Schema.Types;

const itemSchema = mongoose.Schema({
  description: { 
    type: String,
    required: true,
  },
  list: {
    type: ObjectId,
    ref: 'List',
    required: true,
  }
});

const Item = mongoose.model('Item', itemSchema);

module.exports = Item;