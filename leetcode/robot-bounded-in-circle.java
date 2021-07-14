class Solution {
    public boolean isRobotBounded(String instructions) {
        int[][] moves = {{0,1}, {1,0}, {0,-1}, {-1,0}}; // possible directions that the robot can f 
        int x = 0, y = 0;
        int dir = 0;
        
        for(int i = 0; i < instructions.length(); ++i) {
            if(instructions.charAt(i) == 'G') {
                x += moves[dir][0];
                y += moves[dir][1];
            }
            if(instructions.charAt(i) == 'L') {
                dir = (dir + 3) % 4;
            }
            if(instructions.charAt(i) == 'R') {
                dir = (dir + 1) % 4;
            }
        }
        // if the robot has returned to the starting position, they are in a circle
        // else, if the robot is not facing north, they will eventually reach the
        // center again after the instructions are executed a few more times
        // (the number of times exactly depends on the direction it is facing)
        return (x == 0 && y == 0) || (dir > 0);
    }
}
