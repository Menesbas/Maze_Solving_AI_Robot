// Generated by gencpp from file control_toolbox/SetPidGains.msg
// DO NOT EDIT!


#ifndef CONTROL_TOOLBOX_MESSAGE_SETPIDGAINS_H
#define CONTROL_TOOLBOX_MESSAGE_SETPIDGAINS_H

#include <ros/service_traits.h>


#include <control_toolbox/SetPidGainsRequest.h>
#include <control_toolbox/SetPidGainsResponse.h>


namespace control_toolbox
{

struct SetPidGains
{

typedef SetPidGainsRequest Request;
typedef SetPidGainsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetPidGains
} // namespace control_toolbox


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::control_toolbox::SetPidGains > {
  static const char* value()
  {
    return "b06494a6fc3d5b972ded4e2a9a71535a";
  }

  static const char* value(const ::control_toolbox::SetPidGains&) { return value(); }
};

template<>
struct DataType< ::control_toolbox::SetPidGains > {
  static const char* value()
  {
    return "control_toolbox/SetPidGains";
  }

  static const char* value(const ::control_toolbox::SetPidGains&) { return value(); }
};


// service_traits::MD5Sum< ::control_toolbox::SetPidGainsRequest> should match
// service_traits::MD5Sum< ::control_toolbox::SetPidGains >
template<>
struct MD5Sum< ::control_toolbox::SetPidGainsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::control_toolbox::SetPidGains >::value();
  }
  static const char* value(const ::control_toolbox::SetPidGainsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::control_toolbox::SetPidGainsRequest> should match
// service_traits::DataType< ::control_toolbox::SetPidGains >
template<>
struct DataType< ::control_toolbox::SetPidGainsRequest>
{
  static const char* value()
  {
    return DataType< ::control_toolbox::SetPidGains >::value();
  }
  static const char* value(const ::control_toolbox::SetPidGainsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::control_toolbox::SetPidGainsResponse> should match
// service_traits::MD5Sum< ::control_toolbox::SetPidGains >
template<>
struct MD5Sum< ::control_toolbox::SetPidGainsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::control_toolbox::SetPidGains >::value();
  }
  static const char* value(const ::control_toolbox::SetPidGainsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::control_toolbox::SetPidGainsResponse> should match
// service_traits::DataType< ::control_toolbox::SetPidGains >
template<>
struct DataType< ::control_toolbox::SetPidGainsResponse>
{
  static const char* value()
  {
    return DataType< ::control_toolbox::SetPidGains >::value();
  }
  static const char* value(const ::control_toolbox::SetPidGainsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // CONTROL_TOOLBOX_MESSAGE_SETPIDGAINS_H
