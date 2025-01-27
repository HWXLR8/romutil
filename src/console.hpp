#pragma once

#include <mutex>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Console {
public:
    Console(const std::string& name);
    void find_roms();
    void parse_dat(std::string cat, std::unordered_map<std::string, std::string>& rom_crc);
    void process_roms();
    void check_rom(const std::string& rom, const std::string& cat);
    void print_results();
    void print_missing();

private:
    std::string name_;
    std::string dat_file_;
    std::vector<std::string> romdirs_;
    std::vector<std::string> roms_;
    std::vector<std::string> cats_;
    // str(cat) -> [str(rom_crc) -> str(rom_name)]
    std::unordered_map<std::string, std::unordered_map<std::string, std::string>> dats_;
    std::unordered_map<std::string, int> dat_sizes_;
    // str(cat) -> [str(rom_crc)]
    std::unordered_map<std::string, std::unordered_set<std::string>> romsets_;
    std::unordered_set<std::string> missing_;

    std::mutex dats_mtx_;
    std::mutex romsets_mtx_;
};
