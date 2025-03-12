module;
#include <string_view>

export module library;

namespace lib {
export std::string_view version() {
  return "2.0";
}

} // namespace lib
