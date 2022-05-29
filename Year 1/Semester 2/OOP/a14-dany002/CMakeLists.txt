cmake_minimum_required(VERSION 3.21)
project(a14_dany002)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_PREFIX_PATH "C:/Qt/6.3.0/mingw_64")

find_package(Qt6 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(a14_dany002
        src/Controller.cpp
        src/Controller.h
        src/CsvFiles.cpp
        src/CsvFiles.h
        src/Exceptions.cpp
        src/Exceptions.h
        src/HtmlFile.cpp
        src/HtmlFile.h
        src/main.cpp
        src/Movie.cpp
        src/Movie.h
        src/Repository.cpp
        src/Repository.h
        src/TextFiles.cpp
        src/TextFiles.h
        src/UI.cpp
        src/UI.h
        src/WatchList.cpp
        src/WatchList.h
        src/WatchListGUI.cpp
        src/WatchListGUI.h
        src/WatchListGUI.ui src/admin_or_user.cpp src/admin_or_user.h src/admin_or_user.ui src/usergui.cpp src/usergui.h src/usergui.ui src/Undo.cpp src/Undo.h)
target_link_libraries(a14_dany002
        Qt::Core
        Qt::Gui
        Qt::Widgets
        )

if (WIN32)
    set(QT_INSTALL_PATH "${CMAKE_PREFIX_PATH}")
    if (NOT EXISTS "${QT_INSTALL_PATH}/bin")
        set(QT_INSTALL_PATH "${QT_INSTALL_PATH}/..")
        if (NOT EXISTS "${QT_INSTALL_PATH}/bin")
            set(QT_INSTALL_PATH "${QT_INSTALL_PATH}/..")
        endif ()
    endif ()
    if (EXISTS "${QT_INSTALL_PATH}/plugins/platforms/qwindows${DEBUG_SUFFIX}.dll")
        add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E make_directory
                "$<TARGET_FILE_DIR:${PROJECT_NAME}>/plugins/platforms/")
        add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy
                "${QT_INSTALL_PATH}/plugins/platforms/qwindows${DEBUG_SUFFIX}.dll"
                "$<TARGET_FILE_DIR:${PROJECT_NAME}>/plugins/platforms/")
    endif ()
    foreach (QT_LIB Core Gui Widgets)
        add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy
                "${QT_INSTALL_PATH}/bin/Qt6${QT_LIB}${DEBUG_SUFFIX}.dll"
                "$<TARGET_FILE_DIR:${PROJECT_NAME}>")
    endforeach (QT_LIB)
endif ()



