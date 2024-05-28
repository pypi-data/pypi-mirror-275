#pragma once
#include "Node.h"
#include "Vector.h"
#include <vector>
#include <array>
#include <fstream>
#include <iostream>
#include "Mesh_Tools.h"


/**
 * @brief Function for generating a Tetrahedron_Vertices object from files
 * 
 * @param filename_nodes 
 * @param filename_vertices 
 * @return Tetrahedron_Vertices 
 */
Tetrahedron_Vertices Tetrahedrons_From_File(std::string filename_nodes, std::string filename_vertices);


std::vector<Vector> Location_Linspace(const Vector& start,const Vector& end, unsigned samples);


std::string Triangle_To_STL(Vector v1, Vector v2, Vector v3);

void Append_To_STL(const Triangle_Vertices& triangle_vertices ,std::ofstream& ofstream, bool orientation_switch = false);