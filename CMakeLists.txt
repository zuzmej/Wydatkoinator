cmake_minimum_required(VERSION 3.10)

project(Wydatkoinator)

# Znajdź wszystkie pliki .ui w katalogu ui
file(GLOB UI_FILES ui/*.ui)

foreach(UI_FILE ${UI_FILES})
    # Pobierz nazwę pliku bez rozszerzenia
    get_filename_component(FILE_NAME ${UI_FILE} NAME_WE)
    
    # Określ ścieżkę docelową dla wygenerowanego pliku .py
    set(OUTPUT_PY_FILE "${CMAKE_SOURCE_DIR}/src/ui/${FILE_NAME}.py")
    
    # Dodaj polecenie do generowania plików .py z plików .ui za pomocą pyuic
    add_custom_command(
        OUTPUT ${OUTPUT_PY_FILE}
        COMMAND pyuic5 -o ${OUTPUT_PY_FILE} ${UI_FILE}
        MAIN_DEPENDENCY ${UI_FILE}
        COMMENT "Generating ${OUTPUT_PY_FILE} from ${UI_FILE}"
    )
    
    # Dodaj plik wyjściowy do listy źródeł, aby został uwzględniony w całkowitej konfiguracji
    list(APPEND GENERATED_PY_FILES ${OUTPUT_PY_FILE})
endforeach()

# Dodaj niestandardowy cel dla wygenerowanych plików
add_custom_target(UiFiles ALL DEPENDS ${GENERATED_PY_FILES})
