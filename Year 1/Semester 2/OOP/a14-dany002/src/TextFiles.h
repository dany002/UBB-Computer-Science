//
// Created by moldo on 4/6/2022.
//

#ifndef A8_9_DANY002_TEXTFILES_H
#define A8_9_DANY002_TEXTFILES_H

#include "Repository.h"
#include <string>

class TextFiles : public Repository {
private:
    std::string file_name;
public:

    TextFiles(const std::string& file_name);
    ~TextFiles();
    TextFiles();
    TextFiles(const TextFiles& txt);
    void add_movie(const Movie& m) override;
    void delete_movie(const std::string& title) override;
    void update_movie_trailer(const std::string& title, const std::string& new_trailer) override;
    void save_file();
    void load_file();
    void increment_likes(const std::string& title) override;
    Movie get_specific_movie(const std::string& title) override;
};


#endif //A8_9_DANY002_TEXTFILES_H
