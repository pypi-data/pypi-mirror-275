#pragma once 
#include <cmath>
#include <complex>
#include "Vector.h"
#include "Contiguous_Arrays.h"
/**
 * @brief Spherical harmonic function \f$Y_{lm}\f$
 *
 *  Uses the following definition:
 * \f[Y_{lm}(\theta, \phi) = \sqrt{\frac{(2l+1)(l-m)!}{(l+m)!}} P^m_l(\cos(\theta)) e^{i \phi m} \f]
 *  
 *  @param l 
 *  @param m 
 *  @param Omega_n
 *
 */
std::complex<double> Ylm(int l, int m, const Unit_Vector& Omega_n);

/**
 * @brief Struct for encapsulating a (l,m) pair for spherical harmonics
 * 
 */
struct lm{
    /**
     * @brief Construct a new lm object
     * 
     * @param l_in 
     * @param m_in 
     */
    lm(int l_in, int m_in) : l(l_in), m(m_in){}

    /**
     * @brief \f$l\f$
     * 
     */
    int l;
    
    /**
     * @brief \f$m\f$
     * 
     */
    int m;

    /**
     * @brief Comparison operator
     * 
     * @param lm_other 
     * @return true 
     * @return false 
     */
    bool operator==(lm lm_other)const{return lm_other.l == l && lm_other.m == m;}
};

/**
 * @brief Templated class to iterate over all (l,m) pairs for a given maximum order
 * 
 * 
 * Use simply as \code{.cpp} for(auto lm : lm_iterator<L>()){...} \endcode
 * 
 * @tparam L 
 */
template<unsigned L>
class lm_iterator{
    public:
        class iterator : public std::iterator<std::input_iterator_tag, lm, lm,const lm*, lm>{
            int m_l_order = 0;
            lm current_lm = lm(0,0);
            public:
            explicit iterator(int legendre_order, lm lm_in = lm(0,0)) : current_lm(lm_in), m_l_order(legendre_order) {}
            iterator& operator++() { 
                if(current_lm.m == current_lm.l){ 
                    current_lm.l += 1;
                    current_lm.m = - current_lm.l;
                }
                else{
                    current_lm.m += 1;                   
                }
                return *this;
            }
            iterator operator++(int) { iterator retval = *this; ++(*this); return retval;}
            bool operator==(iterator other) const { return current_lm == other.current_lm;}
            bool operator!=(iterator other) const { return !(*this == other);}
            reference operator*() const{ return current_lm;}
    };
    lm_iterator(){}
    iterator begin(){return iterator(L, lm(0,0));}
    iterator end()  {return iterator(L, lm(L + 1 , - (L+1)));}
};

/**
 * @brief Templated class to store a complete collection data of all pairs (l,m)
 * 
 * @tparam T datatype to store
 * @tparam L maximum legendre order
 */
template<class T, unsigned L>
class x_lm_collection{
    public:
        /**
         * @brief Construct a new x lm collection object
         * 
         * Template L determines underlying array size
         * 
         */
        x_lm_collection() : m_data((1+ L)  * (1 + L)){m_data.setZero();}
        /**
         * @brief Setter of data at (l,m)
         * 
         * @param l 
         * @param m 
         * @return T& 
         */
        T& Set_lm(int l, int m )       {return m_data(this->Index(l,m));}
        T& Set_lm(lm lm_in )       {return m_data(this->Index(lm_in.l,lm_in.m));}

        /**
         * @brief Getter of data at (l,m)
         * 
         * @param l 
         * @param m 
         * @return T& 
         */
        T Get_lm(int l, int m ) const {return m_data(this->Index(l,m));}
        T Get_lm(lm lm_in ) const {return m_data(this->Index(lm_in.l,lm_in.m));}

        /**
         * @brief Write out complete dataset
         * 
         */
        void Write() const{
            for(auto lm_i : lm_iterator<L>()){
                std::cout<<lm_i.l<<","<<lm_i.m<<","<<this->Get_lm(lm_i.l,lm_i.m)<<std::endl;
            }
        }
    private:
        Eigen::Array<T,Eigen::Dynamic, 1> m_data;
        unsigned Index(int l, int m) const{
           sb_assert(l <= L && m >= -l && m <= l);
            return unsigned(l * l  + l + m );
        };
        
};

