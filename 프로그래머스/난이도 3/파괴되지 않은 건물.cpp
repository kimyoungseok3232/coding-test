// https://school.programmers.co.kr/learn/courses/30/lessons/92344

#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    int deg[board.size()+1][board[0].size()+1];
    fill(&deg[0][0], &deg[board.size()][board[0].size()+1], 0);
    
    for(int i = 0 ; i < skill.size() ; i++){
        if(skill[i][0] == 1){
            deg[skill[i][1]][skill[i][2]] -=skill[i][5];
            deg[skill[i][1]][skill[i][4]+1] +=skill[i][5];
            deg[skill[i][3]+1][skill[i][2]] +=skill[i][5];
            deg[skill[i][3]+1][skill[i][4]+1] -=skill[i][5];
            
        }
        else{
            deg[skill[i][1]][skill[i][2]] +=skill[i][5];
            deg[skill[i][1]][skill[i][4]+1] -=skill[i][5];
            deg[skill[i][3]+1][skill[i][2]] -=skill[i][5];
            deg[skill[i][3]+1][skill[i][4]+1] +=skill[i][5];
        }
    }
    
            
    for(int i = 0 ; i < board.size() ; i++){
        for(int j = 0 ; j < board[0].size() ; j++){
            deg[i][j+1] += deg[i][j];
        }
    }
    
    for(int j = 0 ; j < board[0].size() ; j++){
        for(int i = 0 ; i < board.size() ; i++){
            deg[i+1][j] += deg[i][j];
        }
    }

    for(int i = 0 ; i < board.size() ; i++){
        for(int j = 0 ; j < board[0].size() ; j++){

            board[i][j] += deg[i][j];
            
            if(board[i][j]>0)
                answer++;

        }
    }

    return answer;
}