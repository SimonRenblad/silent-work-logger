#include <iostream>
#include <chrono>
#include <ctime>

const int SEC_PER_HOUR = 3600;
const int SEC_PER_MIN = 60;

int main(){
 
    auto start = std::chrono::system_clock::now();

    std::cin.get();

    auto end = std::chrono::system_clock::now();

    std::chrono::duration<double> diff = end - start;

    int seconds = std::chrono::duration_cast<std::chrono::seconds>(diff).count();
    
    //get the number of hours
    int hours = seconds / SEC_PER_HOUR;
    seconds = seconds % SEC_PER_HOUR;

    //get the number of minutes
    int minutes = seconds / SEC_PER_MIN;

    //get the number of seconds
    seconds = seconds % SEC_PER_MIN;

    //convert to time_t
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);

    std::tm *start_time_tm = std::localtime(&start_time);

    std::cout << start_time_tm->tm_mday << "/";
    std::cout << 1 + start_time_tm->tm_mon << "/";
    std::cout << 1900 + start_time_tm->tm_year << ": ";

    //print
    std::cout << hours << "h" << minutes << "m" << seconds << "s" << std::endl;

    return 0;

}
