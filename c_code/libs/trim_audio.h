#ifndef __TRIM_AUDIO__
#define __TRIM_AUDIO__

#ifdef __cpluscplus
#endif

#include <stdint-gcc.h>

typedef struct 
{
    double *raw_data;
    uint32_t raw_len;
    double *trim_data;
    uint32_t trim_len;
    uint32_t sr;
    uint16_t frame_length;
    uint16_t hop_length;
    uint8_t threshold_db;
} AudioTrimConfig;

int trimAudio(AudioTrimConfig *config);

#ifdef __cpluscplus
#endif

#endif

