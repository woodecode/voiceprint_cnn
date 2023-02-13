#include "normalize_2d.h"

/*
from:
0.128805,58.015791,19.898848,83.252204,60.221189,49.398402,36.059200,92.230876,
84.703620,76.855921,17.922786,88.420124,73.139417,52.863579,31.293404,1.542522,
9.409070,37.516899,15.164467,17.077697,101.759326,45.879818,12.258494,0.480664,
0.917345,38.899200,54.729685,58.798047,61.945923,62.501985,17.112255,68.254241,
to:
0.000000,0.521083,0.119660,0.927562,0.000000,0.211680,1.000000,1.000000,
1.000000,1.000000,0.069716,1.000000,0.310997,0.420147,0.799762,0.011573,
0.109728,0.000000,0.000000,0.000000,1.000000,0.000000,0.000000,0.000000,
0.009324,0.035138,1.000000,0.584790,0.041522,1.000000,0.203933,0.738675,
*/

/**
 * @author woodeCode
 * @brief the same as `sklearn.preprocessing.minmax_scale()`, normalize by column
 * @param arr_ret: normalized array
 * @param arr_src: the original array
 * @return None
*/
void normalize2D(_normailze2d_ret_type_ (*arr_ret)[COL_2D], _normailze2d_src_type_ (*arr_src)[COL_2D])
{
    int i, j = 0;
    /* 
     * Reference: sklearn.preprocessing.minmax_scale()
     * X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
     * X_scaled = X_std * (max - min) + min 
     */
    for (j = 0; j < COL_2D; j++) {
        /* store min and max position of value */
        int min_pos, max_pos = 0;
        /* find min and max position of value */
        for (i = 0; i < ROW_2D; i++) {
            if(arr_src[i][j] > arr_src[max_pos][j]) max_pos = i; 
            if(arr_src[i][j] < arr_src[min_pos][j]) min_pos = i;
        }
        /* calculate every element and store into arr_ret */
        for (i = 0; i < ROW_2D; i++) {
            arr_ret[i][j] = (arr_src[i][j] - arr_src[min_pos][j]) * 1.0 / 
                            (arr_src[max_pos][j] - arr_src[min_pos][j]);
        }
    }
}


#include <stdlib.h>
#include <stdio.h>

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