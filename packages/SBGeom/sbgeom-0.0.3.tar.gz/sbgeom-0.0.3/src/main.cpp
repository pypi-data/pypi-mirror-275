#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "Flux_Surfaces.h"
#include "Flux_Surfaces_Extended.h"
#include "pybind11/eigen.h"
#include "Coils.h"
#include <string>
namespace py = pybind11;

template<unsigned N>
UnsignedArray vec_to_uarray(const std::vector<std::array<unsigned, N>>& vec_in){
    auto result = UnsignedArray(vec_in.size(), N);
    for(unsigned i = 0; i < vec_in.size(); ++i){
        for(unsigned j=0; j < N; ++j){
            result(i,j) = vec_in[i][j];
        }        
    }
    return result;
}

Array Nodes_to_array(const std::vector<std::unique_ptr<Node>>& v_in){
    auto result = Array(v_in.size(), 3);
    for(unsigned i = 0; i < v_in.size(); ++i){
        for(unsigned j = 0; j < 3; ++j){
            result(i,j) = v_in[i]->m_location[j];
        }
    }
    return result;
}



struct Mesh{
    Mesh(const Triangle_Vertices& t_v_in) : positions(Nodes_to_array(t_v_in.nodes)), vertices(vec_to_uarray<3>(t_v_in.vertices)) {}
    Mesh(const Tetrahedron_Vertices& t_v_in) : positions(Nodes_to_array(t_v_in.nodes)), vertices(vec_to_uarray<4>(t_v_in.vertices)) {}
    Array positions;
    UnsignedArray vertices;
};

Mesh Mesh_From_Triangle_Vertices_Vector(const std::vector<Triangle_Vertices>& tvec_in){
    auto result = Triangle_Vertices();
    unsigned offset = 0;
    for(auto& tv  : tvec_in){
        for(auto& pos : tv.nodes){
            result.nodes.push_back(pos->Make_Unique());
        }
        for(auto& vert : tv.vertices){
            result.vertices.push_back({vert[0] + offset, vert[1] + offset, vert[2] + offset});
        }
        offset += tv.nodes.size();
    }
    return Mesh(result);
}
Mesh Mesh_Tiled_Surface(const Flux_Surfaces& self, double s, double d, unsigned N_tiles_v, unsigned N_tiles_u, double tile_spacing, double tor_min, double tor_max){
    auto tor_extent = Toroidal_Extent(tor_min, tor_max);
    auto edge_points = self.Return_UV_Manifold({s,d},N_tiles_u, N_tiles_v, {tor_min, tor_max});
    unsigned no_u_tiles = N_tiles_u;
    unsigned no_v_tiles = tor_extent.Full_Angle() ? N_tiles_v : N_tiles_v - 1;

    auto result_mesh = Triangle_Vertices();
    
    for(unsigned v_i = 0; v_i < no_v_tiles; ++v_i){
        for(unsigned u_i = 0; u_i < no_u_tiles; ++u_i){
            
            auto line_u0_v0 = edge_points.Real_Coordinate_From_Index(u_i,v_i);
            auto line_u1_v0 = edge_points.Real_Coordinate_From_Index( (u_i + 1) % no_u_tiles, v_i);
            auto line_u0_v1 = edge_points.Real_Coordinate_From_Index( u_i , (v_i + 1 ) % N_tiles_v);
            auto line_u1_v1 = edge_points.Real_Coordinate_From_Index( (u_i + 1) % no_u_tiles, (v_i + 1 ) % N_tiles_v);
            auto centre_point = (line_u0_v0 + line_u0_v1 + line_u1_v0 + line_u1_v1) / 4.0;            

            auto l00 = centre_point + tile_spacing * (line_u0_v0 - centre_point);
            auto l01 = centre_point + tile_spacing * (line_u0_v1 - centre_point);
            auto l10 = centre_point + tile_spacing * (line_u1_v0 - centre_point);
            auto l11 = centre_point + tile_spacing * (line_u1_v1 - centre_point);

            result_mesh.nodes.push_back(std::make_unique<Node>(l00));
            result_mesh.nodes.push_back(std::make_unique<Node>(l01));
            result_mesh.nodes.push_back(std::make_unique<Node>(l10));
            result_mesh.nodes.push_back(std::make_unique<Node>(l11));
            
            unsigned start_index = 4 * (v_i * no_u_tiles  + u_i);
            
            result_mesh.vertices.push_back({start_index, start_index + 1, start_index + 2});            
            result_mesh.vertices.push_back({start_index + 2, start_index + 1, start_index + 3});
        }
    }
    return Mesh(result_mesh);
}