/**
 * @brief Templated class to store a complete collection data of all indices (i,l,m) 
 * 
 * i represents an external index (e.g. list of nodes)
 * 
 * 
 * 
 * @tparam T datatype
 * @tparam L maximum legendre order
 */
template<class T, unsigned L>
class x_i_lm_collection{
    public:

        /**
         * @brief Construct a new x i lm collection object
         * 
         * @param i_number number of external indices
         */
        x_i_lm_collection(unsigned i_number) : m_data((1+ L)  * (1 + L) * i_number), m_i_number(int(i_number)){ m_data.setZero();};

        /**
         * @brief Setter of data at (i,l,m)
         * 
         * @param i 
         * @param l 
         * @param m 
         * @return T& 
         */
        T& Set_ilm(int i, int l, int m )       {return m_data(this->Index(i,l,m));}
        T& Set_ilm(int i, lm lm_in)            {return m_data(this->Index(i,lm_in.l,lm_in.m));}

        void Set_ilm(const x_lm_collection<T,L>& x_lm_in, int i){
            for(auto lm_i : lm_iterator<L>()){
                this->Set_ilm(i,lm_i) = x_lm_in.Get_lm(lm_i);
            }
        }

        /**
         * @brief Getter of data at (i,l,m)
         * 
         * @param i 
         * @param l 
         * @param m 
         * @return T 
         */
        T  Get_ilm(int i, int l, int m ) const {return m_data(this->Index(i,l,m));}
        T  Get_ilm(int i, lm lm_in)      const {return m_data(this->Index(i,lm_in.l, lm_in.m));}

        /**
         * @brief Gets maximum number of external indices
         * 
         * @return unsigned 
         */
        unsigned Get_Number_Values() const{return m_i_number;}
        
        
        /**
         * @brief Function for obtaining a 3d matrix of all the data (real part)
         * The 3D matrix is a bit weird: the m index is just shifted towards the first index:
         * i.e. for a l=2 matrix we have (l,m) (at fixed node i)
         * [(0,  0),     0.0,     0.0,     0.0,     0.0]
         * [(1, -1), (1,  0), (1,  1),     0.0,     0.0]
         * [(2, -2), (2, -1), (2,  0), (2,  1), (2,  2)]
         * @return std::unique_ptr<Contiguous3D<T>> 
         */
        std::unique_ptr<Contiguous3D<T>> Obtain_3D_Matrix(){
            auto result = std::make_unique<Contiguous3D<T>>(m_i_number, L + 1, 2* L  + 1);
            for(int i  = 0; i < m_i_number; ++i){
                for(int l = 0; l<= L; ++l){
                    for(int m = -l; m <= l; ++m){
                        (*result)(i,l, m +l) = this->Get_ilm(i, l, m);
                    }
                }
            }
            return result;
        }

        Eigen::Matrix<T, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor> Return_2D_Matrix() const{
            auto result = Eigen::Matrix<T, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>(m_i_number, ( L + 1 ) *(L + 1));
            for(int i =0; i < m_i_number; ++i){
                for(auto lm_i : lm_iterator<L>()){
                    result(i, lm_i.l * lm_i.l  + lm_i.l + lm_i.m) = this->Get_ilm(i, lm_i);
                }
            }
            return result;
        }

        void Set_Zero(){m_data.setZero();}

    private:
        Eigen::Array<T,Eigen::Dynamic, 1> m_data;
        // For locality, computing types of Psi_lmg it sums over i and thus that should be the fastest changing index ? this is not the case?
        unsigned Index(int i, int l, int m) const{
           sb_assert(i < m_i_number && l <= L && m >= -l && m <= l);
            return unsigned( i * (L+1) * (L+1) + (l * l  + l + m));
        };
        
        int m_i_number;
};
