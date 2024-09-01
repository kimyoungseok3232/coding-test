// https://school.programmers.co.kr/learn/courses/30/lessons/92334

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// id_list_len은 배열 id_list의 길이입니다.
// report_len은 배열 report의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.

int* solution(const char* id_list[], size_t id_list_len, const char* report[], size_t report_len, int k) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    //printf(report[0]);

    int reporttable[id_list_len][id_list_len];
    for(int i = 0 ; i < id_list_len ; i++){
        for(int j = 0 ; j < id_list_len ; j++){
            reporttable[i][j] = 0;
        } 
    }
    int who_reported[id_list_len];
    
    int* answer = (int*)calloc(id_list_len+1,sizeof(int));
    const char* reported_id;
    const char* reporter_id;
    int reported;
    int reporter;

    for(int j = 0 ; j < report_len ; j++){

        reporter_id = strtok(report[j]," ");

        for(int i = 0 ; i < id_list_len ; i++){
            if(strcmp(reporter_id,id_list[i])==0){
                reporter = i;
            }
        }
        
        reported_id = strtok(NULL," ");
        for(int i = 0 ; i < id_list_len ; i++){
            if(strcmp(reported_id,id_list[i])==0){
                reported = i;
            }
        }
        reporttable[reporter][reported]++;
        

    }
    
    for(int i = 0 ; i < id_list_len ; i++){
        who_reported[i] = 0;
        for(int j = 0 ; j < id_list_len ; j++){
            if(reporttable[j][i] > 0){
                who_reported[i]++;
            }
        } 
    }
    
    for(int i = 0 ; i < id_list_len ; i++){
        for(int j = 0 ; j < id_list_len ; j++){
            if(reporttable[j][i] > 0 && who_reported[i]>=k){
                answer[j]++;
            }
        } 
    }

    return answer;
}
