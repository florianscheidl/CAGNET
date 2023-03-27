from setuptools import setup, Extension
from torch.utils import cpp_extension

setup(name='sparse_coo_tensor_cpp',
      ext_modules=[cpp_extension.CppExtension('sparse_coo_tensor_cpp', ['sparse_coo_tensor.cpp'],
                                              extra_compile_args=["-lcusparse"],
                                              include_dirs=["/apps/ault/spack/opt/spack/linux-centos8-zen/gcc-8.4.1/cuda-10.1.243-esf7lrqweehid7ugtyko5tirmuqvcvqp/include",
                                                            "/apps/ault/spack/opt/spack/linux-centos8-zen/gcc-8.4.1/cuda-10.1.243-esf7lrqweehid7ugtyko5tirmuqvcvqp/lib64"],
                                              extra_link_args=["-lcusparse_static", "-lcudart_static", "-lpthreat", "-ldl"],)],
      cmdclass={'build_ext': cpp_extension.BuildExtension})
