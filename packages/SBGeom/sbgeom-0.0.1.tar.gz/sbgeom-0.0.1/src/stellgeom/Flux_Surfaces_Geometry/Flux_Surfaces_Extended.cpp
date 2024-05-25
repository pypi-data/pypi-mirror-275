#include "Flux_Surfaces_Extended.h"


/*
Flux_Surfaces_Fourier_Extended::Flux_Surfaces_Fourier_Extended(Array&& Rmnc, Array&& Zmns, Flux_Surface_Settings fs_settings, hid_t flux_surface_hid) : Flux_Surfaces(std::move(Rmnc), std::move(Zmns), fs_settings){
    try{
        m_Rmnc_extension = HDF5_Load_Array(flux_surface_hid, "Rmnc_extension");
        m_Zmns_extension = HDF5_Load_Array(flux_surface_hid, "Zmns_extension");;
        m_d_extension    = HDF5_Load_Array(flux_surface_hid, "d_extension");
        if(! this->Check_Compatible()){
            throw std::runtime_error("Extension does not have the same size (same toroidal and poloidal harmonic numbers) as the base flux surface class..");
        }
    }
    catch(const std::exception& e){
        std::cout<< e.what()<<" in Flux_Surfaces_Fourier_Extended(Array&&, Array&&, Flux_Surface_Settings, hid_t). Aborting..."<<std::endl;
        abort();
    }
    
    
};
*/
Flux_Surfaces_Fourier_Extended::Flux_Surfaces_Fourier_Extended(const Array& Rmnc,const Array& Zmns, Flux_Surface_Settings fs_settings,\
                                                              const DynamicVector& d_extension, const Array& Rmnc_extension, const Array& Zmns_extension) : Flux_Surfaces(Rmnc, Zmns, fs_settings),\
                                                                                                                                                                                  m_Rmnc_extension(Rmnc_extension),\
                                                                                                                                                                                  m_Zmns_extension(Zmns_extension),\
                                                                                                                                                                                  m_d_extension(d_extension){
        if(! this->Check_Compatible()){
            throw std::runtime_error("Extension does not have the same size (same toroidal and poloidal harmonic numbers) as the base flux surface class..");
        }
                                                                                                                                                                                  
};
Flux_Surfaces_Fourier_Extended::Flux_Surfaces_Fourier_Extended(const Flux_Surfaces& flux_surfaces,\
                                                              const DynamicVector& d_extension, const Array& Rmnc_extension, const Array& Zmns_extension) : Flux_Surfaces(flux_surfaces),\
                                                                                                                                                                                  m_Rmnc_extension(Rmnc_extension),\
                                                                                                                                                                                  m_Zmns_extension(Zmns_extension),\
                                                                                                                                                                                  m_d_extension(d_extension){
        if(! this->Check_Compatible()){
            throw std::runtime_error("Extension does not have the same size (same toroidal and poloidal harmonic numbers) as the base flux surface class..");
        }
                                                                                                                                                                                  
};

/*/
Flux_Surfaces_Fourier_Extended::Flux_Surfaces_Fourier_Extended(std::string filename_VMEC_NC4, const json& json_extension) : Flux_Surfaces(filename_VMEC_NC4){
    
    try{
        auto extension_file_name = json_extension.at("Initialisation_Parameters").at("Filename_Extension").get<std::string>();
        auto file_id = H5Fopen(extension_file_name.c_str(), H5F_ACC_RDONLY, H5P_DEFAULT);
            if(file_id == H5I_INVALID_HID){throw std::invalid_argument(" File " + extension_file_name + " not found ");}
            m_Rmnc_extension = HDF5_Load_Array(file_id, "Rmnc_extension");
            m_Zmns_extension = HDF5_Load_Array(file_id, "Zmns_extension");
            m_d_extension    = HDF5_Load_Array(file_id, "d_extension")   ;
        auto status       = H5Fclose(file_id);
        if(! this->Check_Compatible()){
            throw std::runtime_error("Extension does not have the same size (same toroidal and poloidal harmonic numbers) as the base flux surface class..");
        }
    }
    catch(const std::exception& e){
        std::cout<< e.what()<< " in Flux_Surfaces_Fourier_Extended(std::string filename_VMEC_NC4, const json& json_extension)"<<std::endl;
        abort();
    }
};
Flux_Surfaces_Fourier_Extended::Flux_Surfaces_Fourier_Extended(std::string filename_VMEC_NC4, std::string filename_extension) : Flux_Surfaces(filename_VMEC_NC4){
    try{
        auto file_id = H5Fopen(filename_extension.c_str(), H5F_ACC_RDONLY, H5P_DEFAULT);
            if(file_id == H5I_INVALID_HID){throw std::invalid_argument(" File " + filename_extension + " not found ");}
            m_Rmnc_extension = HDF5_Load_Array(file_id, "Rmnc_extension");
            m_Zmns_extension = HDF5_Load_Array(file_id, "Zmns_extension");
            m_d_extension    = HDF5_Load_Array(file_id, "d_extension")   ;
        auto status       = H5Fclose(file_id);
    }
    catch(const std::exception& e){
        std::cout<< e.what()<< " in Flux_Surfaces_Fourier_Extended(std::string filename_VMEC_NC4, std::string filename_extension)"<<std::endl;
        abort();
    }
    
};
*/
unsigned Flux_Surfaces_Fourier_Extended::Find_Index_d(double d) const{
    unsigned result = 0;
    bool     found  = false;
    for(unsigned i = 0; i < m_d_extension.rows(); ++i){
        if(d < m_d_extension[i]){
            result = i;
            found  = true;
            break;
        }
    }
    if( ! found){throw std::invalid_argument(" Trying to calculate a position beyond the last surface in Flux_Surfaces_Fourier_Extend.");}
    return result;
}

