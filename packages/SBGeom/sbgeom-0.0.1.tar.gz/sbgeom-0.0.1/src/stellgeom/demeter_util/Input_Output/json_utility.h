#include "json.h"
#include "iostream"
#include "fstream"
#include <string>
auto Parse_Input_JSON(char* argv){
    using json = nlohmann::json;
    json result;
    try{
        std::cout<<"Trying to open the JSON file specified by '" << argv<<"' ...."<< std::endl;

        std::ifstream f(argv);
        
        result = json::parse(f);
 
        //std::cout<<"Input JSON:"<<std::endl<<result.dump(4)<<std::endl<<std::endl;
    }
    catch(const std::exception& e){
        std::cout<<e.what()<<" in Parse_Input_JSON in json_utility.h. Aborting..."<<std::endl;
        abort();
    }
    return result;
}



void Output_Terminal_Header(std::string name){
    auto length = name.length();
    unsigned total_header_length = 60;
    if(total_header_length - length < 0){throw(name+" is too long to be represented as a header....");};
    unsigned left_header = (total_header_length - length + 1) /2;
    unsigned right_header = (total_header_length - length) / 2;
    std::cout<<std::string(left_header,'=')<<name<<std::string(right_header,'=')<<std::endl;
    
}
