from setuptools import setup, Extension
from torch.utils import cpp_extension

setup(name='sparse_coo_tensor_cpp',
      ext_modules=[cpp_extension.CppExtension('sparse_coo_tensor_cpp', ['sparse_coo_tensor.cpp'],
                                              extra_compile_args=["-lcusparse"],
                                              include_dirs=["/opt/nvidia/cudatoolkit10.2/10.2.89_3.28-2.1__g52c0314/include",
                                                            "/opt/nvidia/cudatoolkit10.2/10.2.89_3.28-2.1__g52c0314/lib64"],
                                              extra_link_args=["-lcusparse_static", "-lcudart_static", "-lpthread", "-ldl"])],
      cmdclass={'build_ext': cpp_extension.BuildExtension})
