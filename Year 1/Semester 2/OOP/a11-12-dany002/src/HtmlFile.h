//
// Created by moldo on 4/6/2022.
//

#ifndef A8_9_DANY002_HTMLFILE_H
#define A8_9_DANY002_HTMLFILE_H
#include "WatchList.h"
#include <string>

class HtmlFile : public WatchList {
private:
    std::string text_file;
public:
    HtmlFile(const std::string& file_name);
    ~HtmlFile();
    HtmlFile();
    HtmlFile(const HtmlFile& txt);
    void add_movie(const Movie& m) override;
    void delete_movie_from_watch_list(const std::string& title) override;
    void save_file() override;
    void load_file();
    std::string get_file_name();
};


#endif //A8_9_DANY002_HTMLFILE_H
