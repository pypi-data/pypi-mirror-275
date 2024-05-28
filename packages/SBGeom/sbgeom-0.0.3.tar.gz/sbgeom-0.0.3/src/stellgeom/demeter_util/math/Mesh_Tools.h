#pragma once
#include "Node.h"
#include <vector>
#include <array>

/**
 * @brief Struct for importing a tetrahedron domain from somewhere
 * 
 */
struct Tetrahedron_Vertices
{   public:
    /**
     * @brief Node vector containing all physical nodes
     * 
     */
    std::vector<std::unique_ptr<Node>> nodes;

    /**
     * @brief vector of arrays with four unsigned numbers connecting the Nodes
     * 
     */
    std::vector<std::array<unsigned,4>> vertices;
    private:
};

/**
 * @brief Struct for a triangular mesh
 * 
 * Only really used for meshing .stl files.
 * 
 */
struct Triangle_Vertices
{   public:
    /**
     * @brief Node vector containing all physical nodes
     * 
     */
    std::vector<std::unique_ptr<Node>> nodes;

    /**
     * @brief vector of arrays with four unsigned numbers connecting the Nodes
     * 
     */
    std::vector<std::array<unsigned,3>> vertices;
    private:
};