bool    Flux_Surfaces_Fourier_Extended::Check_Compatible() const{
    return m_mpol_vector.size() == m_Rmnc_extension.cols();
};
Vector Flux_Surfaces_Fourier_Extended::Return_Extension_Position(unsigned index, double u, double v) const{
        
    double R_i = 0.0;
    double Z_i = 0.0;
    double phi = v;
    
    double x = 0.0;
    double y = 0.0;
    double z = 0.0;
        
    for(unsigned i = 0; i < m_Rmnc.cols(); ++i){
        double ntor_i = m_ntor_vector[i];
        double mpol_i = m_mpol_vector[i];
        R_i += m_Rmnc_extension(index,i) * cos(u * mpol_i - v * ntor_i); 
        Z_i += m_Zmns_extension(index,i) * sin(u * mpol_i - v * ntor_i); 
    }
    x = R_i * cos(v);
    y = R_i * sin(v);
    z = Z_i;

    return Vector(x,y,z);
}
Vector Flux_Surfaces_Fourier_Extended::Return_Position(const Flux_Surface_Coordinates& flux_surface_coordinates) const{
    Vector result(0.0,0.0,0.0);
    
    if(flux_surface_coordinates.Get_distance_LCFS() == 0.0){
        result = Flux_Surfaces::Return_Position(flux_surface_coordinates);
    }
    else{
        auto d = flux_surface_coordinates.Get_distance_LCFS();
        auto s = flux_surface_coordinates.Get_s(); // Will always be 1.0; Radial_Flux_Surface_Coordinate throws if d > 0.0 && s < 1.0
        
        auto d_max_index = this->Find_Index_d(d);
        auto result_start = Vector(0.0,0.0,0.0);
        auto result_end   = Vector(0.0,0.0,0.0);

        double d_start      = 0.0;
        
        if(d_max_index == 0){
            result_start = Flux_Surfaces::Return_Position({{1.0,0.0}, flux_surface_coordinates.u,flux_surface_coordinates.v});
            d_start      = 0.0;
        }
        else{
            result_start = this->Return_Extension_Position(d_max_index - 1, flux_surface_coordinates.u, flux_surface_coordinates.v);
            d_start      = m_d_extension(d_max_index - 1);
        }
        result_end       = this->Return_Extension_Position(d_max_index, flux_surface_coordinates.u, flux_surface_coordinates.v);
        
        double d_end            = m_d_extension(d_max_index);
        auto d_max_fraction = (d - d_start) / (d_end - d_start);
        auto d_min_fraction =  1.0 - d_max_fraction;
        result = result_start * d_min_fraction + result_end * d_max_fraction;
    }
    
    return result;
};

/*
void  Flux_Surfaces_Fourier_Extended::Save_HDF5(hid_t location_id) const{
    Flux_Surfaces::Save_HDF5(location_id);
    auto fs_id  = H5Gopen(location_id, "Flux_Surfaces", H5P_DEFAULT); 
        HDF5_Add_Unsigned_Attribute("Extension", fs_id, Flux_Surfaces_Fourier_Extended_type_H5); 
        HDF5_Store_Array(m_Rmnc_extension, fs_id, "Rmnc_extension");
        HDF5_Store_Array(m_Zmns_extension, fs_id, "Zmns_extension");
        HDF5_Store_Array(m_d_extension,    fs_id, "d_extension");
    auto status = H5Gclose(fs_id);
};
*/

Vector Flux_Surfaces_Normal_Extended::Return_Position(const Flux_Surface_Coordinates& flux_surface_coordinates) const{
    
    double s = flux_surface_coordinates.Get_s();
    double d = flux_surface_coordinates.Get_distance_LCFS();
    double u = flux_surface_coordinates.u;
    double v = flux_surface_coordinates.v;

    
    double R_i = 0.0;
    double Z_i = 0.0;
    double phi = v;
    
    double x = 0.0;
    double y = 0.0;
    double z = 0.0;
    
    unsigned s_index = this->Index_in_Matrix(s);
    
    for(unsigned i = 0; i < m_Rmnc.cols(); ++i){
        double ntor_i = m_ntor_vector[i];
        double mpol_i = m_mpol_vector[i];
        R_i += m_Rmnc(s_index,i) * cos(u * mpol_i - v * ntor_i); 
        Z_i += m_Zmns(s_index,i) * sin(u * mpol_i - v * ntor_i); 
    }
    x = R_i * cos(v);
    y = R_i * sin(v);
    z = Z_i;
    Vector result;
    if(fabs(d) > 0.0){
        auto normal = this->Return_Surface_Normal(Flux_Surface_Coordinates(Radial_Flux_Coordinate(1.0,0.0),u,v));
        result = Vector(x,y,z) + this->Return_Surface_Normal(Flux_Surface_Coordinates(Radial_Flux_Coordinate(1.0,0.0),u,v)) * d;
    }
    else{
        result = Vector(x,y,z);
    }
    return result;
 };
 


//void Flux_Surfaces_Normal_Extended::Save_HDF5(hid_t location_id) const {Flux_Surfaces::Save_HDF5(location_id) ; auto fs_id = H5Gopen(location_id, "Flux_Surfaces", H5P_DEFAULT); HDF5_Add_Unsigned_Attribute("Extension", fs_id, Flux_Surfaces_Normal_Extended_type_H5); auto status = H5Gclose(fs_id);};