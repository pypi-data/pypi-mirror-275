#include "Flux_Surfaces.h"

/**
 * @brief Derived class of Flux_Surfaces for a Fourier extension
 * 
 * This extension has the same Fourier coefficients as the base class but defined beyond \f$ s=1\f$. 
 * 
 * It uses internally a \f$d\f$ (distance from LCFS) vector. Distances between the defined \f$d\f$ manifolds are linearly interpolated.
 * 
 */
class Flux_Surfaces_Fourier_Extended : public Flux_Surfaces {
    using  json = nlohmann::json ;
    public:

    /**
     * @brief Construct a new Flux_Surfaces_Fourier_Extended object
     * 
     * Directly uses the provided data
     * 
     * @param Rmnc 
     * @param Zmns 
     * @param fs_settings 
     * @param d_extension 
     * @param Rmnc_extension 
     * @param Zmns_extension 
     */
    Flux_Surfaces_Fourier_Extended(const Array& Rmnc, const Array& Zmns, Flux_Surface_Settings fs_settings, const DynamicVector& d_extension, const Array& Rmnc_extension, const Array& Zmns_extension);
    Flux_Surfaces_Fourier_Extended(const Flux_Surfaces& flux_surfaces, const DynamicVector& d_extension, const Array& Rmnc_extension, const Array& Zmns_extension);

    /**
     * @brief Override of Flux_Surfaces::Return_Position
     * 
     * @param flux_surface_coordinates 
     * @return Vector 
     */
       Vector Return_Position(const Flux_Surface_Coordinates& flux_surface_coordinates) const override;

       
    private:
        bool     Check_Compatible() const;
        unsigned Find_Index_d(double d) const;
        Vector   Return_Extension_Position(unsigned index, double u, double v) const;
        Array         m_Rmnc_extension;
        Array         m_Zmns_extension;
        DynamicVector m_d_extension;
};

/**
 * @brief Derived class of Flux_Surfaces for a normal vector extension
 * 
 * See Lion, Jorrit, Felix Warmer, and Huaijin Wang. "A deterministic method for the fast evaluation and optimisation of the 3D neutron wall load for generic stellarator configurations." Nuclear Fusion 62.7 (2022): 076040.
 * 
 */
class Flux_Surfaces_Normal_Extended : public Flux_Surfaces { 
    public:
        
        /**
         * @brief Construct a new Flux_Surfaces_Normal_Extended object 
         * 
         * Does not need extra data
         * 
         * @param Rmnc 
         * @param Zmns 
         * @param fs_settings 
         */
        Flux_Surfaces_Normal_Extended(const Array& Rmnc, const Array& Zmns, Flux_Surface_Settings fs_settings) : Flux_Surfaces(Rmnc, Zmns, fs_settings) {};
        Flux_Surfaces_Normal_Extended(const Flux_Surfaces& flux_surfaces) : Flux_Surfaces(flux_surfaces){}
                

        /**
         * @brief Override of Flux_Surfaces::Return_Position
         * 
         * @param flux_surface_coordinates 
         * @return Vector 
         */
        Vector Return_Position(const Flux_Surface_Coordinates& flux_surface_coordinates) const override;
    private:

};