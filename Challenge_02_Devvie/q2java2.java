public static int devvie(String input) {
  String cleanInput = input.replaceAll("[^FLR]","");
  int facing = 0;
  int x = 0;
  int y = 0;
  int stepCount = 0;

  // determine end position (x,y)
  for (char step : cleanInput.toCharArray()) {
    switch (step) {
      case 'F':
        switch (facing) {
          case 0:
            y++;
            break;
          case 1:
            x++;
            break;
          case 2:
            y--;
            break;
          case 3:
            x--;
            break;
        }
        break;

      case 'L':
        facing = (facing <= 0) ? 3 : facing-1;
        break;
      case 'R':
        facing = (facing >= 3) ? 0 : facing+1;
        break;
    }
  }


  // is orig value in the negative
  boolean flippedX = (x < 0);
  boolean flippedY = (y < 0);

  // convert all values to positive
  x = Math.abs(x);
  y = Math.abs(y);

  // count number of steps to make y co-ord 0
  if (y > 0) {
    if (facing == 1 || facing == 3)  ++stepCount;

    else if (facing == 0 && !flippedY || facing == 2 && flippedY) stepCount += 2;

    facing = 2;

    while (y != 0) {
      --y;
      ++stepCount;
    }
  }

  // count number of steps to make x co-ord 0
  if (x > 0) {
    if (facing == 0 || facing == 2) ++stepCount;

    else if (facing == 1 && !flippedX || facing == 3 && flippedX) stepCount += 2;

    while (x != 0) {
      --x;
      ++stepCount;
    }
  }

  return stepCount;
}
