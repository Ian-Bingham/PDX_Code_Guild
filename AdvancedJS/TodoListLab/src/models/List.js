const mongoose = require('mongoose');

const listSchema = mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
}, {
  toJSON: {
    virtuals: true
  },
  timestamps: true,
});

listSchema.virtual('items', {
  ref: 'Item',
  localField: '_id',
  foreignField: 'list',
  justOne: false
});

const List = mongoose.model('List', listSchema);

module.exports = List;