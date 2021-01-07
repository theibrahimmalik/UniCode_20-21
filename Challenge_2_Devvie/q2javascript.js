devvie = function (input) {
  // Your code goes here
  var invalid = false;
  var result = 0;
  var cordinates = { x: 0, y: 0 };
  var currentDirection = "+x";

  const action = {
    F: () => {
      if (currentDirection === "+x") {
        cordinates.x = cordinates.x + 1;
      }
      if (currentDirection === "-x") {
        cordinates.x = cordinates.x - 1;
      }
      if (currentDirection === "+y") {
        cordinates.y = cordinates.y + 1;
      }
      if (currentDirection === "-y") {
        cordinates.y = cordinates.y - 1;
      }
    },

    R: () => {
      if (currentDirection === "+x") currentDirection = "-y";
      if (currentDirection === "-x") currentDirection = "+y";
      if (currentDirection === "-y") currentDirection = "-x";
      if (currentDirection === "+y") currentDirection = "+x";
    },
    L: () => {
      if (currentDirection === "+x") currentDirection = "+y";
      if (currentDirection === "-x") currentDirection = "-y";
      if (currentDirection === "-y") currentDirection = "+x";
      if (currentDirection === "+y") currentDirection = "-x";
    },
  };

  for (var i = 0; i < input.length; i++) {
    if (action[input[i]]) {
      action[input[i]]();
    } else {
      invalid = true;
      break;
    }
  }

  if (
    (cordinates.x !== 0 || cordinates.y !== 0) &&
    (currentDirection === "-x" || currentDirection === "-y")
  ) {
    result += 2;
  }
  if (
    (cordinates.x !== 0 || cordinates.y !== 0) &&
    (currentDirection === "+x" || currentDirection === "-y")
  ) {
    result += 2;
  }

  result += Math.abs(cordinates.x);
  result += Math.abs(cordinates.y);

  // return invalid? 0:result

  console.log(cordinates, currentDirection, result);
};
