/**
 * @file /include/ecl/filesystem/config.hpp
 * 
 * @brief Pre-processed macros that define time for the platform.
 * 
 * Cmake is used to check/verify your target platform parameters related
 * to filesystem functions. At the moment this is all automated. If ever this
 * needs to change (i.e. if we need to hand configure some macros as per
 * ecl_config style) then we should move this to ecl_config itself.
 **/
/*****************************************************************************
** Guards
*****************************************************************************/

#ifndef ECL_FILESYSTEM_CONFIG_HPP_
#define ECL_FILESYSTEM_CONFIG_HPP_

/*****************************************************************************
** Include
*****************************************************************************/

#include <ecl/config/ecl.hpp>

/**
 * @addtogroup Macros
 * @{
**/

/*****************************************************************************
** Private macros
*****************************************************************************/
/**
 * @def ECL_PRIVATE_HAS_POSIX_REALPATH
 *
 * @brief Can utilise the posix realpath function from -lrt.
**/
#define ECL_PRIVATE_HAS_POSIX_REALPATH

/*****************************************************************************
** Public macros
*****************************************************************************/

/**
 * @}
 **/

#endif /* ECL_FILESYSTEM_CONFIG_HPP_ */
 
