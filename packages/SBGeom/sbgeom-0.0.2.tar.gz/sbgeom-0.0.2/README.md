## SBGeom

A simple package for creating blanket geometries derived from Fourier Surfaces.


### Dependencies

The build process uses [scikit-build-core](https://github.com/scikit-build/scikit-build-core) for building.

Internally, it uses the [JAX](https://github.com/google/jax) library. scikit-build-core automatically installs this dependency, however, a GPU-accelerated version
can significantly improve performance. This requires an NVIDIA GPU and can be installed using:

```
pip install -U "jax[cuda12_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
```

If this is however not available, the CPU version will be automatically installed during the build process.

### Installation


##### Linux

Wheels are provided on pypi and thus the package can be installed from pypi using:

```
pip install sbgeom
```

It can also be installed from the source if CMake and a c++17 compatible comiler are present on the system by cloning the repository, and inside the repository run

```
pip install . 
```

##### Windows

Only a source distribution is provided on pypi and thus the package can be installed from pypi only if CMake and a c++17 compatible compiler are present.

```
pip install sbgeom
```

### Examples

The paraview state file example.pvsm can be used to view the results of the example (be sure to use the option "Search Files under specified directory" to find the local files). It should look somewhat like this 

<img src="example_data/paraview_example.png" alt="drawing" width="400"/>


where you can see the different capabilities (generating LCFS, generating blanket geometry, generating fourier fitted blanket geometry, generating tetrahedral mesh, generating finite size coils 
and generating finite sized upsampled coils)

### Input data 

For flux surfaces, it's just a VMEC file, but convert to an NC4 (i.e., and HDF5) file by using:

```
nccopy -k 4 vmec_file.nc vmec_file.nc4
```

For coils, it just uses an H5 with 1 dataset ("Dataset1") which contains a 3D array (coil number, points per coil, cartesian coordinates) of the coil points. See the example data (also a Fourier Coil HDF5 is provided there for convience.)


### Subtree commands 

For pushing and pulling the subtree packages.

```
git remote add subtree_stellgeom git@gitlab.tue.nl:s1668021/stellgeom.git
git remote add subtree_eigen https://gitlab.com/libeigen/eigen.git

git subtree add  --prefix=src/eigen/ subtree_eigen master
git subtree add  --prefix=src/stellgeom/ subtree_stellgeom main
git subtree pull --prefix=src/stellgeom/ subtree_stellgeom main
git subtree push --prefix=src/stellgeom/ subtree_stellgeom main
```

Eigen is a subtree because although it can be compiled with a local Eigen installation, this allows for an easier installation process (e.g. in a cibuildwheel manylinux environment)