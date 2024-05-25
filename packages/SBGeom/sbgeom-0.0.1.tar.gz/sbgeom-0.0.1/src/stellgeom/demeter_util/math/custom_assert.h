#include "iostream"

/// ASSERT(condition) checks if the condition is met, and if not, calls
/// ABORT with an error message indicating the module and line where
/// the error occurred.
#ifdef CHECK_ASSERT_SB
#define sb_assert(x)                                                                \
    if (!(x)) {                                                                     \
        std::cerr<< "Assertion failed in"<<__FILE__<<", line"<<__LINE__<<std::endl; \
        abort();                                                                    \
    }                                                                               \
    else   // This 'else' exists to catch the user's following semicolon
#else
#define sb_assert(x) /*nothing*/
#endif
