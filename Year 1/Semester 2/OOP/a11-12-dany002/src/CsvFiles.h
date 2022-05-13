//
// Created by moldo on 4/7/2022.
//

#ifndef A8_9_DANY002_CSVFILES_H
#define A8_9_DANY002_CSVFILES_H
#include "WatchList.h"
#include <string>

class CsvFiles : public WatchList{
private:
    std::string text_file;
public:

    CsvFiles(const std::string& text_file);
    ~CsvFiles();
    CsvFiles();
    CsvFiles(const CsvFiles& txt);
    void add_movie(const Movie& m) override;
    void delete_movie_from_watch_list(const std::string& title) override;
    void save_file() override;
    void load_file();
    std::string get_file_name();
};


#endif //A8_9_DANY002_CSVFILES_H
