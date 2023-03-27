from setuptools import setup, Extension
from torch.utils import cpp_extension

# setup(name='sparse_coo_tensor_cpp',
#       ext_modules=[cpp_extension.CppExtension('sparse_coo_tensor_cpp', ['sparse_coo_tensor.cpp'],
#                                               extra_compile_args=["-lcusparse"],
#                                               library_dirs=["/apps/ault/spack/opt/spack/linux-centos8-zen/gcc-8.4.1/cuda-10.1.243-esf7lrqweehid7ugtyko5tirmuqvcvqp/lib64"])],
#       cmdclass={'build_ext': cpp_extension.BuildExtension})

setup(name='sparse_coo_tensor_cpp',
      ext_modules=[Extension(name='sparse_coo_tensor_cpp',
                             sources=['sparse_coo_tensor.cpp'],
                #             library_dirs=["/apps/ault/spack/opt/spack/linux-centos8-zen/gcc-8.4.1/cuda-10.1.243-esf7lrqweehid7ugtyko5tirmuqvcvqp/lib64"],
                                            #  /apps/ault/spack/opt/spack/linux-centos8-zen/gcc-8.4.1/cuda-11.8.0-fjdnxm6yggxxp75sb62xrxxmeg4s24ml/lib64  # this is where the newer cuda lives
                             extra_compile_args=["-lcusparse"])],
      cmdclass={'build_ext': cpp_extension.BuildExtension})
# setup(name='sparse_coo_tensor_cpp',
#       ext_modules=[Extension(name='sparse_coo_tensor_cpp',
#                              sources=['sparse_coo_tensor.cpp'],
#                              libraries=["/apps/ault/spack/opt/spack/linux-centos8-zen/gcc-8.4.1/cuda-10.1.243-esf7lrqweehid7ugtyko5tirmuqvcvqp/lib64"],
#                              extra_compile_args=["-lcusparse"])],
#       cmdclass={'build_ext': cpp_extension.BuildExtension})
