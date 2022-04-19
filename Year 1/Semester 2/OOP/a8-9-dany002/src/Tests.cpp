/*
//
// Created by moldo on 3/19/2022.
//
#include <gtest/gtest.h>
#include "Movie.h"
#include "WatchList.h"
#include "Repository.h"
#include "DynamicVector.h"
#include "Controller.h"
#include "Exceptions.h"
#include <gmock/gmock.h>
#include <vector>

///                                     MOVIE TEST                                             ///


class MovieTest : public ::testing::Test {
protected:
    Movie movie;
    void SetUp() override{
        movie = Movie("Inception","SF", 2010, 300, "https://www.youtube.com/watch?v=YoHD9XEInc0");
    }
};

TEST_F(MovieTest, get_title){
    ASSERT_EQ(movie.get_title(), "Inception");
}

TEST_F(MovieTest, get_genre){
    ASSERT_EQ(movie.get_genre(), "SF");
}

TEST_F(MovieTest, get_trailer){
    ASSERT_EQ(movie.get_trailer(), "https://www.youtube.com/watch?v=YoHD9XEInc0");
}

TEST_F(MovieTest, get_year_of_release){
    ASSERT_EQ(movie.get_year_of_release(), 2010);
}

TEST_F(MovieTest, get_number_of_likes){
    ASSERT_EQ(movie.get_number_of_likes(), 300);
}

TEST_F(MovieTest, set_title){
    movie.set_title("F9");
    ASSERT_EQ(movie.get_title(), "F9");
}

TEST_F(MovieTest, set_genre){
    movie.set_genre("Romance");
    ASSERT_EQ(movie.get_genre(), "Romance");
}

TEST_F(MovieTest, set_trailer){
    movie.set_trailer("https://www.youtube.com/watch?v=Yo21sfaInc0");
    ASSERT_EQ(movie.get_trailer(), "https://www.youtube.com/watch?v=Yo21sfaInc0");
}

TEST_F(MovieTest, set_year_of_release){
    movie.set_year_of_release(1985);
    ASSERT_EQ(movie.get_year_of_release(), 1985);
}

TEST_F(MovieTest, set_number_of_likes){
    movie.set_number_of_likes(142);
    ASSERT_EQ(movie.get_number_of_likes(), 142);
}

TEST_F(MovieTest, default_constructor_and_copy_constructor){
    Movie mov;
    Movie mov2 = movie;
    ASSERT_EQ(movie.get_number_of_likes(), mov2.get_number_of_likes());
    ASSERT_EQ(movie.get_year_of_release(), mov2.get_year_of_release());
    ASSERT_EQ(movie.get_trailer(), mov2.get_trailer());
    ASSERT_EQ(movie.get_genre(), mov2.get_genre());
    ASSERT_EQ(movie.get_title(), mov2.get_title());
}

///                                     DYNAMIC VECTOR TEST                                             ///

class DynamicVectorTest : public ::testing::Test {
protected:
    DynamicVector<Movie> vector;
    Movie movie;
    Movie movie2;
    void SetUp() override{
        movie = Movie("Inception","SF", 2010, 300, "https://www.youtube.com/watch?v=YoHD9XEInc0");
        movie2 = Movie("Ted", "Comedy", 2012, 1000, "https://www.youtube.com/watch?v=9fbo_pQvU7M");
        vector = DynamicVector<Movie>();
    }
};

TEST_F(DynamicVectorTest, add_element){
    ASSERT_EQ(vector.get_size(), 0);
    vector.add(movie);
    ASSERT_EQ(vector.get_size(), 1);
    vector.add(movie2);
    ASSERT_EQ(vector.get_size(), 2);
}

TEST_F(DynamicVectorTest, get_element){
    vector.add(movie);
    vector.add(movie2);
    ASSERT_EQ(vector.get_element(0).get_title(), movie.get_title());
    ASSERT_EQ(vector.get_element(0).get_genre(), movie.get_genre());
    ASSERT_EQ(vector.get_element(0).get_trailer(), movie.get_trailer());
    ASSERT_EQ(vector.get_element(0).get_year_of_release(), movie.get_year_of_release());
    ASSERT_EQ(vector.get_element(0).get_number_of_likes(), movie.get_number_of_likes());
}

TEST_F(DynamicVectorTest, get_element_throw_exception){
    vector.add(movie);
    try{
        vector.get_element(3);
    }
    catch(IndexGreaterThanSize const& err){
        EXPECT_STREQ(err.what(), "The index that u gave is greater than the size of the array.");
    }
}

TEST_F(DynamicVectorTest, pop){
    vector.add(movie);
    vector.add(movie2);
    ASSERT_EQ(vector.get_size(), 2);
    vector.pop();
    ASSERT_EQ(vector.get_size(), 1);
}

TEST_F(DynamicVectorTest, pop_throw_exception){
    vector.add(movie);
    vector.pop();
    try{
        vector.pop();

    }
    catch(LengthIsZero const& err){
        EXPECT_STREQ(err.what(), "The length is zero.");
    }
}

TEST_F(DynamicVectorTest, get_size){
    vector.add(movie);
    ASSERT_EQ(vector.get_size(), 1);
    vector.add(movie2);
    ASSERT_EQ(vector.get_size(), 2);
}

TEST_F(DynamicVectorTest, get_capacity){
    vector.add(movie);
    ASSERT_EQ(vector.get_capacity(), 1);
    vector.add(movie2);
    ASSERT_EQ(vector.get_capacity(), 2);
}

TEST_F(DynamicVectorTest, get_all_elems){
    vector.add(movie);
    ASSERT_EQ(vector.get_all_elems()->get_number_of_likes(), movie.get_number_of_likes());
    ASSERT_EQ(vector.get_all_elems()->get_year_of_release(), movie.get_year_of_release());
    ASSERT_EQ(vector.get_all_elems()->get_trailer(), movie.get_trailer());
    ASSERT_EQ(vector.get_all_elems()->get_genre(), movie.get_genre());
    ASSERT_EQ(vector.get_all_elems()->get_title(), movie.get_title());
}

TEST_F(DynamicVectorTest, remove_element_from_a_specific_index){
    vector.add(movie);
    vector.add(movie2);
    ASSERT_EQ(vector.get_size(), 2);
    vector.remove_element_from_a_specific_index(0);
    ASSERT_EQ(vector.get_size(), 1);
    ASSERT_EQ(vector.get_all_elems()->get_number_of_likes(), movie2.get_number_of_likes());
    ASSERT_EQ(vector.get_all_elems()->get_year_of_release(), movie2.get_year_of_release());
    ASSERT_EQ(vector.get_all_elems()->get_trailer(), movie2.get_trailer());
    ASSERT_EQ(vector.get_all_elems()->get_genre(), movie2.get_genre());
    ASSERT_EQ(vector.get_all_elems()->get_title(), movie2.get_title());
}

TEST_F(DynamicVectorTest, remove_element_from_a_specific_index_throw_exception){
    vector.add(movie);
    try{
        vector.remove_element_from_a_specific_index(2);

    }
    catch(IndexGreaterThanSize const& err){
        EXPECT_STREQ(err.what(), "The index that u gave is greater than the size of the array.");
    }
}

TEST_F(DynamicVectorTest, set_element){
    vector.add(movie);
    ASSERT_EQ(vector.get_element(0).get_number_of_likes(), movie.get_number_of_likes());
    ASSERT_EQ(vector.get_element(0).get_title(), movie.get_title());
    ASSERT_EQ(vector.get_element(0).get_genre(), movie.get_genre());
    ASSERT_EQ(vector.get_element(0).get_trailer(), movie.get_trailer());
    ASSERT_EQ(vector.get_element(0).get_year_of_release(), movie.get_year_of_release());
    vector.set_element(movie2, 0);
    ASSERT_EQ(vector.get_element(0).get_number_of_likes(), movie2.get_number_of_likes());
    ASSERT_EQ(vector.get_element(0).get_title(), movie2.get_title());
    ASSERT_EQ(vector.get_element(0).get_genre(), movie2.get_genre());
    ASSERT_EQ(vector.get_element(0).get_trailer(), movie2.get_trailer());
    ASSERT_EQ(vector.get_element(0).get_year_of_release(), movie2.get_year_of_release());
}

TEST_F(DynamicVectorTest, set_element_throw_exception){
    vector.add(movie);
    try{
        vector.set_element(movie2, 2);

    }
    catch(IndexGreaterThanSize const& err){
        EXPECT_STREQ(err.what(), "The index that u gave is greater than the size of the array.");
    }
}

TEST_F(DynamicVectorTest, copy_constructor){
    vector.add(movie);
    vector.add(movie2);
    DynamicVector<Movie> vector2 = vector;
    ASSERT_EQ(vector2.get_size(), 2);
    ASSERT_EQ(vector2.get_capacity(), 2);
}

///                                     REPOSITORY TEST                                             ///



class RepositoryTest : public ::testing::Test {
protected:
    Movie movie;
    Movie movie2;
    Repository repo;
    void SetUp() override {
        movie = Movie("Inception", "SF", 2010, 300, "https://www.youtube.com/watch?v=YoHD9XEInc0");
        movie2 = Movie("Ted", "Comedy", 2012, 1000, "https://www.youtube.com/watch?v=9fbo_pQvU7M");
        repo = Repository();
    }
};

TEST_F(RepositoryTest, add_movie){
    repo.add_movie(movie);
    ASSERT_EQ(repo.get_size(), 1);
    repo.add_movie(movie2);
    ASSERT_EQ(repo.get_size(), 2);
}

TEST_F(RepositoryTest, add_movie_throw_exception){
    repo.add_movie(movie);
    try{
        repo.add_movie(movie);
    }
    catch(RepositoryException const& err){
        EXPECT_STREQ(err.what(), "Repository exception.");
    }
}

TEST_F(RepositoryTest, get_movies){

    Movie* movie1;
    repo.add_movie(movie);
    movie1 = repo.get_movies();
    ASSERT_EQ(movie1->get_number_of_likes(), movie.get_number_of_likes());
    ASSERT_EQ(movie1->get_title(), movie.get_title());
    ASSERT_EQ(movie1->get_genre(), movie.get_genre());
    ASSERT_EQ(movie1->get_trailer(), movie.get_trailer());
    ASSERT_EQ(movie1->get_year_of_release(), movie.get_year_of_release());
}

TEST_F(RepositoryTest, get_size){
    ASSERT_EQ(repo.get_size(), 0);
    repo.add_movie(movie);
    ASSERT_EQ(repo.get_size(), 1);
    repo.add_movie(movie2);
    ASSERT_EQ(repo.get_size(), 2);
}

TEST_F(RepositoryTest, get_movie_by_index){
    repo.add_movie(movie);
    repo.add_movie(movie2);
    Movie movie1 = repo.get_movie_by_index(0);
    ASSERT_EQ(movie1.get_number_of_likes(), movie.get_number_of_likes());
    ASSERT_EQ(movie1.get_title(), movie.get_title());
    ASSERT_EQ(movie1.get_genre(), movie.get_genre());
    ASSERT_EQ(movie1.get_trailer(), movie.get_trailer());
    ASSERT_EQ(movie1.get_year_of_release(), movie.get_year_of_release());
}

TEST_F(RepositoryTest, get_movie_by_index_raise_exception){
    repo.add_movie(movie);
    repo.add_movie(movie2);
    try{
        Movie movie1 = repo.get_movie_by_index(2);
    }
    catch(RepositoryException const& err){
        EXPECT_STREQ(err.what(), "Repository exception.");
    }
}

TEST_F(RepositoryTest, delete_movie){
    repo.add_movie(movie);
    repo.add_movie(movie2);
    ASSERT_EQ(repo.get_size(), 2);
    repo.delete_movie(movie.get_title());
    ASSERT_EQ(repo.get_size(), 1);
}

TEST_F(RepositoryTest, delete_movie_raise_exception){
    repo.add_movie(movie);
    repo.add_movie(movie2);
    try{
        repo.delete_movie("F9");
    }
    catch(RepositoryException const& err){
        EXPECT_STREQ(err.what(), "Repository exception.");
    }
}

TEST_F(RepositoryTest, update_movie_trailer){
    repo.add_movie(movie);
    repo.add_movie(movie2);
    ASSERT_EQ(repo.get_movie_by_index(0).get_trailer(), "https://www.youtube.com/watch?v=YoHD9XEInc0");
    repo.update_movie_trailer(movie.get_title(), "https://www.youtube.com/watch?v=naQr0uTrH_s");
    ASSERT_EQ(repo.get_movie_by_index(0).get_trailer(), "https://www.youtube.com/watch?v=naQr0uTrH_s");
}

TEST_F(RepositoryTest, update_movie_trailer_raise_exception){
    repo.add_movie(movie);
    repo.add_movie(movie2);
    try{
        repo.update_movie_trailer("Pirates of the Caribbean", "https://www.youtube.com/watch?v=naQr0uTrH_s");
    }
    catch(RepositoryException const& err){
        EXPECT_STREQ(err.what(), "Repository exception.");
    }
}

TEST_F(RepositoryTest, get_movie_index_genre_repo){
    repo.add_movie(movie);
    repo.add_movie(movie2);
    Movie movie3 = Movie("Matrix", "SF", 2003, 140, "https://www.youtube.com/watch?v=Y21412wdsf");
    repo.add_movie(movie3);
    ASSERT_EQ(repo.get_movie_index_genre_repo("SF", 1).get_trailer(), movie3.get_trailer());
    ASSERT_EQ(repo.get_movie_index_genre_repo("SF", 1).get_genre(), movie3.get_genre());
    ASSERT_EQ(repo.get_movie_index_genre_repo("SF", 1).get_title(), movie3.get_title());
    ASSERT_EQ(repo.get_movie_index_genre_repo("SF", 1).get_year_of_release(), movie3.get_year_of_release());
    ASSERT_EQ(repo.get_movie_index_genre_repo("SF", 1).get_number_of_likes(), movie3.get_number_of_likes());
}

TEST_F(RepositoryTest, get_movie_index_genre_repo_get_the_first_one){
    Movie movie3 = Movie("Matrix", "SF", 2003, 140, "https://www.youtube.com/watch?v=Y21412wdsf");
    repo.add_movie(movie3);
    repo.add_movie(movie);
    repo.add_movie(movie2);
    ASSERT_EQ(repo.get_movie_index_genre_repo("SF", 3).get_trailer(), movie3.get_trailer());
    ASSERT_EQ(repo.get_movie_index_genre_repo("SF", 3).get_genre(), movie3.get_genre());
    ASSERT_EQ(repo.get_movie_index_genre_repo("SF", 3).get_title(), movie3.get_title());
    ASSERT_EQ(repo.get_movie_index_genre_repo("SF", 3).get_year_of_release(), movie3.get_year_of_release());
    ASSERT_EQ(repo.get_movie_index_genre_repo("SF", 3).get_number_of_likes(), movie3.get_number_of_likes());
}

TEST_F(RepositoryTest, get_size_for_a_genre){
    Movie movie3 = Movie("Matrix", "SF", 2003, 140, "https://www.youtube.com/watch?v=Y21412wdsf");
    repo.add_movie(movie3);
    repo.add_movie(movie);
    repo.add_movie(movie2);
    ASSERT_EQ(repo.get_size_for_a_genre("SF"), 2);
}

TEST_F(RepositoryTest, increment_likes){
    repo.add_movie(movie);
    repo.add_movie(movie2);
    ASSERT_EQ(repo.get_movie_by_index(0).get_number_of_likes(), 300);
    repo.increment_likes("Inception");
    ASSERT_EQ(repo.get_movie_by_index(0).get_number_of_likes(), 301);
}

TEST_F(RepositoryTest, copy_constructor){
    repo.add_movie(movie);
    repo.add_movie(movie2);
    Repository repo2 = repo;
    ASSERT_EQ(repo.get_size(), 2);
    ASSERT_EQ(repo2.get_size(), 2);
}

///                                     WATCH LIST TEST                                             ///

class WatchListTest : public ::testing::Test {
protected:
    Movie movie;
    Movie movie2;
    WatchList watch_list;
    void SetUp() override {
        movie = Movie("Inception", "SF", 2010, 300, "https://www.youtube.com/watch?v=YoHD9XEInc0");
        movie2 = Movie("Ted", "Comedy", 2012, 1000, "https://www.youtube.com/watch?v=9fbo_pQvU7M");
        watch_list = WatchList();
    }
};

TEST_F(WatchListTest, add_movie){
    watch_list.add_movie(movie);
    ASSERT_EQ(watch_list.get_size_of_watch_list(), 1);
    watch_list.add_movie(movie2);
    ASSERT_EQ(watch_list.get_size_of_watch_list(), 2);
}

TEST_F(WatchListTest, get_size_of_watch_list){
    ASSERT_EQ(watch_list.get_size_of_watch_list(), 0);
    watch_list.add_movie(movie);
    ASSERT_EQ(watch_list.get_size_of_watch_list(), 1);
    watch_list.add_movie(movie2);
    ASSERT_EQ(watch_list.get_size_of_watch_list(), 2);
}

TEST_F(WatchListTest, get_movie_by_index_from_watch_list){
    watch_list.add_movie(movie);
    watch_list.add_movie(movie2);
    Movie movie3 = watch_list.get_movie_by_index_from_watch_list(1);
    ASSERT_EQ(movie3.get_number_of_likes(), movie2.get_number_of_likes());
    ASSERT_EQ(movie3.get_title(), movie2.get_title());
    ASSERT_EQ(movie3.get_trailer(), movie2.get_trailer());
    ASSERT_EQ(movie3.get_year_of_release(), movie2.get_year_of_release());
    ASSERT_EQ(movie3.get_genre(), movie2.get_genre());
}

TEST_F(WatchListTest, delete_movie_from_watch_list){
    watch_list.add_movie(movie);
    watch_list.add_movie(movie2);
    ASSERT_EQ(watch_list.get_size_of_watch_list(), 2);
    watch_list.delete_movie_from_watch_list("Inception");
    ASSERT_EQ(watch_list.get_size_of_watch_list(), 1);
}

TEST_F(WatchListTest, check_movie){
    watch_list.add_movie(movie);
    watch_list.add_movie(movie2);
    ASSERT_EQ(watch_list.check_movie("Inception"), true);
    ASSERT_EQ(watch_list.check_movie("Pirates of the Caribbean"), false);
}

///                                     CONTROLLER TEST                                             ///

class ControllerTest : public ::testing::Test {
protected:
    Movie movie;
    Movie movie2;
    WatchList watch_list;
    Repository repo;
    Controller control;
    void SetUp() override {
        movie = Movie("Inception", "SF", 2010, 300, "https://www.youtube.com/watch?v=YoHD9XEInc0");
        movie2 = Movie("Ted", "Comedy", 2012, 1000, "https://www.youtube.com/watch?v=9fbo_pQvU7M");
        watch_list = WatchList();
        repo = Repository();
        control = Controller(repo, watch_list);
    }
};

TEST_F(ControllerTest, add_movie_admin){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    ASSERT_EQ(control.get_size(), 1);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    ASSERT_EQ(control.get_size(), 2);
}



TEST_F(ControllerTest, add_movie_admin_INTEGER_ERROR){
    try{
        control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", -2010, -300);
    }
    catch(IntegerError const& err){
        EXPECT_STREQ(err.what(), "The year and the number of likes must be > 0.");
    }
}

TEST_F(ControllerTest, add_movie_admin_MOVIE_ALREADY_EXIST){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    try{
        control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    }
    catch(MovieAlreadyExists const& err){
        EXPECT_STREQ(err.what(), "Movie already exists.");
    }
}

TEST_F(ControllerTest, get_size){
    ASSERT_EQ(control.get_size(), 0);
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    ASSERT_EQ(control.get_size(), 1);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    ASSERT_EQ(control.get_size(), 2);
}

TEST_F(ControllerTest, get_movies){
    Movie* movie1;
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    movie1 = control.get_movies();
    ASSERT_EQ(movie1->get_number_of_likes(), 300);
    ASSERT_EQ(movie1->get_title(), "Inception");
    ASSERT_EQ(movie1->get_genre(), "SF");
    ASSERT_EQ(movie1->get_trailer(), "https://www.youtube.com/watch?v=YoHD9XEInc0");
    ASSERT_EQ(movie1->get_year_of_release(), 2010);
}

TEST_F(ControllerTest, get_movie_by_index){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    Movie movie1 = control.get_movie_by_index(0);
    ASSERT_EQ(movie1.get_number_of_likes(), 300);
    ASSERT_EQ(movie1.get_title(), "Inception");
    ASSERT_EQ(movie1.get_genre(), "SF");
    ASSERT_EQ(movie1.get_trailer(), "https://www.youtube.com/watch?v=YoHD9XEInc0");
    ASSERT_EQ(movie1.get_year_of_release(), 2010);
}

TEST_F(ControllerTest, get_movie_by_index_index_greater_than_size){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    try{
        control.get_movie_by_index(4);
    }
    catch(IndexGreaterThanSize const& err) {
        EXPECT_STREQ(err.what(), "The index that u gave is greater than the size of the array.");
    }
}

TEST_F(ControllerTest, remove_movie_admin){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    ASSERT_EQ(control.get_size(), 2);
    control.remove_movie_admin("Inception");
    ASSERT_EQ(control.get_size(), 1);
}

TEST_F(ControllerTest, remove_movie_admin_raise_exception){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    try{
        control.remove_movie_admin("Pirates of the Caribbean");
    }
    catch(MovieDoesntExist const& err){
        EXPECT_STREQ(err.what(), "Movie doesn't exist.");
    }
}

TEST_F(ControllerTest, update_movie_admin){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    ASSERT_EQ(control.get_movie_by_index(1).get_trailer(), "https://www.youtube.com/watch?v=9fbo_pQvU7M");
    control.update_movie_admin("Ted", "https://www.youtube.com/watch?v=9fbwfiodhafj");
    ASSERT_EQ(control.get_movie_by_index(1).get_trailer(), "https://www.youtube.com/watch?v=9fbwfiodhafj");
}



TEST_F(ControllerTest, update_movie_admin_movie_doesnt_exist){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    try{
        control.update_movie_admin("Pirates of the Caribbean", "https://www.youtube.com/watch?v=9fbwfiodhafj");
    }
    catch(MovieDoesntExist const& err){
        EXPECT_STREQ(err.what(), "Movie doesn't exist.");
    }
}

TEST_F(ControllerTest, get_movie_index_genre){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    Movie movie1 = control.get_movie_index_genre("SF", 0);
    ASSERT_EQ(movie1.get_number_of_likes(), 300);
    ASSERT_EQ(movie1.get_title(), "Inception");
    ASSERT_EQ(movie1.get_genre(), "SF");
    ASSERT_EQ(movie1.get_trailer(), "https://www.youtube.com/watch?v=YoHD9XEInc0");
    ASSERT_EQ(movie1.get_year_of_release(), 2010);
}

TEST_F(ControllerTest, get_size_for_a_genre){
    ASSERT_EQ(control.get_size_for_a_genre("Action"), 0);
    ASSERT_EQ(control.get_size_for_a_genre("SF"), 0);
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    ASSERT_EQ(control.get_size_for_a_genre("SF"), 1);
}

TEST_F(ControllerTest, add_movie_watch_list){
    movie = Movie("Inception", "SF", 2010, 300, "https://www.youtube.com/watch?v=YoHD9XEInc0");
    ASSERT_EQ(watch_list.get_size_of_watch_list(), 0);
    control.add_movie_watch_list(movie);
    ASSERT_EQ(control.get_size_watch_list(), 1);
}

TEST_F(ControllerTest, get_movie_watch_list_by_index){
    movie = Movie("Inception", "SF", 2010, 300, "https://www.youtube.com/watch?v=YoHD9XEInc0");
    control.add_movie_watch_list(movie);
    movie2 = Movie("Ted", "Comedy", 2012, 1000, "https://www.youtube.com/watch?v=9fbo_pQvU7M");
    control.add_movie_watch_list(movie2);
    Movie movie1 = control.get_movie_watch_list_by_index(0);
    ASSERT_EQ(movie1.get_number_of_likes(), 300);
    ASSERT_EQ(movie1.get_title(), "Inception");
    ASSERT_EQ(movie1.get_genre(), "SF");
    ASSERT_EQ(movie1.get_trailer(), "https://www.youtube.com/watch?v=YoHD9XEInc0");
    ASSERT_EQ(movie1.get_year_of_release(), 2010);
}

TEST_F(ControllerTest, increment_likes_for_a_movie){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    ASSERT_EQ(control.get_movie_by_index(0).get_number_of_likes(), 300);
    control.increment_likes_for_a_movie("Inception");
    ASSERT_EQ(control.get_movie_by_index(0).get_number_of_likes(), 301);
}

TEST_F(ControllerTest, delete_movie_from_watch_list){
    movie = Movie("Inception", "SF", 2010, 300, "https://www.youtube.com/watch?v=YoHD9XEInc0");
    control.add_movie_watch_list(movie);
    movie2 = Movie("Ted", "Comedy", 2012, 1000, "https://www.youtube.com/watch?v=9fbo_pQvU7M");
    control.add_movie_watch_list(movie2);
    ASSERT_EQ(control.get_size_watch_list(), 2);
    control.delete_movie_from_watch_list("Inception");
    ASSERT_EQ(control.get_size_watch_list(), 1);
}

TEST_F(ControllerTest, check_movie_in_watch_list){
    movie = Movie("Inception", "SF", 2010, 300, "https://www.youtube.com/watch?v=YoHD9XEInc0");
    control.add_movie_watch_list(movie);
    movie2 = Movie("Ted", "Comedy", 2012, 1000, "https://www.youtube.com/watch?v=9fbo_pQvU7M");
    control.add_movie_watch_list(movie2);
    ASSERT_EQ(control.check_movie_in_watch_list("Inception"), true);
    ASSERT_EQ(control.check_movie_in_watch_list("Pirates of the Caribbean"), false);
}

TEST_F(ControllerTest, copy_constructor){
    control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 300);
    control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    Controller control2 = control;
    ASSERT_EQ(control.get_size(), 2);
    ASSERT_EQ(control2.get_size(), 2);
}

int main(){

    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
*/