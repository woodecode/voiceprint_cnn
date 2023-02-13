#ifndef __TRIM_AUDIO__
#define __TRIM_AUDIO__

#ifdef __cpluscplus
#endif

#include <stdint-gcc.h>

void trimAudio(uint16_t *trim_data, uint16_t trim_len,uint8_t threshold_db, 
                uint16_t *raw_data, uint16_t raw_len);

#ifdef __cpluscplus
#endif

#endif

