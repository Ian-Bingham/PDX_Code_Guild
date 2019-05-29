const mongoose = require('mongoose');
const { ObjectId } = mongoose.Schema.Types;

const itemSchema = mongoose.Schema({
  description: { 
    type: String,
    required: true,
  },
  completed: {
    type: Boolean,
    default: false
  },
  list: {
    type: ObjectId,
    ref: 'List',
    required: true,
  }
}, {
  timestamps: true,
});

const Item = mongoose.model('Item', itemSchema);

module.exports = Item;