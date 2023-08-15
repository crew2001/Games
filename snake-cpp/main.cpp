#include "snake.h"
#include "standard-header.h"

int main(){
    // Setup the window and renderer
    SDL_Window *window = nullptr;
    SDL_Renderer* renderer = nullptr;
    SDL_Event e;
    SDL_Init(SDL_INIT_EVERYTHING);
    // start the direction to the right
    // initialise the snake object
    Snake snake;

    // draw the board

    int speed = 1;
    // Snake head position
    SDL_CreateWindowAndRenderer(1280,720,0,&window,&renderer);
    int count =0;
    snake.addFood();
    // Create the game loop
    bool running = true;
    while(running){
        snake.moving();
        while(SDL_PollEvent(&e)){
            if (e.type == SDL_QUIT){
                running=false;
                break;
            }
            if (e.type==SDL_KEYDOWN){
                snake.directionChange(e);
                break;
            }
        }
        SDL_SetRenderDrawColor(renderer,0,0,0,255);
        SDL_RenderClear(renderer);
        SDL_SetRenderDrawColor(renderer,255,255,255,255);
        SDL_SetWindowTitle( window,to_string(count).c_str());
        snake.collisionSelf(running);
        snake.drawFood(renderer);
        snake.drawBody();
        snake.draw(renderer);
        if (snake.collisionFood()){
            snake.size+=30;
            snake.addFood();
            count +=1;
        }
        SDL_SetRenderDrawColor(renderer,250,250,250,250);
        SDL_Rect board{0,0,1280,720};
        SDL_RenderDrawRect(renderer,&board);
        SDL_RenderPresent(renderer);
        SDL_Delay(speed);
    }
    cout << "Final score = " << count << endl;
    return 0;

}