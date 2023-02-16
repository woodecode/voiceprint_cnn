#include <stdio.h>
#include <stdlib.h>
#include "normalize_2d.h"
#include "trim_audio.h"

void normalize2D_test(void);
void trimAudio_test(void);


int main(int argc, char const *argv[])
{
    normalize2D_test();
    
    // system("pause");
    return 0;
}


void normalize2D_test(void)
{
    double arr_ret[ROW_2D][COL_2D];
    double arr[ROW_2D][COL_2D];

    printf("from:\n");
    for(int i = 0; i < ROW_2D; i++) {
        for(int j = 0; j < COL_2D; j++) {
            arr[i][j] = (double) rand()*0.001*3.1415926;
            arr_ret[i][j] = 0.0; 
            printf("%2.6lf,",arr[i][j]);
        }
        printf("\n");
    }

    /* normalize 2d-array `arr` */
    normalize2D(arr_ret, arr);
    
    printf("to:\n");
    for(int i = 0; i < ROW_2D; i++) {
        for(int j = 0; j < COL_2D; j++) {
            printf("%2.6lf,",arr_ret[i][j]);
        }
        printf("\n");
    }
}


void trimAudio_test(void)
{

}



