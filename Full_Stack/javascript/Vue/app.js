new Vue({
  el: '#vue-app',
  data: {
    name: 'Ian',
    job: 'Gamer',
    website: 'http://www.neopets.com/',
    websiteTag: '<a href="https://www.youtube.com/" target="_blank">Youtube</a>',
    age: 22,
    x: 0,
    y: 0,
    a: 0,
    b: 0,
    available: false,
    nearby: false,
    error: false,
    success: false,
    characters: ['Mario', 'Luigi', 'Yoshi', 'Bowser'],
    ninjas: [
      {name: 'Ryu', age: 25},
      {name: 'Xiao', age: 35},
      {name: 'Ken', age: 55}
    ]
  },
  methods: {
    greet: function(time) {
      return `Good ${time} ${this.name}!`;
    },
    add: function(inc) {
      this.age += inc;
    },
    subtract: function(dec) {
      this.age -= dec;
    },
    updateXY: function(event) {
      this.x = event.offsetX;
      this.y = event.offsetY;
    },
    logName: function() {
      console.log("you entered your name")
    },
    logAge: function() {
      console.log("you entered your age")
    },
    updateName: function() {
      console.log("you entered your name")
    },
    updateAge: function() {
      console.log("you entered your age")
    }
    // addToA: function() {
    //   return this.a + this.age;
    // },
    // addToB: function() {
    //   return this.b + this.age;
    // },
  },
  computed: {
    addToA: function() {
      return this.a + this.age;
    },
    addToB: function() {
      return this.b + this.age;
    },
    compClasses: function() {
      return {
        available: this.available,
        nearby: this.nearby
      }
    }
  }
})
