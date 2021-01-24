# time O(1)
# space O(N)
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.pos = set([(0,0)])
        self.snake = deque([(0,0)])
        self.n = height
        self.m = width
        self.food = food
        self.dir = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.snake[0]
        next_head = (head[0]+self.dir[direction][0], head[1]+self.dir[direction][1])
        tail = self.snake.pop()
        self.pos.remove(tail)
        if next_head in self.pos or not (0<=next_head[0]<self.n and 0<=next_head[1]<self.m):
            return -1
        
        cur_food = (-1,-1)
        if self.food:
            cur_food = tuple(self.food[0])
            
        self.snake.appendleft(next_head)
        self.pos.add(next_head)
        if next_head == cur_food:
            self.food.pop(0)
            self.snake.append(tail)
            self.pos.add(tail)
        return len(self.snake)-1
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)