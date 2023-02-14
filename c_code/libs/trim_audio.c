#include "trim_audio.h"
#include <math.h>
#include <string.h>

#define _TRIM_SQUARE(x)     pow(x, 2)
#define _TRIM_SQRT(x)       sqrt(x)
#define _TRIM_LOG10(x)      log10(x)


double calcRootMeanSquare(double *data, uint16_t len)
{
    double sum = 0;
    for (int i = 0; i < len; i++) {
        sum += _TRIM_SQUARE(data[i]);
    }
    double ret = _TRIM_SQRT(sum / len);
    return ret;
}


double convertRmsToDb(double rms)
{
    return 20 * _TRIM_LOG10(rms);
}


/**
 * @return 
*/
int trimAudio(AudioTrimConfig *config)
{
    // The number of frames in the raw audio data
    uint16_t num_frames = config->raw_len / config->frame_length;
    // The pointer to the current frame in the raw audio data
    uint16_t p_raw = 0;
    // The pointer to the current frame in the trimmed audio data
    uint16_t p_trim = 0;
    // The energy of the current frame in decibels
    double energy = 0;
    
    // Loop through the frames in the raw audio data
    while(p_raw + config->frame_length < num_frames) {
        // Calculate the energy of the current frame
        energy = calcRootMeanSquare(&config->raw_data[p_raw], 
                                    config->frame_length);
        // Convert the energy into decibels
        energy = convertRmsToDb(energy);

        if( energy >= config->threshold_db 
            && p_trim + config->frame_length < config->trim_len) 
        {
            memcpy( &config->trim_data[p_trim],
                    &config->raw_data[p_raw],
                    config->frame_length);

            p_trim += config->frame_length;
        }

        p_raw += config->hop_length;
    }
    return 0;
}
