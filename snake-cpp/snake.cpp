#include "snake.h"


void Snake::draw(SDL_Renderer* renderer){
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        for_each(body.begin(),body.end(),[&](auto& bod){
            SDL_RenderFillRect(renderer, &bod);
        });
        SDL_RenderFillRect(renderer, &head);
}

void Snake::addFood(){
    SDL_Rect fo{rand()%1000,rand()%700,30,30};
    food = fo;
}

void Snake::drawFood(SDL_Renderer* renderer){
    SDL_SetRenderDrawColor(renderer,255,255,255,255);
    SDL_RenderFillRect(renderer,&food);
}

bool Snake::collisionFood(){
    if (SDL_HasIntersection(&food,&head)){
        return true;
    }
    return false;
}

void Snake::drawBody(){
    body.push_front(head);
    while(body.size()>size){
        body.pop_back();
    }
}

void Snake::collisionSelf(bool &running){
    for_each(body.begin(),body.end(),[&](auto& bod_part){
        if (head.x==bod_part.x and head.y==bod_part.y){
            running =false;
        }
        });
}

void Snake::directionChange(SDL_Event event){
    if (event.type== SDL_KEYDOWN){
        switch(event.key.keysym.sym){
        case SDLK_UP:{
            if (direction!=3){
                direction=1;
            }
            break;
        }
        case SDLK_LEFT:{
            if (direction!=4){
                direction=2;
            }
            break;
        }
        case SDLK_DOWN:{
            if (direction!=1){
                direction=3;
            }
            break;
        }
        case SDLK_RIGHT:{
            if (direction!=2){
                direction=4;
            }
            break;
        }
    }
    }
}

void Snake::moving(){
    if (direction ==1){
        head.y--;
        if (head.y<0) head.y=720;
    }
    else if (direction ==2){
        head.x--;
        if (head.x<0) head.x=1280;
    }
    else if (direction ==3){
        head.y++;
        if (head.y>720) head.y=0;
    }
    else if (direction==4){
        head.x++;
        if (head.x>1280) head.x=0;
    }
}



