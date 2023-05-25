#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; // Return an empty object if w or h is invalid
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
const rect1 = new Rectangle(4, 3);
rect1.print(); // Prints a rectangle with width 4 and height 3 using "X"

const rect2 = new Rectangle(5, 2);
rect2.rotate(); // Exchanges width and height
rect2.print(); // Prints a rotated rectangle with width 2 and height 5 using "X"

const rect3 = new Rectangle(6, 4);
rect3.double(); // Doubles the width and height
rect3.print(); // Prints a rectangle with width 12 and height 8 using "X"
