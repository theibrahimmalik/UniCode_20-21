public int shortestDist00(){
        int x = Math.abs(currentPos[0]);
        int y = Math.abs(currentPos[1]);
        int r = currentPos[2];
        if(x == 0 && y == 0)return 0;
        int[] sides = getSides();
        int addAmount = 1;
        int diff = -1;
        if(sides[0] == -1) diff = Math.abs(r - sides[1]);
        else if(sides[1] == -1) diff = Math.abs(r - sides[0]);
        else{
            for(int i : sides)
                if (r == i){addAmount = 2;break;}
        }
        if(diff == 0)addAmount = 2;
        else if(diff == 2)addAmount = 0;
        return addAmount + x + y;
    }
    public int[] getSides(){
        int[] sides = {-1, -1};
        if(currentPos[0] > 0)sides[0] = 1;
        else if(currentPos[0] < 0)sides[0] = 3;
        if(currentPos[1] > 0)sides[1] = 0;
        else if(currentPos[1] < 0)sides[1] = 2;
        return sides;
    }
