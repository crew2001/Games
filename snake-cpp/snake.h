#pragma once
#include "standard-header.h"

class Snake{
    public:
    deque<SDL_Rect> body;
    SDL_Rect head;
    int size;
    SDL_Rect food;
    int direction=2;
    // Default constructor for snake 
    Snake(){
        size = 20;
        SDL_Rect temp{40,40,40,40};
        head = temp;
        body.push_front(head);
    };

    void draw(SDL_Renderer* renderer);
    void drawBody();
    void directionChange(SDL_Event event);
    void moving();
    void growing();

    void drawFood(SDL_Renderer* renderer);
    void addFood();

    bool collisionFood();
    void collisionSelf(bool &running);

};