std::unique_ptr<Coil_Set> Create_Coil_Set_From_List(py::list& coil_list){
    std::vector<std::shared_ptr<Coil>> coil_vec;
    for(auto it = coil_list.begin(); it != coil_list.end(); ++it){
        coil_vec.push_back(it->cast<std::shared_ptr<Coil>>());
    }   
    return std::make_unique<Coil_Set>(coil_vec);
}; 

std::unique_ptr<UV_Manifold> Create_Manifold_From_Data(const Array& points, const DynamicVector& u, const DynamicVector& v, double s, double d, double tor_min, double tor_max, unsigned N_u, unsigned N_v){
    auto data=  Contiguous3D<double>(N_u, N_v,3);
    for(unsigned i = 0; i < N_u; ++i){
        for(unsigned j = 0; j < N_v; ++j){
            for(unsigned k = 0; k < 3; ++k){
                data(i,j,k) = points(j * N_u + i, k);
            }
        }
    }
    return std::make_unique<UV_Manifold>(std::move(data), Radial_Flux_Coordinate(s,d), Toroidal_Extent(tor_min, tor_max));
}


PYBIND11_MODULE(SBGeom_cpp, m) {

    py::class_<Flux_Surface_Settings>(m, "Flux_Surface_Settings")
        .def(py::init<unsigned, unsigned, unsigned,unsigned>())
        .def_readonly("n_tor", &Flux_Surface_Settings::n_tor)
        .def_readonly("m_pol", &Flux_Surface_Settings::m_pol)
        .def_readonly("number_of_surfaces", &Flux_Surface_Settings::number_of_surfaces)
        .def_readonly("symmetry", &Flux_Surface_Settings::symmetry);

    py::class_<Mesh>(m, "Mesh")
        .def_readwrite("positions", &Mesh::positions)
        .def_readwrite("vertices", &Mesh::vertices);

    py::class_<Flux_Surfaces>(m, "Flux_Surfaces")
        .def(py::init<const Array&, const Array&, Flux_Surface_Settings>())
        .def_property_readonly("Rmnc", &Flux_Surfaces::Get_Rmnc)
        .def_property_readonly("Zmns", &Flux_Surfaces::Get_Zmns)
        .def_property_readonly("m_pol_vec", &Flux_Surfaces::Get_m_mpol_vector) 
        .def_property_readonly("n_tor_vec", &Flux_Surfaces::Get_n_ntor_vector) 
        .def_property_readonly("flux_surface_settings", &Flux_Surfaces::Get_Flux_Surface_Settings)
        .def("Return_Axis_Position", &Flux_Surfaces::Return_Axis_Position)
        .def("Return_Position", [](const Flux_Surfaces& self,  DynamicVector& s, DynamicVector& d, DynamicVector& u, DynamicVector& v){
            Array values(s.rows(),3); 
            for(unsigned i=0; i < s.rows(); ++i){
                values.row(i)  = self.Return_Position({{s[i], d[i]}, u[i],v[i]});
            }
            return values;
            })
        .def("Mesh_Surface", [](const Flux_Surfaces& self, double s, double d, unsigned Nv, unsigned Nu, double tor_min, double tor_max){
            return Mesh(self.Return_UV_Manifold({s,d},Nu,Nv,{tor_min, tor_max}).Mesh_Surface());
        })
        .def("Mesh_Tetrahedrons", [](const Flux_Surfaces& self, DynamicVector s_arr, DynamicVector d_arr, unsigned Nv, unsigned Nu, double tor_min, double tor_max){
            return Mesh(Mesh_Tetrahedron_Flux_Surfaces(self, s_arr, d_arr, Nv, Nu, {tor_min, tor_max}));
        })  
        .def("Mesh_Surfaces_Closed", [](const Flux_Surfaces& self, double s_1, double s_2, double d_1, double d_2, unsigned Nv, unsigned Nu, double tor_min, double tor_max){
            return Mesh(Mesh_Closed_Flux_Surface(self, {Radial_Flux_Coordinate(s_1, d_1), Radial_Flux_Coordinate(s_2, d_2)}, Nu, Nv, {tor_min, tor_max}));
        })
        .def("Mesh_Tiled_Surface", [](const Flux_Surfaces& self, double s, double d, unsigned N_tiles_v, unsigned N_tiles_u, double tile_spacing, double tor_min, double tor_max){
            return Mesh_Tiled_Surface(self,s,d, N_tiles_v, N_tiles_u, tile_spacing, tor_min, tor_max);
        });

    py::class_<UV_Manifold>(m, "UV_Manifold")
        .def(py::init(&Create_Manifold_From_Data))
        .def("Mesh_Surface", [](const UV_Manifold& self){
            return Mesh(self.Mesh_Surface());
        });

    py::class_<Flux_Surfaces_Normal_Extended, Flux_Surfaces>(m, "Flux_Surfaces_Normal_Extended")
        .def(py::init<const Array&, const Array&, Flux_Surface_Settings>())
        .def(py::init<const Flux_Surfaces&>());

    py::class_<Flux_Surfaces_Fourier_Extended, Flux_Surfaces>(m, "Flux_Surfaces_Fourier_Extended")
        .def(py::init<const Array&, const Array&, Flux_Surface_Settings, const DynamicVector&, const Array&, const Array& >())
        .def(py::init<const Flux_Surfaces& , const DynamicVector&, const Array&, const Array& >());

    py::class_<Coil, std::shared_ptr<Coil>>(m,"Coil")
	    .def("Scale_Points",&Coil::Scale_Points)
        .def_property("Centre", &Coil::Get_Centre, &Coil::Set_Centre)
        .def("Mesh_Triangles", [](const Coil& self, double width_phi, double width_R, unsigned number_of_vertices, std::string type, DynamicVector rot){
            if(type == "Centroid"){
                return Mesh(self.Mesh_Triangles_Centroid(width_phi, width_R,number_of_vertices));
            }
            else if(type == "RMF"){
                return Mesh(self.Mesh_Triangles_RMF(width_phi, width_R,number_of_vertices));
            }
            else if(type == "Frenet"){
                return Mesh(self.Mesh_Triangles_Frenet(width_phi, width_R,number_of_vertices));
            }
            else if(type == "Rotated_From_Centroid"){
                return Mesh(self.Mesh_Triangles_Rotated_From_Centroid(width_phi, width_R,number_of_vertices, rot));
            }
            else{
                throw std::invalid_argument("Type " + type + " not recognized.");
            }
        } , py::arg("self"), py::arg("width_phi"), py::arg("width_R"), py::arg("number_of_vertices"), py::arg("rot") = DynamicVector(1).setZero())
        .def("Position", [](const Coil& self, double arclength){return self.Position(arclength);})
        .def("Position",[](const Coil& self, DynamicVector arclength){
            auto result = VectorArray(arclength.rows(), 3);
            for(unsigned i =0; i < arclength.rows(); ++i){
                result.row(i) = self.Position(arclength[i]);
            }
            return result;
        })
        .def("Tangent", [](const Coil& self, double arclength){return self.Tangent(arclength);})
        .def("Tangent",[](const Coil& self, DynamicVector arclength){
            auto result = VectorArray(arclength.rows(), 3);
            for(unsigned i =0; i < arclength.rows(); ++i){
                result.row(i) = self.Tangent(arclength[i]);
            }
            return result;
        })
        .def("Finite_Size_Lines", [](const Coil& self, double width_phi, double width_R, unsigned no_of_points, std::string type, DynamicVector rot){
            if(type == "Centroid"){
                return self.Finite_Size_Lines_Centroid(no_of_points, width_phi, width_R);
            }
            else if(type == "RMF"){
                return self.Finite_Size_Lines_RMF(no_of_points, width_phi, width_R);
            }      
            else if(type == "Frenet"){
                return self.Finite_Size_Lines_Frenet(no_of_points, width_phi, width_R);
            }
            else if(type == "Rotated_From_Centroid"){
                return self.Finite_Size_Lines_Rotated_From_Centroid(no_of_points, width_phi, width_R, rot );
            }
            else{
                throw std::invalid_argument("Type " + type + " not recognized.");
            }
        }, py::arg("width_phi"), py::arg("width_R"), py::arg("number_of_vertices"), py::arg("type"), py::arg("rot") = DynamicVector(1).setZero())
        .def("Return_Sampling_Curve",[](const Coil& self){return self.Return_Sampling_Curve();});
    py::class_<Discrete_Coil, Coil, std::shared_ptr<Discrete_Coil>>(m,"Discrete_Coil")
        .def(py::init<VectorArray>())
        .def_property("Vertices", &Discrete_Coil::Return_Sampling_Curve, &Discrete_Coil::Set_Vertices);
    py::class_<Fourier_Coil, Coil, std::shared_ptr<Fourier_Coil>>(m,"Fourier_Coil")
        .def(py::init<VectorArray,VectorArray,Vector>())
        .def_property("Fourier_Cos", &Fourier_Coil::Get_Fourier_Cos, &Fourier_Coil::Set_Fourier_Cos)
        .def_property("Fourier_Sin", &Fourier_Coil::Get_Fourier_Sin, &Fourier_Coil::Set_Fourier_Sin);
    
//    py::class_<Harmonic_RMF_Fourier_Coil, Fourier_Coil, std::shared_ptr<Harmonic_RMF_Fourier_Coil>>(m,"Harmonic_RMF_Fourier_Coil")
//        .def(py::init<VectorArray, VectorArray, Vector, VectorArray, VectorArray, Vector>());

    py::class_<Coil_Set>(m, "Coil_Set")
        .def(py::init(&Create_Coil_Set_From_List))        
        .def("Truncate_to_Angles", [](Coil_Set& self, double tor_min, double tor_max){self.Truncate_To_Angles({tor_min, tor_max});})
	    .def("Scale_Points",&Coil_Set::Scale_Points,"Scale points") 
        .def("Mesh_Triangles", [](const Coil_Set& self, double width_phi, double width_R, unsigned number_of_vertices, std::string type, DynamicVector rot){
            std::vector<Triangle_Vertices> result;
            for(auto& coil : self.m_coils){
                if(type == "Centroid"){
                    result.push_back(coil->Mesh_Triangles_Centroid(width_phi, width_R,number_of_vertices));
                }
                else if(type == "RMF"){
                    result.push_back(coil->Mesh_Triangles_RMF(width_phi, width_R,number_of_vertices));
                }
                else if(type == "Frenet"){
                    result.push_back(coil->Mesh_Triangles_Frenet(width_phi, width_R,number_of_vertices));
                }
                else if(type == "Rotated_From_Centroid"){
                    result.push_back(coil->Mesh_Triangles_Rotated_From_Centroid(width_phi, width_R,number_of_vertices,rot));
                }
                else{
                    throw std::invalid_argument("Type " + type + " not recognized.");
                }                
            }
            return Mesh_From_Triangle_Vertices_Vector(result);
        }, py::arg("self"), py::arg("width_phi"), py::arg("width_R"), py::arg("number_of_vertices"), py::arg("rot") = DynamicVector(1).setZero())        
        .def("Number_of_Coils", [](const Coil_Set& self){return self.m_coils.size();})
        .def("Return_Coil", [](const Coil_Set& self, unsigned index){
            if(index >= self.m_coils.size()){
                throw std::invalid_argument("Index " + std::to_string(index) + " greater than number of coils (" + std::to_string(self.m_coils.size())+")");
            }
            return self.m_coils[index];
        });
    m.def("Compute_RMF", &Compute_RMF);
    m.def("Compute_Rotation_Between_Finite_Builds", &Compute_Rotation_Finite_Sizes);
}

