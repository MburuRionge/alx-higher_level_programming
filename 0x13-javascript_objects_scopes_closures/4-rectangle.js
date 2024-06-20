#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    // Check if w and h are positive integers
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is not a positive integer, create an empty object
      this.width = 0;
      this.height = 0;
    }
  }

  print() {
    // Print the rectangle using 'X' character
    if (this.width > 0 && this.height > 0) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate() {
    // Exchange width and height of the rectangle
    if (this.width > 0 && this.height > 0) {
      let temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  double() {
    // Multiply width and height of the rectangle by 2
    if (this.width > 0 && this.height > 0) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle; // Exporting the Rectangle class
