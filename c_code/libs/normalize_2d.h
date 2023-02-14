#ifndef __NORMALIZE_2D__
#define __NORMALIZE_2D__

#ifdef __cplusplus
extern "C"{
#endif

#define ROW_2D 5
#define COL_2D 8

typedef double _normailze2d_src_type_;

typedef double _normailze2d_ret_type_;

void normalize2D(_normailze2d_ret_type_ (*arr_ret)[COL_2D], 
                    _normailze2d_src_type_ (*arr_src)[COL_2D]);



#ifdef __cplusplus
}
#endif

#endif